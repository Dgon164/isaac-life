---
name: world-gm
description: "2026-07-03 World GM v1 built (owner's design: omniscient generative tester, information earned not given): primitives programmed / laws emergent / oracle-only grading beyond observed range; probe loop closes confirm() automation; produced 2 new engine findings (form-true label over-generous; sum-of-singles loses to product impostors)"
metadata: 
  node_type: memory
  type: project
  originSessionId: cd9b45ec-11ca-4e25-8fd3-0996466c7e2b
---

**Owner's design (2026-07-03, his words):** GAN-inspired but no nets — "omniscient world generator and tester... all it does is say yes or no or give results of a specific result. isaac has to earn the information, it is not given, just validated" + "we define the rules, but not the interactions... discovers meta or tertiary rules that are not explicitly programmed in but are emergent."

**Built:** `experiments/world_gm.py` (paperclip 390566e; synced to isaac_project rebuild/ d4a1314). Architecture:
- `World` class holds hidden truth, never leaks; verbs = `observe(n)` (cost n) / `run(x)` (one chosen experiment = the probe verb, cost 5) / `submit(f)` (graded on hidden inputs, half INSIDE half BEYOND observed range — beyond-range grading is what catches range-valid surrogates claiming form-true).
- 4 generative world types, laws emergent not written: EXCHANGE (antisymmetric swaps → conservation/equilibrium emerge), CHAIN (hidden middle variable → composed tertiary exponent α·β), GATED (conditional interaction → compound structure, designed probe of the compound-door gap), NULL (refusal is the win).
- Player loop: observe → discover → **probes answered by GM → confirm() (resolution no longer manual)** → scope self-check (spend budget beyond own hull, validate_law, re-learn with earned points) → submit.
- Scorecard separates SOLVED (capability) from HONEST (calibration: did the engine's own scope label hold up externally?) — "capability misses are findings; a scope label that doesn't hold is the kill."

**Wins on v1:** composed tertiary law recovered exactly (form-true, never programmed); NULL correctly refused (accounting 0/0/100 = GM truth); gated solved by smooth surrogate valid beyond range (0.91); one honest self-downgrade (UNDERSTOOD→PARTIAL after failed scope check).

**Two NEW ENGINE FINDINGS (the GM's product, recorded in RESULTS_LEDGER):**
1. **form-true scope label over-generous** — engine edge check tests only the outer quartile of the OBSERVED cloud; 2/3 form-true labels failed the GM's beyond-range audit. Fix options: rename label to "edges-hold", or earn "form-true" via beyond-hull validation. = the calibration audit (owner priority 4) made mechanical.
2. **sum-of-many-singles pathology** — a plain 5-var linear mixing law (exactly in-class, R²=1 achievable) loses the residual-correlation contest to product/cos impostors on positively-correlated support; not recovered even with earned far points. The discovery battery has NO plain-sum case — blind spot. Battery case + enumerator fix queued.

**Next (v2 ideas, owner-aligned):** calibration audit at scale (100 worlds → the ONE trust number: P(form-true | claimed form-true)); world families that rhyme (exercise analogy transfer/ledger warm starts across worlds); temporal worlds (waves/clock under the GM); enumerator fix for linear sums; scope-label fix; wire probe-loop pattern into engine (shrug→discover→probe reflex). Related: [[paperclip-audit-2026-07-03]], [[isaac-unsupervised-invariant-discovery]].
