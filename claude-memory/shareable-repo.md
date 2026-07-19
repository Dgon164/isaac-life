---
name: shareable-repo
description: Curated private git repo at Documents/isaac-paperclip; consolidated engine = code/isaac.py (6/6 superset)
metadata: 
  node_type: memory
  type: project
  originSessionId: 6042f9ac-13f8-474e-9f55-13c24931ab25
---

**Shareable repo (built 2026-07-01):** `C:\Users\jtwee\Documents\isaac-paperclip\` — a **curated, share-safe** subset (user's choice: **Private** visibility, curated subset). Git-initialized, first commit on `main`, 13 files. Local git identity set in-repo only (name `jtwee`, email jtweeks12@gmail.com); global git config untouched.

Contents: `isaac.py` (the consolidated engine), `PAPERCLIP_MANUAL.md`, `README.md`, `requirements.txt`, `docs/` (THE_COMPLETE_PICTURE, ISAAC_THEORY_OF_OPERATION, EQUATION_DISCOVERY_ENGINE, HIGGS_writeup), `demos/` (crystal_in_isaac, unsup_discover, interaction_extract, higgs_residual). Excludes personal story / history (share-safe).

**CONSOLIDATION FINDING (answers "is there one up-to-date Isaac"):** there were THREE divergent isaac.py — `Downloads/New folder (3)/isaac.py` (57KB, stale), `2_the_machine/code/isaac.py` (85KB, the reorg reference I ran+edited this session), and **`code/isaac.py` (90KB, the LIVE superset)** which uniquely has `recognize_doors`+`recognize_matrix` and passes 6/6. `code/isaac.py` is the authoritative base; the shareable repo uses it. The working project still has the split — reconciling code/ vs 2_the_machine/code/ is open (Jun-27 handoff flagged it too).

**TWO private repos now exist (GitHub account = Dgon164):**
1. **https://github.com/Dgon164/isaac-paperclip** — the CURATED share-safe subset (consolidated isaac.py + manual + key docs + demos), 13 files.
2. **https://github.com/Dgon164/isaac-project** — the FULL project (pushed 2026-07-01 to share with a collaborator), 416 files, git-initialized IN PLACE at `Documents/isaac_project/`. EXCLUDES (via `.gitignore`): `4_the_story/` (personal), the 3 `CONFIDENTIAL_*`/`ISAAC_Confidential_Overview` briefings, and regenerable data (`**/data/`, `*.npz/npy/tar.gz/zip`). To share: add collaborator via repo Settings→Collaborators or `gh api -X PUT repos/Dgon164/isaac-project/collaborators/<user>`.

**UPDATE 2026-07-02: BOTH repos updated + pushed with the discovery-stack work.** isaac-paperclip: new engine (suite 10/10), `docs/` gained WRITEUP_FOR_REVIEW, Understanding_as_Closure, AUDIT_STANDARD_v1, VERDICT_SHEET, CURRICULUM_HARD_TESTS, ISAAC_BUILD_STATE; new `experiments/` = full rebuild harness (16 scripts + reports + battery CSVs) with sys.path rewritten repo-relative; README self-test 6/6→10/10 + update section (commit de89841). isaac-project (full/collaborator repo): everything committed in place (commit d055783); gitignore's `**/data/` correctly excluded the 2.8GB HIGGS re-download. `gh auth` NOW WORKS (user logged in as Dgon164 since June) — the old auth blocker is gone.

**GitHub status: DONE — pushed live 2026-07-01.** Original curated repo = **https://github.com/Dgon164/isaac-paperclip** (PRIVATE, branch `main`). GitHub account = **Dgon164**. `gh` CLI installed via winget (v2.95.0) at `%LOCALAPPDATA%\Microsoft\WinGet\Packages\GitHub.cli_.../bin/gh.exe` (not on PATH in the assistant's shell — locate with `find`). `origin` remote set, `main` tracks `origin/main`. To push future updates: `cd` to the repo, `git add -A && git commit && git push`. Relates to [[operation-paperclip]], TODO.md "make it a private repo" (now satisfied).
