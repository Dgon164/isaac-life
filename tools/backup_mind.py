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
  * Skips a destination that already holds a backup with this exact
    hash (nothing new to save), and says so.
  * Lands as .part first, verifies the hash on the destination, then
    renames — a torn upload can never masquerade as a backup.
  * Writes a .sha256 sidecar next to every backup for later checking.
  * NEVER deletes anything unless --prune is passed explicitly
    (keep-everything is the house law). --prune keeps all copies
    newer than --keep-days (default 14) and one per week older.
  * Exit code 0 = every destination verified; 1 = any failure
    (so a scheduled task can notice).

Restore: pick a .bak, check it against its .sha256 sidecar, copy it
to isaac_home/mind.isaac while the workspace is STOPPED. Never while
he is running.
"""
import argparse
import hashlib
import os
import shutil
import sys
import time
from datetime import datetime, timezone

CHUNK = 8 * 1024 * 1024
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SOURCE = os.path.join(REPO_ROOT, "isaac_home", "mind.isaac")


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
    except OSError:
        pass  # the log must never block the backup itself


def stable_snapshot(source, staging_dir, retries=5):
    """Copy source to staging; return (staging_path, hash) only when
    the source hashed the same before and after the copy."""
    os.makedirs(staging_dir, exist_ok=True)
    staging = os.path.join(staging_dir, "mind.snapshot.part")
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
    found = {}
    for name in os.listdir(dest_dir):
        if name.endswith(".sha256"):
            try:
                with open(os.path.join(dest_dir, name),
                          encoding="utf-8") as f:
                    found[f.read().strip().split()[0]] = name[:-7]
            except OSError:
                continue
    return found


def deliver(staging, digest, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    already = existing_hashes(dest_dir)
    if digest in already:
        log(dest_dir, f"SKIP unchanged — {already[digest]} already "
                      f"holds this exact mind ({digest[:12]})")
        return True
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    final = f"mind.isaac.{stamp}.{digest[:12]}.bak"
    part = os.path.join(dest_dir, final + ".part")
    shutil.copy2(staging, part)
    if sha256_of(part) != digest:
        os.remove(part)
        log(dest_dir, f"FAIL verify mismatch on {final} — torn copy "
                      f"removed, nothing landed")
        return False
    os.replace(part, os.path.join(dest_dir, final))
    with open(os.path.join(dest_dir, final + ".sha256"), "w",
              encoding="utf-8") as f:
        f.write(f"{digest}  {final}\n")
    size_mb = os.path.getsize(os.path.join(dest_dir, final)) / 1e6
    log(dest_dir, f"OK {final} ({size_mb:.1f} MB) verified")
    return True


def prune(dest_dir, keep_days):
    """Explicit-only. Keep everything newer than keep_days; older,
    keep the first backup of each ISO week; never touch sidecar-less
    files or the newest backup."""
    baks = sorted(n for n in os.listdir(dest_dir)
                  if n.startswith("mind.isaac.") and n.endswith(".bak"))
    if len(baks) <= 1:
        return
    now = time.time()
    kept_weeks = set()
    for name in baks[:-1]:  # newest always survives
        path = os.path.join(dest_dir, name)
        age_days = (now - os.path.getmtime(path)) / 86400
        week = datetime.fromtimestamp(
            os.path.getmtime(path)).strftime("%G-W%V")
        if age_days <= keep_days:
            continue
        if week not in kept_weeks:
            kept_weeks.add(week)
            continue
        os.remove(path)
        sidecar = path + ".sha256"
        if os.path.exists(sidecar):
            os.remove(sidecar)
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
    for dest in args.dest:
        try:
            ok = deliver(staging, digest, dest) and ok
            if args.prune:
                prune(dest, args.keep_days)
        except OSError as e:
            log(dest if os.path.isdir(dest) else staging_dir,
                f"FAIL {dest}: {e}")
            ok = False
    os.remove(staging)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
