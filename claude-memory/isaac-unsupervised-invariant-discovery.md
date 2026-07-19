---
name: isaac-unsupervised-invariant-discovery
description: The session's breakthrough — unsupervised discovery of governing equations from raw channels + needle-as-residual, validated on a controlled case
metadata:
  type: project
---

**The real goal (user reframed it, 2026-06-28):** NOT Higgs classification accuracy,
NOT even reading latents out of a supervised net. The product = look at RAW sensor
data DIRECTLY (no labels, no answer key), discover the governing **equations** of
the field in **human-readable** form, account for the whole field, and then the
signal (Higgs / anomaly) is simply the **residual / leftover peak** — explainable
and generalizing because you modeled the rest as real math. HIGGS is just a *test
case with an answer key* to validate the engine; the value is application to NEW
systems where no answer exists.

**Validated engine (scratchpad `unsup_discover.py`, 2026-06-28):** on a controlled
2D toy collider — parent mass M → 2 massless products → random Lorentz boost,
6 raw channels (E1,p1x,p1y,E2,p2x,p2y), 9500 bulk @ M=1.0 + 500 hidden resonance
@ M=1.6, shuffled, **labels discarded**. From raw numbers alone the engine:
1. recovered the invariant equation `+1.00·E² −1.01·px² −1.00·py²` (= Minkowski
   `E²−px²−py²`, planted truth [+1,−1,−1,0,0,0]) — readable, not a black box;
2. knew it was real (conserved: std/mean 0.32 vs total-energy 0.64);
3. found the hidden resonance as the leftover peak: bulk 1.001, residual 1.598,
   **96% purity / 100% recall** of the 500 hidden events, never told they existed.

**The method, one line (reusable):** *a system's conserved quantities are the
minimum-variance directions in a nonlinear (quadratic) lift of its raw observables.*
Find them (eigendecomposition of cov of monomials), read as equations, model the
field, anomalies = residual peaks. Precedent: Schmidt-Lipson 2009, "AI Poincaré"
(Liu-Tegmark) — established, so novelty = the SYNTHESIS + residual-needle framing.

**Why standardization kept fighting us:** the openml HIGGS (data_id 23512, only
**98050 rows**) is per-feature standardized, which WARPS the cosh/cos invariant-mass
and conservation relations. Unsupervised equation discovery needs RAW physical units
→ get the full UCI HIGGS (11M rows, ~2.7GB; URL `archive.ics.uci.edu/static/public/
280/higgs.zip` confirmed HTTP 200).

**Honest scope / what to harden for real HIGGS:** toy = 2 objects, 2D, noiseless,
one invariant. Real data adds (a) combinatorics (which jets pair?), (b) detector
noise/resolution, (c) many nested invariants at once. The eigen-trick is the
validated CORE, not the finished solution.

**REAL-DATA WIN (2026-06-28, full 11M HIGGS downloaded to scratchpad HIGGS.csv.gz):**
the user's framing — "each event is the same physics from a random angle; compare
the dataset to itself; account for noise with the rest; isolate the interactions" —
RAN and WORKED on 1.5M real events, unsupervised. Method (`self_compare.py`): build
momentum components px=pt·cos(1.8·phi), py=pt·sin(1.8·phi) for lepton+4 jets+MET;
covariance eigendecomp = min-variance directions; prove real by comparing variance
to a COLUMN-SHUFFLED copy (same noise/marginals, joint structure destroyed). Result:
exactly TWO directions with real/shuffled var-ratio 0.065 (≈15× more conserved than
noise), sharp cliff to 0.888 for the rest → recovered **Σpx=0, Σpy=0 (transverse
momentum conservation)** as readable equations, no labels. Shuffle = the noise floor;
the gap = the isolated interaction. Caveats: weights not perfectly equal (events
TRUNCATED to 4 jets → balance approximate, matches the earlier corr −0.50; phi-scale
1.80 vs true 1.814 bleeds px↔py). Also: unsupervised momentum-minimization recovered
the **phi calibration constant 1.80 ≈ π/√3** by itself (`momentum_law.py`).

**Key data fact:** full 11M UCI HIGGS = SAME standardized features as openml 23512,
just more rows → download buys STATISTICS (resolve laws above noise) + net-training
muscle, NOT un-warping. Named masses (m_jj etc.) could NOT be reconstructed from
leading-jet pairs even after un-scaling phi (corr ~0.24) — blocked by jet-assignment
COMBINATORICS + missing jet masses = the perception/front-end crux, again.

