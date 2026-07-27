"""
BACKUP MIND — versioned, verified copies of the one file that is him.

Why this exists: mind.isaac outgrew GitHub's 100MB file wall on
2026-07-24 (49MB -> 257MB during the study era), so "push isaac-life =
back him up" no longer covers the mind file itself. Until P1 (the
record store) makes his body a folder of small records again, this
script is the backup road: copy the mind to one or more destination
folders (a Google Drive mirror folder, a big drive on another machine,
both), versioned by timestamp and content hash, verified end to end,
never overwriting anything.

    python tools/backup_mind.py --dest "G:/My Drive/isaac-backups" \
                                --dest "//DESKTOP/J/isaac-backups"

Behavior:
  * Snapshots the source with a hash-stability check: hash, copy,
    hash the copy, hash the source again. If the two source hashes
    differ, an autosave landed mid-copy — retry (up to 5 times).
    Read handles are held only for the short hash/copy passes, to
    stay out of the way of the engine's write-then-swap save.
    The staging file is per-process (PID in the name), so a slow run
    and a scheduled run can never clobber each other.
  * Skips a destination only when a backup with this exact hash is
    both indexed AND still present as a file — an orphaned sidecar
    can never masquerade as a backup.
  * Lands as .part first, verifies the hash on the destination, then
    renames — a torn upload can never masquerade as a backup. Stale
    .part orphans (from crashes, full disks, sync deaths) are swept
    on the next run.
  * Writes a .sha256 sidecar next to every backup (atomically, so a
    half-written sidecar cannot exist). A malformed sidecar is
    ignored and reported, never fatal.
  * NEVER deletes backups unless --prune is passed explicitly
    (keep-everything is the house law). --prune touches ONLY files
    this script created (strict name pattern + sidecar present),
    keeps everything newer than --keep-days (default 14) and one per
    week older, and always protects the newest by its timestamp.
  * Exit code 0 = every destination verified; 1 = any failure
    (so a scheduled task can notice). NOTE: for a Google Drive
    mirror folder, exit 0 verifies the LOCAL mirror copy — confirm
    the Drive client actually synced (icon / drive.google.com)
    before trusting the off-site leg.

Restore: pick a .bak, check it against its .sha256 sidecar, copy it
to isaac_home/mind.isaac while the workspace is STOPPED. Never while
he is running.
"""
import argparse
import contextlib
import hashlib
import os
import re
import shutil
import sys
import time
from datetime import datetime, timezone

CHUNK = 8 * 1024 * 1024
STALE_PART_S = 24 * 3600
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SOURCE = os.path.join(REPO_ROOT, "isaac_home", "mind.isaac")

