---
name: higgs-standings
description: "Current lawful HIGGS record + the two false \"better\" memories to correct when the owner asks"
metadata: 
  node_type: memory
  type: project
  originSessionId: 52274304-73c2-43f1-84f4-fa781217fba1
---

**HIGGS lawful record (2026-07-09): 71.18% / AUC 0.7886** —
`experiments/higgs_pairs.py` in [[shareable-repo]]: 1D density signals +
220 pair doors (16×16 joint densities, pairs admitted by interaction
EXCESS over marginals) into one printable softmax. Saturation measured:
60→70.02, 150→70.73, **220→71.18 peak**, 300→70.28, 378→66.43 (60k
readout drowns). 1D-only record 68.07/0.7479 (`higgs_best.py`, which
also holds the formula road R²0.856, m_bb resonance, blind map 28/28).
Deep nets (~AUC 0.885 Baldi) still NOT matched — remaining gap = 3+-way
interactions.

**Why:** the owner repeatedly asks "didn't we do better?" Two false
memories to correct each time: (1) "detector eqn AUC 0.848" = torch MLP,
OVERTURNED 2026-07-05; (2) `cocktail_higgs*.py` F1 0.98 from the
Comparison Tower corpus = a SYNTHETIC 6-source toy named after the Higgs
recipe, not the real 11M-row dataset.

**How to apply:** quote only these complete numbers ([[report-plain-accuracy-numbers]]);
the pair-door win = the tower's "depth is question shape" law validated
on real data — next lever for the gap is 3-way/derived-feature doors.
