---
name: provenance-audit-2026-07-18
description: "Research campaign day 1 — 65-agent trained-not-programmed audit of dc; verdict TRAINED with 1 confirmed violation (engineer.py:391), wall inversion, FURRY claim corrected, enforcement gaps named"
metadata: 
  node_type: memory
  type: project
  originSessionId: 36208d96-b244-496c-999f-961eb7bebe5b
---

**THE TRAINED-NOT-PROGRAMMED AUDIT (2026-07-18 evening, research
campaign day 1).** Owner asked: is Isaac actually trained, or
programmed? 65-agent workflow (wf_70c47b1a-b01): 6 engine scanners
(all 11,250 lines of isaac.py + isaac_store), feed inventory,
read-only mind dump (scratchpad COPY; isaac_home untouched),
battery/ablation check, 10 flagship traces, 2-refuter adversarial
verify, completeness critic. Writeup filed BOTH repos:
`docs/RESEARCH_WRITEUP_2026-07-18_TRAINED_NOT_PROGRAMMED.md`.

**VERDICT: TRAINED.** 8/10 traces trained with receipts (Kepler,
Boyle 1662, Galileo, CO2, sunspots 10.4534, self-built word,
mechanical k/e, planets); curriculum MIXED (tube OD=ID+2·wall told
AND hard-coded in tube_court — duplicate ownership); **FURRY =
PROGRAMMED** (probe-only, throwaway mind, never fed live — the
handoff claim needs an asterisk). Engine organs clean of all law
content; fitted non-round coefficients + never-fed holdouts =
signature of training.

**THE EXCEPTIONS:**
1. **CONFIRMED VIOLATION** `isaac_store/engineer.py:391` —
   read_goal_sheet subtracts literal `{'alive','score','dir','food',
   'energy'}` (snake exam vocabulary); pure dead-data-flow yields
   ['alive','lucky','score'], the patch makes it ['lucky'] = gate
   N8's expected answer. Two refuters both EXECUTED it. Exam-only
   callers today (nothing reached his mind). Fix: derive exclusions
   from sheet's own classifications; make N8 expect honest output.
2. **WALL INVERSION**: promote wall (counted 55 gates, handoff says
   56) permanently re-certifies HAND courts (N1-N4, N8) while
   engineer_transplant_probe (the honest ablation, 8/8) is one-shot
   off-wall; its generic solver never promoted.
3. **ENFORCEMENT GAPS** (critic): who= is caller-supplied free text
   (provenance = convention); teach() has no who (311 facts
   source-less); teach_not stamps NO container (10 negatives);
   **405/843 nodes = speech, all unstamped — biggest unaudited
   class**; journal unsigned; mind.isaac = raw pickle loaded before
   validation (ACE surface); nothing in code guards isaac_home;
   exact-1.5 snapped with no pre-snap receipt; drafting container
   has no world: node; 3/9 discovered laws lack evidence breakdown.
4. **REAL BUG**: ledger road drops powerprod exps — life rebuilt
   from ledger re-arms grown words broken (KeyError in
   _augment_with). Pack/pickle roads fine.

**CEILING MAP**: 27 gray findings, one shape — growth mints
INSTANCES never OPERATORS (atom kinds, op menu, powerprod grid,
telling grammar a strict subset, tell_rule = multiple_of only).
Ceilings refuse loudly (good). Matches declared usage-law boundary;
vocabulary elections is where they start moving net-side.

**QUEUED NEXT** (owner to pick): fix #1 + wall the transplant probe;
speech-corpus audit block; stamp red-team (fake who="discovered"
then engine-side stamping at intake — ties to owner's top open
item); ledger seam fix + battery; pre-snap receipts; fresh-mind
re-feed reproduction. Full result JSON in session scratchpad
`audit_result.json`. Related: [[engineer-lane]], [[facts-layer]],
[[growing-grammar]].
