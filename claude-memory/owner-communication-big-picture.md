---
name: owner-communication-big-picture
description: "OWNER CORRECTION 2026-07-15 — he directs at the idea level; ALL docs/code are commissioned (assistant-authored), he doesn't know internals; report big-picture in plain language, mechanisms only as analogies"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bcf72f7c-b5e8-4d25-a62b-2e2fc74b0cfb
---

**Owner, 2026-07-15:** "can you simplify it again. we need to be clear.
if its a doc or code, i didnt write it. i asked for it. i dont
understand how the systems work internally, just big picture."
(Second strike — 2026-07-13 was the same wire: "you are using words
for things i know in ways that i dont understand.")

**THIRD STRIKE, same day (test reporting):** "you are running these
tests, i dont actually know what these tests are doing or finding or
how they work or the datasets are doing or what they should be doing
or look like or what we expect. i have no idea what it failed on the
typos because i dont know what that means." Lesson: NEVER report a
probe/bench result without first saying, in one or two plain
sentences, WHAT the test does (what we planted, what a pass looks
like) — and watch loaded words: "typo" made him think spelling when
the test was about mis-entered NUMBERS. A word that means something
specific to him will be read that way.

**The facts to hold:** every document and every line of code in this
project was COMMISSIONED by the owner and AUTHORED by assistant
sessions. The designs, laws, and direction are genuinely his; the
implementations and their internal vocabulary are not. Never assume he
remembers or knows a doc's/probe's internals, world-labels (W1, A3),
metric names (r², RMS, partial correlation), or file mechanics.

**Why:** he is the vision-and-judgment holder ([[isaac-working-style]]);
jargon walls force him to ask for translation, which costs the exact
trust and momentum reports exist to build.

**How to apply:** lead every report with what-happened-in-plain-words,
as to a sharp executive, not an engineer. Mechanisms only as analogies
(tape-measure, judge, receipt). Complete numbers still mandatory
([[report-plain-accuracy-numbers]]) but say what each number means in
the sentence that carries it. Internal labels (W-numbers, organ names,
flag classes) stay in the docs; translate them at the chat surface.
When he asks a technical question, answer at the level of WHAT it does
and WHY it matters, and offer depth rather than defaulting to it.

**THE WRITEUP LAW (owner, 2026-07-15 night, now on the sheet):**
"we need to make sure that we are doing thorough writeups and post
evals. i want to know what is happening in the code, what is being
found, what the structures look like, this is where we get into the
research... what is being built and structured that i missed, how is
it being represented, and how well does it perform or break."
**Why:** verdict counts alone bury the research; depth is wanted, not
just brevity — the earlier strikes were about JARGON, not about
detail. **How to apply:** every build/eval campaign ends with a
RESEARCH WRITEUP doc (plain language, labels translated): (1) what
was built, (2) what the structures LOOK like — show the shape, a
sketched table / example row / the actual equation, (3) how it is
represented + its receipts, (4) what was found with complete numbers,
(5) how it performs and where it breaks, with failure MECHANISMS
explained. First instance:
`dc/docs/RESEARCH_WRITEUP_2026-07-15_POOLS_AND_VERDICT.md`.
