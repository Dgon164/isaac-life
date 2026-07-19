---
name: box-to-matrix-translation
description: Net-lens boxes translate into his matrix as feature-value→class doors; log-likelihood matmul beats the box (2026-07-01)
metadata:
  type: project
---

**Result (2026-07-01, verified on held-out sklearn digits, lens=40 dims):** the net-extraction **box** design (`crystallize_features`/`classify_features`: per-class per-dim `[lo,hi,med]` + numpy count/centroid decision) translates into Isaac's **matrix** cleanly. Mapping: feature `d`=value `v` → a **node** `d{d}={v}`; class `c` → **delta node** `class:c`; "value in [lo,hi]" → a **door** `d{d}={v}→class:c`; interval = door **support**; median = weight **peak**; classify = **one matmul** `y=W@x` (x = multi-hot over the point's feature-values) + argmax.

**The door-WEIGHT is what matters** (all are one matmul over the same doors):
- `P(class|fv)` col-norm → 0.856
- binary in-range (pure box count) → 0.807
- box replica (count − dist) → 0.870
- **Naive-Bayes log-likelihood `Σ_d log P(fv|c)` → 0.922** ← BEATS numpy box (0.900)

**Takeaway:** the box's 3-number `lo/hi/med` summary is LOSSY; keeping the full per-value count profile as door-weights (log-lik weighting) is richer and more accurate. So the matrix-native rule = **stop fitting boxes; observe `feature-value→class` doors, weight by log-likelihood, decide by matmul.** Readable (each door = "this value at this dim implies this class by this weight"), his primitive decides, box still recoverable from door support/peak. This is the clean template for how any [[operation-paperclip]] lens hands off to the cortex.

**Why:** user's insight — "boxes were a variation of the matrix." Vindicated + improved. Ties to the hand-coding audit (item #6: box decision was numpy, now his matmul). Prototype scripts in scratchpad (box_to_matrix.py, box_weights.py); NOT yet formalized into isaac.py. Preserver/persistence [[disabled 2026-07-01]] while auditing. Related: [[isaac-working-style]] (decide inside Isaac), [[nn-transplant-carriers]].
