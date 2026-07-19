---
name: isaac-build-state-doc
description: Keep the ISAAC build-state doc updated whenever a capability changes
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3a7d1589-8553-435a-a6a5-a4d70af922f1
---

The user established (2026-06-22) a living **build-state doc**: `ISAAC_BUILD_STATE.md` in the working bundle (`files (63)/extracted/isaac_bundle/`). It's the single source of truth for what Isaac can do *right now* — capability table with status tags (SOLID/RAN/PARTIAL/OPEN), the his/wired-retina ledger, file index, known limits, and a changelog of savepoints.

**Why:** the Manual covers theory but goes stale on capabilities; the user wanted one always-current page so the build state is never guessed.

**How to apply:** whenever you add, change, or break a capability, update `ISAAC_BUILD_STATE.md` in the SAME step (not as an afterthought) — adjust the capability row + status, and append to the changelog for a meaningful savepoint. Status changes by RUNNING, not restating (per [[isaac-working-style]]). Keep it capability-focused and maintainable, not verbose. See [[isaac-project-state]] for the detailed running log.