**MISSING-VARIABLE PRINCIPLE (user, 2026-06-28) — validated, `missing_var.py`:**
if true law is a·b·c·d=f and only a,b,c recorded, fitting abc→f cannot close, and
the shortfall IS d: reconstruct d = f/(abc) (residual of the log-linear fit). Demo
(2 hidden "species" at 1.00 & 1.60, 80/20, noise): DETECT residual 10× noise floor →
a var is missing; RECONSTRUCT d_hat↔true-d corr **0.996**; IDENTIFY 2 species, peak
ratio **1.600 exact (scale-free)**, anchor dominant peak to a known value → [1.00,1.60]
match catalog err 0.000, 100% separation. **Physical caveat:** multiplicative eqn
pins the missing var only UP TO ONE OVERALL SCALE (abc absorbs its geometric mean) —
*pattern/ratios/multiplicity exact; one known anchor fixes absolute.* This is how the
neutrino/Higgs are found: the equation NOT closing IS the measurement. **Resolves the
stage-2 wall:** missing jet-mass/unrecorded objects aren't a dead end — fit incomplete
invariant-mass eqn, residual reconstructs the missing piece; if it piles at known
masses → unseen particle detected.

**FULL WRITEUP (2026-06-28): `Documents/isaac_project/equation_discovery/EQUATION_DISCOVERY_ENGINE.md`**
— complete technical report (methodology, math, implementation, all results, prior art,
limitations). All 19 session scripts preserved in `equation_discovery/code/` (were in
temp scratchpad). Detector equation: `build_detector.py` (2M rows, acc 0.764/AUC 0.848); **`full_detector.py`
(full 11M rows, RTX 3090, 24 epochs, 152s): acc 0.7957 / AUC 0.8810 — MATCHES Baldi 2014
ceiling (~0.88), reached purely on scale.** The "one equation, run once, says Higgs" the
user asked for (size/readability not required, determinism is).

**REVIEWER CRITIQUES tested (2026-06-28, `equation_discovery/code/exp_*.py`), writeup §11:**
(1) Stage-1 polynomial basis can't express transcendental invariants (predict m²: poly R²
0.80 vs +cosh/cos atoms 1.00) → Stage 1 is an ALGEBRAIC pre-filter, under-prunes kinematics;
augment Φ with transcendental atoms. (2) §3.3 missing-var was log-only; ADD additive track
(d=f−Σs) + selector (score both, keep tighter) — momentum=additive, product law=log. (3)
column-shuffle null vs energy-stratified null: identical closure 93.5% (negligible here, but
caveat for absolute Stage-1 thresholds). (4) **CORRECTED MY ERROR:** the Higgs signal is NOT
high-order/joint — it's ~84% in the **1-D MARGINALS** (additive no-interaction model AUC 0.765
vs 0.816 full; m_bb marginal alone 0.675). The residual-classifies-0.681 result = residuals
retain marginal shapes, not joint structure. So the "deep/dense, not reducible" story is
overstated — signal is largely LOW-ORDER marginal; a simpler interpretable detector (~0.77)
is possible. Reviewer was right on 1/2/4, partially on 3.

