---
name: comparison-as-registration
description: "The researcher's theory of comparison/learning as registration (nulling), not subtraction"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3a7d1589-8553-435a-a6a5-a4d70af922f1
---

The deepest output of the 2026-06-22 session (researcher's framing, sharpened together). **Comparison is REGISTRATION, not subtraction.** You slide/scale/rotate one signal onto another until they coincide where you CHOOSE, then read two outputs: (1) the transform applied = the *relationship* (scale/shift/depth); (2) the residual that won't line up = the genuine *difference*. The match is the instrument; difference is read off it.

- Matching gives FINER differentiation than measuring because it's the **null method / hyperacuity** (vernier acuity, interferometers, coincidence rangefinders, moiré, Wheatstone bridge): at coincidence, sensitivity is maximal and common-mode self-cancels. (Carriers/strip-DC/"subtract the shared" are a *consequence* of this, not the principle — do NOT restate the lesson as mere subtraction; that framing was explicitly rejected.)
- The alignment is a CHOICE that selects the question (which difference is visible, at what resolution — the sig-fig example).
- The residual is a FIELD not a scalar; its shape names the transform (radial growth=scaling/balloon; viewpoint shift=parallax=DEPTH; stereo disparity = this theory in one organ).
- Same and different are ONE operation: register, then read. "How different is this same thing" = residual after matching; "how same is this different thing" = how small a transform registers them.

**For LEARNING:** a concept IS a chosen registration. Learning = finding the registration that nulls what you don't care about and maximizes sensitivity to what you do — learn *where to make things coincide*, not "the features." Ties to Isaac's first-class "doesn't-matter" value (the load-bearing one).

**EMPIRICAL CONFIRMATION (2026-06-23, real data):** frozen ResNet18 embeddings on CIFAR-10 — box crystal on raw embedding 0.71 vs linear probe 0.84 (the axis-vs-oblique gap); a ROTATION LENS (LDA) closes the ENTIRE gap → crystal 0.834 ≈ linear 0.839. The cheap box reader MATCHES the linear head once you ALIGN first. Registration IS the lever, proven. Corollary: variants hurt after alignment — good alignment makes the simplest reader win. (`neural_transplant/vision_lens.py`.) This is the strongest evidence for "find the format, the cheap reader does the rest."

**Bridge to code:** the box already does a baby version (median=coincidence, in-range count=null, median-distance=residual). The upgrade: a comparison primitive that ESTIMATES the transform (shift/scale/rotation), not just the residual = analysis-by-synthesis ("align stored model to input; residual pose IS recognition"). This unifies Thread A's scale/rotation wall and Thread B's box-hostility: both are a MISSING REGISTRATION step. See [[nn-transplant-experiments]], [[isaac-project-state]]. Full session record: `Documents/isaac_project/SESSION_HANDOFF_2026-06-22.md`.
