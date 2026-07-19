---
name: generation-not-duplication
description: "OWNER CORRECTION 2026-07-12 (FizzBuzz): learning-from-examples = duplication/mimicry, NOT the goal; the capability is understanding TOLD rules and generating from them; never decompose a task for Isaac"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e753bbbc-d082-492d-a864-7a16681b2792
---

Owner, 2026-07-12, after I presented example-trained FizzBuzz as "Isaac
learned it": **"he didnt learn it. you fed him a pattern and he had to
mimic it. thats not generation, thats duplication. thats not what we
are doing here. what i want is to say if its a 3 say fizz... i want
him to be able to understand that kind of thing."**

**Why:** the mission is understanding, not statistics-matching. Fitting
observed outputs (even null-gated, even 100% held-out) is duplication.
The capability that counts: a rule TOLD in vocabulary form → Isaac
builds the executable understanding → GENERATES behavior having seen
zero output examples. Same family as the speech correction
([[omega-vision]]: template speech "is called programming") and the
usage law on the sheet.

**How to apply:** (1) when the owner says "test whether Isaac can do
X", the test is told-goal → his-method → generation, never
fit-to-examples; (2) NEVER decompose a task into sub-targets for him
(my one-vs-rest indicator framing was programming the lesson —
wrong-kept in fizzbuzz_probe.py); (3) example-fitting stays only as
the DUEL PARTNER / fallback-when-untold (told-knowledge law: belief
from data). Built same day: tell_rule / generate_by_rule /
validate_rule + task-blind learn_responses (rule_battery 11/11,
task_battery 8/8). Companion owner law, settled in three steps the
same day: TAUGHT ROUNDING — "3.0018463 is probably tested to 3;
1.764964 may be 1.75" — a measured constant's roundings (ruler marks
{1,½,¼}×10^k, coarsest first) are tested outright at FIT END with
the trial refit as referee; simplest non-losing mark wins, else the
measured digits stand. STRICTLY POST-HOC (proposal-time rounding
measured wrong — weak referee smears; rounding_battery 7/7). Both on
[[design-intent-sheet]].
