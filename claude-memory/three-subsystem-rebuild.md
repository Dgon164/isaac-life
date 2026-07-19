---
name: three-subsystem-rebuild
description: 2026-07-01 — all three threads (SIS structure / net-extractor / enumerator) diagnosed + rebuilt clean in isaac_project/rebuild/; all 3 rebuilds WORK head-to-head vs faithful broken mechanisms on planted ground truth
metadata: 
  node_type: memory
  type: project
  originSessionId: 6042f9ac-13f8-474e-9f55-13c24931ab25
---

On 2026-07-01 the user reported all three ISAAC threads have major issues and asked for full rebuilds + comparison vs the broken versions. Done same day in `Documents/isaac_project/rebuild/` (RESULTS.md has the full numbers). Diagnosis first (3 parallel explorers), then minimal clean mechanisms per [[capability-audit-standard]], numpy-only, mechanism-under-test makes every decision.

**The three diseases (first two are the same disease — hard binary membership where graded basis-aware comparison is needed):**
1. SIS/Isaac: `_crystallize()` stores members-only, no uptake edges; binary doors → confirms audit suspect for "assembles but never behaves differently".
2. Net-extractor: axis-aligned box ceiling (covtype 0.62 vs net 0.82) + encoding-dependence.
3. Enumerator = Stage-2 term enumerator of equation discovery (`interaction_solver.py`, m_jj R² 0.075) — NOTE: user's word "enumerator" was ambiguous; I identified it as Stage-2 term enumeration (runner-up meaning: the counting/inventory subsystem). Not yet confirmed by user.

**Rebuilds (all WORKS):**
- `doors_proximity.py` — proximity doors: observed quantile-histogram distributions per class/dim, scored by one log-likelihood matmul, formed in a **null-gated basis** (rotate only along correlations beating 3/√n — "the basis itself must beat chance"; plain PCA smeared correlation-free data). vs boxes: parity on friendly data, 99.0% vs 88.0% on diagonal, graded remote-vs-none (box gives hard 0), and **100% vs 82.2% verdict-invariance under re-encoding** (box doors describe the encoding — the deepest-untested-assumption, now measured).
- `composition_uptake.py` — whole = parts + uptake edges (provider→affordance→consumer), operability by fixed-point propagation; passes all 7 audit-2.3 checks incl. dismantled-engine control and engine→car level-up; membership-only fails (c),(d) by construction.
- `enumerator_staged.py` — transcendental atoms (cos/sin/cosh of pairwise diffs) + beam growth around admitted terms + permuted-null admission (max-over-candidates null) + dual-track (lin/log) missing-var recovery. Recovered planted pt1·pt2·(cosh(e1−e2)−cos(f1−f2)) EXACTLY (R² 1.000) where faithful poly-L1 walls at 0.609/16 junk terms; says NO RULE on pure noise (old keeps 26 junk terms).

**Real-data results (same day, full datasets; details in rebuild/RESULTS.md):**
- Covtype 581k: proximity doors **56.2%** vs box 49.3% (recorded box-forest ~62%, net 82%). Marginal doors hit their declared expressiveness ceiling — covtype signal is interaction-heavy → compound doors (audit 2.11) is the designed next rung. Class-conditional-basis variant BROKEN (cross-class density calibration, ~20%; kept as marked failure in covtype_real_test.py).
- HIGGS full 11M (data re-downloaded to `isaac_project/data/HIGGS.csv.gz` + `.npy` cache): doors classifier **64.6% / AUC 0.700 in 22s on 10.5M rows** — beats logistic 64.2%, ≈ his-matmul best 65.0%, below MLP 69.1%/additive 0.765. Saturated in bins (64.7% at 128) → limit is additive structure, not resolution.
- Real m_jj: BOTH old (0.050) and new (0.033) fail — and the DECISIVE diagnostic: the TRUE form with scanned scales over ALL SIX jet pairs caps at **R² 0.065** → the relation is NOT in the recorded columns (missing jet masses/4-vectors + per-event pairing). Wall = data wall, PROVEN → epistemic verdict #4, not a method failure. Also observed the pos-3 identifiability trap in the wild: enumerator picked −0.70·cos(Δη) where truth wants +cosh (identical quadratic bulk, tails discriminate) — audit 2.6's warning is real.

**Next:** compound doors (2.11) = the one mechanism both covtype and HIGGS gaps point at; integrate uptake edges into `code/isaac.py`; enumerator needs identifiability stage (name tied candidates + request discriminating samples) per audit 2.6.
