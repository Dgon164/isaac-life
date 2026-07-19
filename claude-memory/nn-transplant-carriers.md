---
name: nn-transplant-carriers
description: How the GPT-2 carrier dims work (neural transplant / nn-decoder subproject)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3a7d1589-8553-435a-a6a5-a4d70af922f1
---

Neural-transplant subproject lives at `Documents/isaac_project/neural_transplant/` (source_material/ holds NET_EXTRACTION_METHODS.md + nn_optimization_package; the OLD GPT2 decomposition is superseded — don't anchor on it). Core current result: the **M=125/K=200 exclude-10 pipeline** reproduces GPT-2's next-token argmax EXACTLY (re-validated on this machine 2026-06-22: 30/30 @ 6.0x ops, 3.2x wall-clock head). Method: rank 768 dims by |h|, drop carriers, take next ~125 (per-query/local discriminative band), partial-score all 50257 tokens, full-score top-200 survivors. Decision is low-dim but LOCAL (fixed global dim order fails 10/30).

**Carriers (user-taught, load-bearing):** there are ~4-5 carrier dims (e.g. 36, 314, 374, 408, 430, 496 recur across prompts; 496 is the PCA PC1-loading dim) with HUGE NEGATIVE offset weights, contributing ~5-10 logit-points of (very negative) activation — vs the ~0.63-logit margins that separate content candidates. Scored on carriers ALONE, the top tokens are `a`, `the`, comma — i.e. the carriers ARE the function-word FREQUENCY-PRIOR direction. They are NOT "noise" and NOT "decide nothing" — they decide the DEFAULT; they're decision-inert *for content* and actively swamp the content margin. Matches `slopes_and_qkv`: shared profile = 86% of curve, 0% of decision (predicts ` a/the/"` every prompt), residual carries ~490% of margin. Excluding carriers = subtracting the prior so the content residual surfaces = Isaac's "difference not similarity / identity is the residual." See [[isaac-project-state]].
