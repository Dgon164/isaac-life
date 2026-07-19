---
name: no-neural-nets-as-deliverable
description: Hard rule — never build/train a neural net as "the answer"; the deliverable is an explicit mathematical equation
metadata:
  type: feedback
---

**The deliverable is NEVER a neural network.** This project rejects trained nets as
*result-tables* (a tabulation of a function's outputs), not the *mechanism* (the rule).
A ReLU/backprop net reaching high accuracy is the TRAP the handoffs warn about — it
memorizes the decision surface instead of extracting the governing equation.

**What "an equation" means here:** an explicit algebraic expression —
`S(x) = c₀ + Σ cᵢ·tᵢ(x)`, threshold `S>θ` — where the `tᵢ` are REAL math terms
(products xᵢxⱼ, invariant forms like cosh(Δη)−cos(Δφ), conservation residuals, recovered
invariants/states) and the `cᵢ` are fit by **linear / least-squares / L1** methods. No
hidden layers, no ReLU, no sigmoid-stack, no backprop. Readable as algebra; run once.

**Why:** [[isaac-unsupervised-invariant-discovery]] — the whole point is mechanism over
result-table, governing equations over approximated surfaces. An honest equation will
score BELOW a net (e.g. ~0.75–0.82 vs a net's 0.88 on HIGGS); that gap IS the thesis,
not a failure. The integrity rule: only the his-way/equation machinery makes the decision.

**How to apply:** when the user asks for "the equation" or "one thing you run once that
says X", build an explicit-interaction-term model fit by linear/sparse regression — NOT
an MLP/deep net. The 2026-06-28 drift (trained a 448k-param ReLU net to hit HIGGS AUC
0.881 while chasing "the number") was exactly the wrong object; the user was rightly
angry: "this isn't a neural net, we were never working on a neural net." Treat any net
only as a throwaway reference ceiling, never as the answer.
