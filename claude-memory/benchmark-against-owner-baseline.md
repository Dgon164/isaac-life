---
name: benchmark-against-owner-baseline
description: "FEEDBACK 2026-07-11 — architecture experiments are graded against the owner's existing single-core ~3-second trainer, not against internal torch baselines; beating a same-width MLP counts for nothing"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4ad6cda5-802d-4837-87cf-3fead5c6e793
---

After the veto-net head-to-head (see [[veto-nets-headtohead]]) the owner
explained why it was a failure even though its internal comparisons were
clean: he already has a thing that trains in ~3 seconds on ONE CPU core
with better results than the veto net achieved on a 3090 — and he
considers even THAT result poor, because 99%+ nets (convnets) exist.

**Why:** the mission ([[lost-einsteins-mission]]) is cheap/explainable/
Raspberry-Pi AI. A new architecture that needs a GPU to lose to a CPU
incumbent is a failure on every axis at once; "fair matched-width torch
baseline" is the wrong opponent.

**How to apply:** any performance/efficiency head-to-head must include
the owner's own current engine as contender #1, run under a hard compute
budget (his bar: ~seconds, one core, no GPU), and be graded as
accuracy-per-compute against that incumbent. Success = beat what he
already has under his constraints; anything else is a negative result
no matter what it beats internally. (Exact baseline number/engine for
the 3-second bar not yet pinned in the ledger — ask and record it when
the next benchmark is built.)
