---
name: capability-audit-standard
description: 2026-07-01 — Capability Audit Standard v1.0 adopted as the governing objectives doc; saved at isaac_project/audit/AUDIT_STANDARD_v1.md; strict WORKS/BROKEN/NEVER-BUILT verdicts in dependency order (doors first)
metadata: 
  node_type: memory
  type: project
  originSessionId: 6042f9ac-13f8-474e-9f55-13c24931ab25
---

On 2026-07-01 the user adopted the **ISAAC Capability Audit Standard v1.0** — the definitive objectives document for the whole system. Saved to `Documents/isaac_project/audit/AUDIT_STANDARD_v1.md` (verdict sheet has an added "Evidence (the number)" column per [[report-plain-accuracy-numbers]]).

Core content: 13 capabilities (differentiation atom, doors/dims/box-ranges, holarchy, crystallizer-as-FCA, null detection, equation recovery, keypoints, completeness scoring, shadow census, permuted-null infra, flat+compound classification, transducer, scaling curves), each with a perfect-state definition, load-bearing property, and ground-truth test. Verdicts strict: WORKS / BROKEN / NEVER BUILT, no partial credit. Audit runs in **dependency order: doors first** (their resolution bounds everything downstream), then atom, permuted-null infra, crystallizer, etc.

Key framings introduced: emergence = interlocking affordances (configuration, not membership); universal permuted-null discipline as single gatekeeper; four epistemic verdicts (understand / caught-but-unsaid / proven-nothing / can't-see-from-here — matches the two-shadow-kinds idea in [[isaac-unsupervised-invariant-discovery]]).

Leading suspects carried in: membership-only composition (explains "assembles but never behaves differently"), representation-variance of doors (deepest untested assumption), Fisher-ratio still in ranking paths.

**Where the audit targets live:** dims/box-range work = `code/neural_transplant/range_classifier/` v2+v3 (METHODS.md in each) + `decode_boxes.py`; authoritative engine = `code/isaac.py` (per [[isaac-project-state]]); Downloads\New folder (3) confirmed backup-only (MOVED_TO_DOCUMENTS.txt).

**Open design tension flagged for the doors audit (2.2):** the standard assumes box-range doors, but [[box-to-matrix-translation]] already found log-likelihood matmul (0.922) beats the numpy box (0.900) — the doors audit must decide box-geometry vs observed-distribution+matmul as the door representation, not assume boxes.