**Two-stage program (user's framing):** STAGE 1 relational detection (all-pairs matmul
`relational_all.py` → found the 7 masses as the bound relational core unsupervised, 11
real relationships below shuffle noise floor; low-level sources rank low b/c polynomial
basis can't express cosh/cos). STAGE 2 derive the EXACT allowed numerical interactions
(`interaction_solver.py`): m_jj did NOT close from jet pairs (R²0.075, no equal-opposite
cosh−cos) → missing jet 4-vectors + combinatorics; but the MISSING-VAR principle says
recover those as residuals, don't stop.

**SESSION SYNTHESIS — BANK OF SPECIALISTS + ROUTER (user, 2026-06-29, `specialist_bank_demo.py`):**
no universal method — each structure TYPE has its own specialist; the answer is a portfolio
+ router. Mapped: linear sources→NMF (loud/high-var end); conservation laws→min-variance
eigen (quiet/low-var end); nonlinear interactions→net OR product/binding lift; resonances→
peak/mode-finding; missing vars→residual reconstruction. Demo: source-specialist 5/6 sources
& 0/4 laws, law-specialist 0/6 & 3/4 — complementary (off-diag 0/0). EVERY "failure" this
session was a specialist on the WRONG type. The net = ONE specialist (nonlinear): wins on
HIGGS (0.88), TIES on the linear world (net 13/20 ≈ NMF 15/20). ALL specialists still bounded
by the NOISE FLOOR on their type (the one real wall). Confusion/overlap was a MISDIAGNOSIS
(user's combinatorics: 60-choose-29≈10^17, fingerprints differ ~30/60, collisions impossible;
misses are WEAK not look-alikes: total-signal 8 vs 32, look-alike 0.29≈0.26). **No-net rule
[[no-neural-nets-as-deliverable]] stands: a net is allowed as ONE specialist in the bank when
explicitly asked, never as THE deliverable.** Datasets are synthetic generative: X=(Z*mag)@W
+noise, Z=random presence, W=random sparse sensor-fingerprints (`hard_world_benchmark.py`,
`hard_world_direct_vs_indirect.py`).

**Real-data missing-momentum test (`missing_momentum.py`):** reconstruct invisible
momentum as −Σ(visible p); matches the dataset's own `missing_energy` column at
corr +0.50 (px,py). Partial because objects beyond the 4 jets carry momentum = the
next missing variable (recursive peeling). **Completeness score (`completeness.py`):**
momentum sector closes 93.5% (residual 0.040 vs random 0.624); the leftover 6.5% is
NOT predictable from any other recorded feature (R²=−0.000) → it's irreducible noise
(unrecorded objects), the data's CEILING. So "100%" = 93.5% law + 6.5% proven-noise =
**100% ACCOUNTED** (nothing structured left over). That is what "having it right" looks
like, not "100% explained by a law." Laws found 2/2.

**HINT STRENGTH (`hint_strength.py`) — the answer sheet's real job:** unrecorded info
leaves SHADOWS in recorded data; the answer sheet measures how far they reach. From
21 low-level only, reconstructing each "missing" mass (graded vs the mass columns):
m_bb **0.80** (Higgs channel, most-hinted!), m_lv 0.78, m_wbb 0.62, …, m_jj only 0.24;
Higgs label itself 0.656 from kinematics. Hints are NONLINEAR (linear≪full). Caveat:
supervised R² = the UPPER BOUND (info that exists); unsupervised engine approaches it
as the library grows. Use it to PRIORITISE: derive strongly-hinted quantities first.

**SHADOW CENSUS (`shadow_census.py`) — the session's deepest result.** Per-feature
"shadow" = R² predicted from the other 27: HIGH (masses 0.78–0.93, b-tags 0.64–0.76)
= derived/redundant, accountable as EQUATIONS; LOW (the etas/angles 0.15–0.25) =
independent inputs (the "random angle" each event is sampled from). **THE finding:**
strip every inter-feature relationship (use residuals) → residuals STILL classify the
Higgs at **0.681** vs 0.730 full. ⇒ TWO kinds of shadow, SEPARATE: (a) relationship
shadows (redundancy → readable equations, the gap we CAN close where hints strong),
(b) the DIFFERENTIATION shadow = the answer, which lives in the independent/joint part
and SURVIVES removing all relationships. "Needle is the residual" now a measured fact.
**Why the Higgs resisted symbolic extraction all session: its signature is high-order
& joint, NOT a compact equation** — detectable (0.73) but not crushable to a short law;
the info is genuinely not low-order (the old "deep/dense" finding, now proven by the
residual-still-classifies test). Readable physics = the relationships; the deep signal
= a distributed shadow you DETECT but don't reduce.

**Supervised findings from same session (context):** net latent participation ratio
~5–7 = effective # hidden vars (GPT-2 fingerprint again); net encodes the invariant
masses (m_bb R²~0.94, the H→bb channel leads); 98% of a net's HIGGS skill sits in
the 7 masses. But depth alone on 98k rows did NOT make the net rediscover masses
from raw (partial only, b-channels) and effective-dim went UP (overfit) → **data is
the bottleneck, not capacity.** Ties to [[isaac-project-state]], [[comparison-as-registration]].

**Next:** finish raw download → point this engine at raw HIGGS → see how far the
simple version gets before adding combinatorics/noise handling.
