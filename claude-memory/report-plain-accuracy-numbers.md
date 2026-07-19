---
name: report-plain-accuracy-numbers
description: "How the user wants results reported, and the honest reliability status of the counting/discovery engine"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 52274304-73c2-43f1-84f4-fa781217fba1
---

**Report results as plain "% correct" accuracy, NOT technical metrics.** The user
cannot interpret ARI / R² / participation-ratio / eigenvalue numbers and explicitly
asked to stop using them ("can't tell jack shit from the numbers you are giving me").
Always translate to "got it exactly right X% of the time", "invents things Y%",
"misses things Z%". Give EXACT values. The user wants reliability **right in totality,
not partiality**, and wants core capabilities *locked down* before building further.

**RULE ESTABLISHED 2026-07-05 — COMPLETE NUMBERS ONLY, NEVER RELATIVE:**
(owner verbatim) "if it solves something in its entirety and gets 100% on an
answer like detecting a 0, it didn't get 100%, it got 10% plus whatever the
rest of the digits are. if it's only getting 64.5% do NOT pad it or tell me
it's doing better than others."
- **Always report against the WHOLE task.** Coverage-conditioned accuracy
  must be multiplied through: "74.2% on the 31/200 it answered" = **11.5%
  of the whole test set correct** — report THAT first; the conditioning is
  a footnote at most. Per-class wins convert to their share of the full
  task (perfect on one digit of ten = 10%).
- **No padding, no consolation comparisons.** Never "better than chance",
  "beats the baseline", "commodity-respectable" as a dressing on a low
  number. 64.5% is 64.5%.
**Why:** relative/conditional numbers confused and misled him — a padded
partial reads as progress that isn't there.
**How to apply:** before reporting any accuracy, ask "is this the number
for the ENTIRE task?" — if not, convert it; state comparisons only as raw
facts when asked, never as framing.

**Honest reliability status (measured 2026-06-28, `reliability*.py`):** the engine's
core "how many hidden things are in this system" count is **NOT locked down.**
- Best method = all-at-once parallel analysis (real eigenspectrum vs shuffle floor):
  **~52% exactly right, 0% invents, ~48% undercounts.** Because it never overcounts,
  its number is a **trustworthy FLOOR** ("at least N things") — that part IS reliable.
- FOUR attempts to beat it all FAILED: threshold tuning (no help); cross-validation/BCV
  (84% invents); naive deflation peeling (96% invents); held-out peeling (94% invents).
  All the "peel one signal at a time" versions OVERCOUNT because deflation leaves a
  rank-deficiency artifact that the "is there one more?" test reads as real signal.

**The user's epistemic reframe (adopt the STANCE, not the broken algorithm):** always
assume some unaccounted hidden thing remains; report "at least N, possibly more", never
"exactly N". The stance is correct; the peeling *implementation* is unreliable. Reliable
to build on TODAY = (1) the floor count, (2) the epistemic stance. Reliable exact
counting / reliable peeling = unsolved, needs careful residual-significance-under-
deflation work, NOT quick attempts. Ties to [[isaac-unsupervised-invariant-discovery]],
[[no-neural-nets-as-deliverable]].