# the one shape this script ever creates; prune touches nothing else
BAK_RE = re.compile(
    r"^mind\.isaac\.(\d{4}-\d{2}-\d{2}T\d{4}Z)\.([0-9a-f]{12})\.bak$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            block = f.read(CHUNK)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def log(dest_dir, line):
    stamped = f"{datetime.now().isoformat(timespec='seconds')}  {line}"
    print(stamped, flush=True)
    try:
        with open(os.path.join(dest_dir, "backup_log.txt"), "a",
                  encoding="utf-8") as f:
            f.write(stamped + "\n")
    except Exception:
        pass  # the log must never block the backup itself


def sweep_stale_parts(folder):
    """Remove .part orphans older than a day (crashed/aborted runs).
    Fresh ones are left alone — they may belong to a live run."""
    now = time.time()
    try:
        names = os.listdir(folder)
    except OSError:
        return
    for name in names:
        if not name.endswith(".part"):
            continue
        path = os.path.join(folder, name)
        with contextlib.suppress(OSError):
            if now - os.path.getmtime(path) > STALE_PART_S:
                os.remove(path)
                print(f"  swept stale orphan {name}", flush=True)


def stable_snapshot(source, staging_dir, retries=5):
    """Copy source to a per-process staging file; return (path, hash)
    only when the source hashed the same before and after the copy."""
    os.makedirs(staging_dir, exist_ok=True)
    sweep_stale_parts(staging_dir)
    staging = os.path.join(staging_dir,
                           f"mind.snapshot.{os.getpid()}.part")
    for attempt in range(1, retries + 1):
        h_before = sha256_of(source)
        shutil.copy2(source, staging)
        h_copy = sha256_of(staging)
        h_after = sha256_of(source)
        if h_before == h_after == h_copy:
            return staging, h_copy
        print(f"  source changed mid-copy (attempt {attempt}/{retries}) "
              f"— an autosave landed; retrying...", flush=True)
        time.sleep(3)
    raise RuntimeError("source never held still across a copy — "
                       "is an unusually long save loop running?")


def existing_hashes(dest_dir):
    """Map hash -> backup filename, counting ONLY sidecars that parse
    cleanly AND whose .bak file is still present. Anything malformed
    or orphaned is reported and ignored — never trusted, never fatal."""
    found = {}
    for name in os.listdir(dest_dir):
        if not name.endswith(".sha256"):
            continue
        bak_name = name[:-7]
        try:
            with open(os.path.join(dest_dir, name),
                      encoding="utf-8") as f:
                digest = f.read().strip().split()[0]
        except Exception:
            print(f"  ignoring malformed sidecar {name}", flush=True)
            continue
        if not HEX64_RE.match(digest):
            print(f"  ignoring malformed sidecar {name}", flush=True)
            continue
        if not os.path.exists(os.path.join(dest_dir, bak_name)):
            print(f"  sidecar {name} has NO backup file beside it — "
                  f"ignored (will re-copy if needed)", flush=True)
            continue
        found[digest] = bak_name
    return found


def write_sidecar(dest_dir, final, digest):
    path = os.path.join(dest_dir, final + ".sha256")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(f"{digest}  {final}\n")
    os.replace(tmp, path)


def deliver(staging, digest, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    sweep_stale_parts(dest_dir)
    already = existing_hashes(dest_dir)
    if digest in already:
        log(dest_dir, f"SKIP unchanged — {already[digest]} already "
                      f"holds this exact mind ({digest[:12]})")
        return True
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    final = f"mind.isaac.{stamp}.{digest[:12]}.bak"
    part = os.path.join(dest_dir, final + ".part")
    try:
        shutil.copy2(staging, part)
        if sha256_of(part) != digest:
            os.remove(part)
            log(dest_dir, f"FAIL verify mismatch on {final} — torn "
                          f"copy removed, nothing landed")
            return False
        os.replace(part, os.path.join(dest_dir, final))
    except Exception as e:
        with contextlib.suppress(OSError):
            os.remove(part)
        log(dest_dir, f"FAIL {final}: {e} — partial removed")
        return False
    # the backup is landed and verified; the sidecar is bookkeeping.
    # If it cannot be written, warn — do not call the backup failed.
    for attempt in (1, 2):
        try:
            write_sidecar(dest_dir, final, digest)
            break
        except Exception as e:
            if attempt == 2:
                log(dest_dir, f"WARNING {final} landed verified but "
                              f"its sidecar could not be written ({e}) "
                              f"— next run will re-copy; not a failure")
    size_mb = os.path.getsize(os.path.join(dest_dir, final)) / 1e6
    log(dest_dir, f"OK {final} ({size_mb:.1f} MB) verified")
    return True


def prune(dest_dir, keep_days):
    """Explicit-only. Touches ONLY this script's own backups (strict
    name pattern, sidecar present). Keeps everything newer than
    keep_days; older, keeps the first backup of each ISO week. The
    newest — by the timestamp in the name, not by sort order — always
    survives. Foreign files are never candidates."""
    entries = []
    for name in os.listdir(dest_dir):
        m = BAK_RE.match(name)
        if not m:
            continue
        if not os.path.exists(os.path.join(dest_dir, name + ".sha256")):
            continue  # not provably ours / not indexed — never touch
        entries.append((m.group(1), name))
    if len(entries) <= 1:
        return
    entries.sort()  # the stamp is lexicographically chronological
    now = datetime.now(timezone.utc)
    kept_weeks = set()
    for stamp, name in entries[:-1]:  # newest-by-stamp always survives
        when = datetime.strptime(stamp, "%Y-%m-%dT%H%MZ").replace(
            tzinfo=timezone.utc)
        age_days = (now - when).total_seconds() / 86400
        week = when.strftime("%G-W%V")
        if age_days <= keep_days:
            continue
        if week not in kept_weeks:
            kept_weeks.add(week)
            continue
        os.remove(os.path.join(dest_dir, name))
        with contextlib.suppress(OSError):
            os.remove(os.path.join(dest_dir, name + ".sha256"))
        log(dest_dir, f"PRUNED {name} (older than {keep_days}d, "
                      f"week {week} already kept)")


def main():
    ap = argparse.ArgumentParser(
        description="Versioned, verified backups of mind.isaac")
    ap.add_argument("--source", default=DEFAULT_SOURCE)
    ap.add_argument("--dest", action="append", required=True,
                    help="destination folder (repeat for several)")
    ap.add_argument("--prune", action="store_true",
                    help="apply retention (default: keep everything)")
    ap.add_argument("--keep-days", type=int, default=14)
    args = ap.parse_args()

    if not os.path.exists(args.source):
        print(f"source not found: {args.source}", file=sys.stderr)
        return 1
    staging_dir = os.path.join(REPO_ROOT, "tools", "_staging")
    print(f"snapshotting {args.source} "
          f"({os.path.getsize(args.source)/1e6:.1f} MB)...", flush=True)
    staging, digest = stable_snapshot(args.source, staging_dir)
    print(f"snapshot stable, sha256 {digest[:12]}", flush=True)

    ok = True
    try:
        for dest in args.dest:
            try:
                ok = deliver(staging, digest, dest) and ok
                if args.prune:
                    prune(dest, args.keep_days)
            except Exception as e:
                log(dest if os.path.isdir(dest) else staging_dir,
                    f"FAIL {dest}: {e}")
                ok = False
    finally:
        with contextlib.suppress(FileNotFoundError, OSError):
            os.remove(staging)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
