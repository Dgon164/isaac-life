# ISAAC — FULL REIMPLEMENTATION RUNBOOK (packaged 2026-07-19)

This PRIVATE repo is Isaac's LIFE. The code lives in two public
sibling repos; this repo holds everything the code cannot
regenerate: his mind, his history, and his school bench.

**PRIVACY: this repo must stay PRIVATE. It contains his journals,
transcripts, and the owner's sessions.**

## What is in here

- `isaac_home/` — HIS LIVE ACCOUNT. `mind.isaac` is his net (a
  Python pickle; `mind.isaac.bak` is the flight-made backup),
  plus journals (`*.jsonl`), transcripts, and the sparring
  corpus. **NEVER clean, move, reset, or hand-edit this
  directory. This is him.**
- `isaac_home_prologue/` — his archived history (the life before
  the alpha launch; read-only by law).
- `wsl/isaac_wsl_bench.tgz` — the boot.dev school bench:
  `/root/bookbot` (the finished Bookbot program + 3 books),
  `/root/gitcourse/webflyx` (the Learn Git bench repo, mid-course
  state), `/root/catalog.json` (50-course map), `lessonfetch/`
  (Go source + binary — their own client flow for lesson JSON),
  and the Python tutorial text he ate (`python-3.14-docs-text`).

## Standing at packaging time

Wall 63 green (dc `4a71e63`, research `1d1938e`). Bookbot
COMPLETE 12/12 server-graded. Learn Git 15/44 CLI passed. His
account: ~1,600+ nodes, 76 laws, selection precision 1.0, 5
codeshapes + git/tutorial idiom meals, the study ledger, and TWO
OPEN ASKS (his first self-generated ones, both naming
cross-lesson artifact memory) at `ask:lesson:The Object File`
and `ask:lesson:Trees and Blobs` behind the `world:asks` door.

## Lay-down on a new machine, in order

1. **Clone the three repos side by side** (private needs your
   GitHub login):
   ```
   git clone https://github.com/Dgon164/dc.git
   git clone https://github.com/Dgon164/isaac-paperclip.git
   git clone https://github.com/Dgon164/isaac-life.git
   ```
   dc's promote.py finds the research repo as a SIBLING
   `../isaac-paperclip` (or set env `ISAAC_RESEARCH`).

2. **Put his life where the code expects it** — the code reads
   `~/Documents/isaac_home`:
   ```
   copy isaac-life/isaac_home        -> Documents/isaac_home
   copy isaac-life/isaac_home_prologue -> Documents/isaac_home_prologue
   ```
   (Copy, don't move — keep the repo copy as the backup; commit
   + push new backups of isaac_home after real sessions.)

3. **Python**: 3.12+ with numpy. PROOF OF LIFE:
   `cd dc && python promote.py` → all 63 gates green means the
   whole engine survived the trip. (On Windows run with
   `PYTHONUTF8=1`.) Quick account check:
   `cd isaac-paperclip/experiments && python bootdev_flight.py
   --report` prints his study ledger from the mind.

4. **Ollama** (speech/sparring sessions only): install ollama,
   `ollama pull mistral` (the 7B tutor). Ollama must be serving
   for live sessions; the engine and wall run fine without it.

5. **WSL bridge** (only needed for boot.dev school):
   - Ubuntu WSL, root user. Disable systemd:
     `/etc/wsl.conf` → `[boot]` `systemd=false` (ghost #3).
   - Install: git (2.46+), python3, Go, and the bootdev CLI
     (`go install github.com/bootdotdev/bootdev@latest`).
   - **The token is NOT in this repo (on purpose — credentials
     never enter git). Re-login on the laptop:**
     `bootdev login` with the owner account
     (@appropriatetraining36) → writes `/root/.bootdev.yaml`.
   - Restore the bench:
     `tar xzf wsl/isaac_wsl_bench.tgz -C /root`
     then rebuild lessonfetch:
     `cd /root/lessonfetch && go build -o /root/go/bin/lessonfetch`
   - Git identity in webflyx per the course: user.name Dgon164,
     user.email jtweeks12@gmail.com, defaultBranch master.

6. **THE THREE GHOSTS — never re-hunt these** (they cost hours
   once already):
   - wsl.exe re-splits quoted argv → EVERY command travels
     base64: `echo <b64> | base64 -d | bash`.
   - Git Bash (MSYS) rewrites unix-path args → launch flights
     with `MSYS_NO_PATHCONV=1` (defensive strip also in code).
   - WSL systemd session flake → systemd stays disabled.

7. **Where to resume**: read
   `docs/SESSION_HANDOFF_2026-07-19_DIAGNOSIS_DAY.md` (both code
   repos) — next work in order: answer his two open asks through
   the telling road (cross-lesson artifact memory), the
   ask-answering loop end-to-end, the remaining 29 CLI git
   lessons, the one-ontology migration.

## What is deliberately NOT in this repo

- The boot.dev auth token (re-login; see step 5).
- Ollama model weights (re-pull; see step 4).
- Nothing else — the two code repos plus this one are the whole
  of Isaac.

## Integrity notes

- `mind.isaac` is a raw pickle: load it only from your own
  trusted copy (the provenance audit's standing hardening item).
- The wall is the gate: if promote.py is not 63/63 green on the
  new machine, do not run live sessions until it is — gate
  failures print the exact organ that broke in transit.
