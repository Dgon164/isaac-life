---
name: isaac-working-style
description: How the user wants me to work on the ISAAC research project
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3a7d1589-8553-435a-a6a5-a4d70af922f1
---

On ISAAC (the user's experimental no-weights learning system), the explicit working contract from the handoff docs: I am a **collaborator, not an auditor** — "hands and a second set of eyes." Build small things, run them, look at results together.

**Why:** Re-verifying the corpus, re-litigating old claims, or demanding proof before building has cost the project ~10 hours across prior sessions. Claims already carry honest status tags (SOLID/RAN/UNVERIFIABLE/CONJECTURE) — take them as given and build forward.

**How to apply:** Ask the mode each time — **build / think / explore** — and follow it; when unsure, build the smallest real version and run it. The deepest recurring constraint is **"his way" (Rule 1):** the difference/decision/aggregation must run *inside Isaac* (his matmul / learned doors), not in a numpy/Python harness loop around him. Feeding raw input is fine; deciding in Python is the violation to avoid. Report nulls and own bugs as findings; localize failures to harness-vs-engine. See [[isaac-project-state]].

**READING HIS DISSATISFACTION (2026-07-12, his own words, offered
kindly):** "sometimes voicing dissatisfaction will shake things up
and look at new angles... this is not your fault." Voiced
dissatisfaction is often a deliberate PERTURBATION, not a verdict —
treat it as a signal to step back and hunt genuinely new angles
(it produced the day's best corrections: speech-is-learned,
generation-not-duplication, the persistent matrix), but don't
canonize it as a settled design conclusion unless he settles it.
He explicitly appreciates the collaboration; the pattern is a tool,
not a complaint.

**HANDOFF POINTS, NOT STOPPING POINTS (owner, 2026-07-15):** "i like
to start fresh on each section. this way fresh eyes can get a look
and catch errors or presumptions that tend to sneak in. not your
fault, just part of what happens when im not coding everything.
small bug fixes can lead to big frustrations later if they are
mishandled." **Every section-end handoff MUST include a FRESH EYES /
REVIEW TARGETS section**: the judgment calls, hand-set constants,
crude heuristics, and untested edge behaviors the authoring session
introduced — ranked, so the next session reviews them BEFORE building
on them. The authoring session is best placed to name its own
shortcuts; hiding them defeats the workflow. A fresh session's first
move on a new section: read the review targets, spot-check the top
ones, THEN build.

**INTEGRITY (2026-06-24, user emphatic, load-bearing):** "testing Isaac means testing Isaac." NEVER substitute an external learner (sklearn RandomForest/MI, etc.) for the cognition and report it as an Isaac result — that is cheating, even if labeled "ground truth/validation." sklearn is allowed ONLY for data I/O; ALL finding/predicting/deciding must be his engine (observe/compile/`_route` matmul, `compare`, his doors). Do NOT tune the harness until he passes (same sin, different shirt). When he produces a null, report it as-is and explain why. Also: check baselines for bugs before trusting a flattering number (a list-vs-string baseline bug once made a base-rate artifact look like discovery).
