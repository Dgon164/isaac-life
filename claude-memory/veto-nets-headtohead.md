---
name: veto-nets-headtohead
description: "Four-valued-connections project (veto gates + 0/-0 ledger) at isaac_project/veto_nets/ — OWNER VERDICT 2026-07-11: FAILURE/SHELVED as a performance play; numbers kept per wrong-kept law"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4ad6cda5-802d-4837-87cf-3fead5c6e793
---

**OWNER VERDICT (2026-07-11, same day as the run): FAILURE — shelved.**
His words: took forever, didn't resolve anything, scores not good, too
much power/GPU time. Do NOT re-pitch veto nets as an accuracy/efficiency
thread. Classification per the wrong-kept law ([[wisdom-laws]]): the veto
MECHANISM is real (holdout 1.000 vs 0.501, zero cost when unused) but it
is a robustness property, NOT a performance win on standard data — dense
beat it on every raw-accuracy and compute metric. For the record: actual
GPU cost was ~15 min total on the 3090. If the owner ever returns here,
the one live unexplored edge is prune→finetune / real exception-
structured data; otherwise leave it.

**Project home: `Documents/isaac_project/veto_nets/`** — the four-valued
connection experiments (+1 vote / 0 tested-irrelevant / -0 never-priced /
-1 multiplicative veto gate). exp1–4 verified per README; `fast_veto.py`
is the wide-layer gate rewrite (matmul gate for binary inputs, verified
identical to VetoLinear, max diff 5e-7). `hh_bench.py` = head-to-head
suite; all numbers in `RESULTS_HEADTOHEAD.md` + `results/*.csv`
(everything kept: acc, params, MACs, wall-clock, memory, prune curves,
veto census).

2026-07-11 head-to-head results (means over seeds 7/23/42, full test set):
- MNIST raw: dense wins every width — matched params (203k) dense 0.9767
  vs veto 0.9493; matched MACs dense +3.4 pts. Fashion @128: 0.8402 vs
  0.8117. The anti-superposition tax, measured. Veto 2.4× slower train,
  ~6× slower inference on GPU at same width.
- Exception holdout (B=1,k=3 unseen): veto 1.000 every seed, dense 0.501.
  No-structure control: both 1.000 — the bias costs nothing unused.
- No-retrain magnitude pruning: veto overtakes at 20% density; at 10%
  veto 0.9073 vs dense_relu 0.7621 (+14.5). **Caveat that gates the
  efficiency claim: dense@32 trained small (0.9605 @ 25k conns) still
  beats veto@256 pruned to ~27k (0.9073).** Prune→fine-tune head-to-head
  = the deciding next experiment, not yet run.
- Crystallization smell confirmed on real data: ~578 mid-range vetoes
  @256, hardening costs 0.9553→0.9486 (synth tasks: zero cost). Veto
  needs ≥15-epoch tau anneal on MNIST or collapses to chance (0.1135 @
  3 ep — `probe_mnist_veto.py` is the record).
- Trap flagged: pruned-dense ood=1.0 rows in hh_prune CSV = broken
  model predicting all-zeros, never quote.

Next levers (order): prune→finetune duel; real data WITH exception
structure (mislabel resistance, README direction 3); sparse kernel for
hardened nets (Raspberry-Pi angle, ties [[lost-einsteins-mission]]);
crystallization pressure. Vetoes-as-first-class ties [[design-intent-sheet]]
checklist item 8.
