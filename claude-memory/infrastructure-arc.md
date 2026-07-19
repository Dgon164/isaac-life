---
name: infrastructure-arc
description: "2026-07-11 owner-declared major shift — persistence v2, package split, partial net loading, batch, API, ops; plan at isaac_project/INFRASTRUCTURE_ARC_2026-07-11.md; recorded on the design sheet"
metadata: 
  node_type: memory
  type: project
  originSessionId: 14c3dbd4-de8f-411d-802a-983f901ba24a
---

**Owner, 2026-07-11:** "time for a major shift" — the six areas:
persistence, structure processing, batch processing, API calls,
system/operational management, partial net loading for responses and
processing.

**NOMENCLATURE (owner, official): PRIME** = Isaac, the full net
(formerly "core"); **ORCHESTRATOR** = Prime's sole writer; **WORKERS**
(leaf worker = all-in-one Isaac + security net); **SCRUBBERS** =
first-class role on every Prime intake; **CLIENT SIDE** = customer/
user side. **THE IDENTITY LAW (owner):** Isaac understands the world
but never identifies people/businesses; Prime = concepts+laws, no
identity dossiers; public info processable; user-submitted = reserved
client-side + scrubbed; **no datasets, no user info, no usage
patterns to Prime — telemetry included; all personalization localized
user-side.**

**Owner's architecture (same day, second message): THE ORCHESTRATOR** —
one orchestrator owns the mind as SOLE WRITER; workers (discover jobs,
perception/recognition, consolidation, API front-ends) process on read
snapshots ("live pulls as needed") and route all updates through the
orchestrator as QUEUED edits. Agreed framing: the queue IS the
admission gate made operational (workers expand, orchestrator
compresses by test); rejected edits wrong-kept; conflicts → existing
organs (count merges, RIVALS, supersession); orchestrator stays THIN
(gatekeeper not thinker).

**HARD CONSTRAINT (owner, same day): NO traditional databases** — he's
had major SQLite scaling problems, averse to any DB. Storage = plain
files, stdlib only: JSONL journal + IMMUTABLE indexed pack snapshots
(`mind.v<N>.isaacpack`: header | node→offset index | records; load
index only, seek/mmap records on demand = partial loading;
atomic-rename publish; new snapshot supersedes, old kept). Immutability
= live pulls with zero locking. Never re-propose SQLite/Postgres/etc.

**Round two (owner, same day):** (1) **CUSTOMER SUBNETS never feed back
to Isaac** — containerized deployments: core pack read-only + customer
overlay (own journal/packs/orchestrator); isolation STRUCTURAL (core
queue unreachable), sync one-way core→customer, pinned upgrades; PII
lives only in the overlay; = fork() made persistent. **Share path
(owner): customer opt-in** — overlay discovery → core orchestrator
evaluates → SCRUBBER WORKER strips identifiable info, keeps general
abstraction only → normal admission; quarantine intake, raw not
retained core-side, scrubber refuses when it can't separate cleanly;
share off = no path. (2) **Worker
caching**: live-load anything, cache locally; **recheck SETTLED BY
OWNER: FIXED 30 min** ("it would be the worker doing the updating, not
the net" — don't re-pitch the adaptive/heartbeat design; it's filed as
superseded rival, revisit only if measured staleness cost bites);
recheck = journal-tail delta past a watermark; companions undisputed:
pin one version per job, admission catches stale proposals. (2b) **SECURITY NETS (owner, "GREAT
IDEA", same day)**: user-side nets one tier BELOW customer subnets —
processed/learned/output by Isaac but pullable ONLY from the worker;
worker = its own mini-orchestrator = "the older all-in-one Isaac" at
the leaf; three-tier recursion core→customer→worker, one mechanism;
reads layer one-way local-wins; NO upstream channel (not even the
share path); ephemeral (RAM-only) vs user-held (encrypted, key
user-side) modes; **logging is a leak channel** (ops events =
counts/timing only). (3) **Working nets**: full net will
be BIG; keep working nets small-but-capable — demand paging + working-
set extraction (task closure × measured usage), information_ledger
states kept-vs-left-behind in complete numbers. Plan has Phase 7
(subnets/containers) + batteries.

**Plan doc:** `isaac_project/INFRASTRUCTURE_ARC_2026-07-11.md` (phases +
batteries + orchestrator diagram).

**BUILD STATE 2026-07-11 (2nd pass): WIRED INTO ENGINE, battery 29/29,
suite 11/11.** ONE home: `isaac-paperclip/isaac_store/` (project copy
deleted). Engine has `save_pack()/Isaac.load_pack()` beside pickle;
manual updated both copies same step. SCALE MEASURED (scale_test.py,
synthetic 100k nodes/500k doors): pack 141.5 MB vs pickle 27.1 (5.2×),
save 10.1 s vs 0.5, full load 5.3 s vs 0.4, single-node fetch 0.04 ms =
133,000× faster than full load (index open 28 ms) — partial loading
vindicated; size/save-time = measured limit, lever = per-record
compression (not yet). codec module-alias: minds saved under __main__
decode where engine imports as 'isaac' (register_module as_name).
**LiveCache BUILT (2026-07-11, "whats next" turn): 13/13** —
isaac_store/cache.py + test_cache.py; 30-min fixed recheck (delta via
journal tail, only touched keys invalidated, adopts new packs),
job-pinning context (overdue recheck waits for job boundary), H6
proves stale proposal rejected + wrong-kept at gate. Store battery
still 29/29. Manual updated both copies. NEXT: the leaf worker
(security-net all-in-one Isaac with layered reads local∪client∪Prime),
then API phase.
**LeafIsaac BUILT ("lets go" turn): 13/13** — isaac_store/leaf.py +
test_leaf.py; layered pull local∪client∪Prime with graft+origin tags,
local-wins meta; ephemeral (save refuses) vs user-held (resumes);
QUARANTINE PROOF = planted-secret byte-scan of all upstream files →
zero hits; no submit path by construction. teach() gotcha: facts live
verbatim in fact_index, doors are between TOKENS (first battery draft
asserted wrong organ). Encryption-at-rest for user-held = open item
(needs vetted crypto lib, owner's call). All three batteries green:
store 29/29, cache 13/13, leaf 13/13.
**PrimeServer BUILT (2026-07-12, owner delegated "know nothing about
this part"): 17/17** — isaac_store/server.py + test_server.py; the
orchestrator over HTTP (watermark/journal-delta/record GET;
submit/compact POST); refusals = HTTP 200 ok:false + why; 400/401
clean JSON only; binds 127.0.0.1 default, optional bearer token
(REQUIRED before any non-localhost bind); access log = method+path
only (Identity Law on logging); wire format = codec JSON. ALL FOUR
batteries green: store 29 + cache 13 + leaf 13 + server 17 = 72/72.
NEXT: point LiveCache/LeafIsaac at HTTP endpoints as alternative to
file access (remote workers); Scrubber role as a worker; then ops
ledger phase.
**RESEARCH-AND-LIVE MODEL (owner final, 2026-07-12): paperclip =
research (ALL development), `Documents/dc/` = LIVE mirror of
everything ("duplicate anything and everything into dc"), private
github.com/Dgon164/dc.** The anti-divergence rule: dc is NEVER
hand-edited — research promotes via **`dc/promote.py`** (copies whole
research tree minus .git/data/caches; preserves dc-only README/
promote.py/PROVENANCE.md/.gitignore; runs ALL gates — engine 11/11 +
4 batteries 72/72 — FROM dc; refuses on any failure; stamps
PROVENANCE.md with source commit). First promotion: research @
f99cc22 → dc 9f05e29, pushed. Both repos self-contained (isaac_store
lives in BOTH via promotion; engine/store find each other same-repo
first, ISAAC_ENGINE/ISAAC_DC/sibling fallbacks). dc git identity set
locally (jtwee / jtweeks12@gmail.com); gh authed as Dgon164.
**SCRUBBER BUILT (2026-07-12): 19/19** — isaac_store/scrubber.py:
scrub(payload, deny_list) strips email/ssn/phone/card/ip/address/
honorific-names → category placeholders, abstraction byte-identical,
report = counts never content, REFUSES identity-in-keys
(load-bearing); identity_gate(inner) = Prime admission backstop
(judges, never cleans). ALL FIVE OWNER ROLES NOW BUILT. Promotion
gates include scrubber: engine 11/11 + 5 batteries = 91/91. Second
promotion: research fddb2df → dc 9dffb04, pushed. Remaining
unbuilt from plan: batch phase (grade vs 3s baseline), ops ledger,
package split (Phase 2), remote workers over HTTP, working-set
extraction, user-held encryption (awaiting dependency call).
**LEARNED SCRUBBER = owner TODO (2026-07-12, "its own research
soon", NOT now):** train the scrubber — learn personal/not-personal +
GENERALIZE content; usage law applied to privacy; on the design
sheet. **LEARNING BATTERY 9/9 (test_learning.py)**: leaf discovers
law from private data → dirty share refused → scrubbed share
admitted byte-exact → different worker pulls ONE record cold →
applies law corr 1.000000; byte-scan zero private bytes in Prime.
**Battery-found fix**: rejected edits were journaled VERBATIM (PII
into Prime via wrong-kept!) — orchestrator now redacts value on
Identity Law refusals (judgment kept, content not). 7 promote gates
= 100/100. Third promotion: research 3c090ed → dc ee00e4c, pushed.
**SKILLS = THE WORKER MODEL (owner, 2026-07-12): roles are loadouts,
not species** — every worker IS Prime + a checkbox of skills; skill =
plain record `skill:<name>` (learned things + preloaded structures)
published via normal queue, pulled like any node (same cache/recheck/
pinning/HTTP). Scrubber refactored: module patterns = SEED only
(`seed_skill()`); `scrub(vocabulary=<pulled record>)` runs Prime's
living vocabulary; educating Prime re-equips workers at recheck
(battery K2 proves pinned jobs keep old loadout to boundary).
test_skills.py 7/7; 8 promote gates = 107/107. Fourth promotion:
research d1129f0 → dc b5d3734, pushed. (Also repaired: sheet's
WORKING NETS header had been eaten by an earlier edit.)
**ALPHA LIVE (owner, 2026-07-12): "this is the alpha live"** — dc IS
the alpha; no research pushes today (and stop mentioning the unpushed
paperclip state to him). **OPS BUILT 13/13**: OpsLedger content-free
by construction (refuses long strings/objects at write); orchestrator
+ server self-report counts/ms; leak-channel proof (PII via HTTP → 0
bytes in ops/journal); **`alpha.py` at repo root = the launcher**
(`python alpha.py` boots Prime service: identity gate + doorway +
ops, seeds scrubber skill first boot, resumes on restart, refuses
non-localhost bind w/o token). Bug fixed: PrimeServer.stop() hung if
never started. 9 promote gates = 120/120. Fifth promotion: research
23a0c93 → dc d94bf55, pushed. Owner's six areas: ALL BUILT except
batch processing (grade vs 3s baseline when done).
**MULTICORE BUILT (owner ask, 2026-07-12): 7/7, MEASURED 2.90×** —
`worker.py` (repo root) = Worker as separate OS process: pulls jobs
from Prime's doorway, claims via "expect" (optimistic concurrency now
NATIVE in orchestrator.process — queue order arbitrates, losers
wrong-kept), computes on own core, submits results via _encoded codec
envelope. 8 discover-jobs: 10.1s (1 worker) → 3.5s (4 workers), all
4 participated, 8/8 laws exact, 0 double-claims. Bug fixed:
/api/submit validated before decoding _encoded (400'd every
numpy-bearing submit); also PrimeServer.stop() hung if never started.
Write path stays single-writer BY DESIGN (edits are ms; compute fans
out). 10 promote gates. Sixth promotion: research 8744bee → dc
06f3b40, pushed. ALL SIX owner areas now built (batch = the worker
fleet; the 3s-baseline head-to-head remains open as a benchmark).
**REAL-DATA FLEET RUN (2026-07-12, "lets do it"):** worker.py gained
`discover_file` jobs (mmap real .npy, job's columns);
`experiments/fleet_higgs.py` = 10 jobs / 4 worker processes / 5000
rows each on real HIGGS: **m_lv PARTIAL r²=0.891 — transverse-mass
form found (lep_pT² + cos(lep_φ−MET_φ) terms)**; m_bb 0.608 / m_wbb
0.493 / m_wwbb 0.421 PARTIAL (pT-pair × cos Δφ structure); m_jj/m_jjj
honest NO RULE (sqrt-of-composite outside vocabulary — next-lever:
sqrt/square-root op or y² framing); ALL 3 controls correctly refused.
Wall 55.1s, busy 175.5s = 3.18× utilization. Report + Prime artifact
in experiments/runs/2026-07-12/. Seventh promotion: research e08dd49
→ dc 369049c, pushed.
**FRAME DUEL (2026-07-12, "lets give it a shot"): y² frame LOST —
wrong-kept.** Hypothesis (sqrt-of-composite blocks m_jj → discover
y²) REFUTED by battery: m_jj/m_jjj NO RULE in BOTH frames; on sayable
masses y² loses held-out original-space everywhere (m_lv 0.904-vs-
0.855, m_bb 0.665-vs-0.545, m_wbb 0.495-vs-0.309, m_wwbb
0.391-vs-0.331). WHY: true m_jj² needs cosh/cos of angle DIFFERENCES
at frequency EXACTLY 1 — **DIAGNOSIS OVERTURNED same day
(mjj_identity_probe, wrong-kept): the engine ALREADY brackets+refines
(grid proposes, hill-climb sharpens) and says planted invariant-mass
physics EXACTLY (y² UNDERSTOOD r²=0.9996, refine 1.5→1.026≈1). Real
m_jj is a MISSING-VARIABLE SHADOW: textbook formula itself maxes corr
0.2358 on stored HIGGS columns (per-column standardization; mass from
4-vector info absent from features) — NO RULE was CORRECT. Owner law
recorded on sheet: NO PRESET FREQUENCIES (bracket+refine, deviation
slower when closer) = standing principle; mechanism verified
present.**
m_lv improved to UNDERSTOOD held-out 0.904. Frame-duel harness kept
(worker "frame" param + held-out orig-space judging =
fleet_higgs_frames.py). Eighth promotion: 3757d4d → dc f095d67.
**TOLD KNOWLEDGE (owner design, 2026-07-12): 13/13, IN ENGINE** —
`tell_law(name, equation, d=)`: canonical-vocabulary parser (refuses
loudly outside grammar; round-trips Isaac's own printed equations);
match check → same-form = WITNESS on existing law (no duplicate
node); new form = TOLD-UNVERIFIED (apply works NOW, law_confidence
None until data — belief measured never told);
`supersession_duel(name, X, y)` = told vs fresh discovery, held-out
quarter: CONFIRMED earns ranges+edge-r² (confidence starts working),
SUPERSEDED keeps defeat with why+numbers (told Kepler confirmed
0.9996; told T=a² crushed −38.9 vs 0.9996 and replaced); retention
proven via ordinary packs. Battery
experiments/told_knowledge_battery.py; 11 promote gates now. Ninth
promotion: 64cca7f → dc 2afdb66, pushed.
**LAW FAMILIES + which_law (owner's Earth/Jupiter/Pluto question,
2026-07-12): 13/13, IN ENGINE.** His question caught a REAL GAP:
form-only match check would have filed Jupiter's gravity as a
witness of Earth's (smushing). Fixed: constants compared on form
match (5% rel) — same = witness, different = VARIANT doored under
`lawform:<crc>` family parent (hierarchy law applied to laws).
`which_law(X,y)` = rank+veto+abstention over candidate laws: Earth
data→earth 0.9998, Jupiter→jupiter, Pluto-unknown→NONE new-variant
candidate (abstains) then names it after telling, MIXED
Earth+Jupiter→refuses single answer (0.40/0.38), split-by-context
resolves. Waves/circles machinery confirmed still present (suite
11/11 + _wave_circles). Battery gravity_family_battery.py; 12
promote gates. Tenth promotion: 61b387e → dc acf806a, pushed.
**OWNER 2026-07-12: "those containers are going to be what is
required for user application"** — the tier architecture (Prime →
client overlay → leaf security net) is THE substrate for anything
user-facing. User-app readiness gaps when that work starts: actual
container packaging (Docker image = engine + core pack read-only +
overlay volume, designed Phase 7 not built), user-held encryption
(vetted lib, owner's dependency call pending), remote workers over
HTTP (LiveCache/leaf still read Prime's files directly — fine
same-machine).
**THE PROVENANCE GATE (owner design, 2026-07-12): 13/13, IN LEAF** —
"reconstructable exclusively from isaac source nodes = game;
requires any user nodes = banned" + follow-up "see if it can
recreate the information from public sources too". Built: node
source tiers (prime/client/user/public), FAIL-CLOSED (unknown=user);
leaf.exportable (closure ⊆ {prime,public} = game; banned from EXPORT
never from USE); share_candidate = first defense BEFORE scrubber
(defense order: provenance gate → scrubber → identity_gate);
recreation_check = active rebuild attempt from prime/public sources
(form+constants match ⇒ user data unnecessary ⇒ upgrade + unlock;
user-told Kepler upgraded via Prime's public record, custom law
stayed banned); literal reconstruction proven (prime-only leaf
rebuilds identical law). Battery isaac_store/test_provenance.py; 13
promote gates. Eleventh promotion: 5b61b95 → dc 73dddd9, pushed.
**THE SEEKER (owner design, 2026-07-12): 11/11, BUILT** — "acts like
a search agent... few sources, chews, best answer". One-question
lifetime (no-curiosity intact: task from outside, no task queue,
cannot self-task); DEPTH ZERO (bait battery: 20 links/page planted,
0 followed); physical budgets (bytes/sources/time in task; clean
stop proven); chew v1 = numeric cross-source corroboration (2%
clusters, ANSWER needs ≥2 sources + majority, else AMBIGUOUS/NONE
refusal with dossier, dissent always shown); receipts url+sha;
public-tier provenance → gate-ready. Search provider PLUGGABLE —
**real-web backend = owner dependency call still open** (API key vs
none); batteries use local mock web. isaac_store/seeker.py +
test_seeker.py; 14 promote gates. Twelfth promotion: 299f027 → dc
2478404, pushed.
**ACCOUNT MODEL (owner, 2026-07-12, on sheet):** account id + hourly-
rotating session keys (grace overlap), one auth path GUI+API, GUI on
website via AWS (TLS at proxy; PrimeServer stays localhost-bound),
concurrent (container fleet) + local (user-held leaf) processing,
**STORAGE-BASED TIERS (1 GB base, 5 next, ...) + 1 worker per
level**; upload caps at the door (Content-Length pre-read); pbkdf2
stdlib for passwords; account PII in ONE ops-side store no net
reaches. Not built yet; tier table/prices = owner's.
**RESTORE-POINT CACHE (owner, 2026-07-12): 10/10 BUILT** — default =
3 supersession layers (newest 3 packs + spanning journal tail,
trimmed), option full log (retention_keep=None); restore(v) = rewind
as APPENDED journal event (cold-start replays through it); measured
224 KB vs 378 KB. **TWO gate catches during shipping:** (1) I pushed
dc DESPITE a REFUSED promotion (chained push after promote
unconditionally — NEVER chain push on promote; gate exit code must
gate the push); (2) the refusal exposed a REAL bug: trimming ALL
journal events reset the seq counter → post-trim events reused seqs
≤ pack watermark → cold-start silently skipped them; fix = trim
never empties (keeps final event: baked into snapshot, never
replays, preserves numbering). Clean stamp: research e0d7bba → dc
eea9ea2, pushed. 15 promote gates.
**THE HONEST REPORT BUILT (owner refocus 2026-07-12: "worried about
isaac and how people will use him"): 11/11** — the 07-04 MVP is
real: `python askisaac.py data.csv [--target col]` → verdict-first
report, equation IN USER'S COLUMN NAMES ("energy = +3.00*alpha*beta
+1.00*alpha*alpha"), r²+edge+rows, calibrated confidence w/ note,
rivals+probes, next-experiment, provenance appendix (data sha
stable); noise → NO RULE refusal report with diagnosis.
isaac_store/report.py (load_csv/challenge/render_text) + askisaac.py
+ test_report.py. 16 promote gates. Promotion: 2c66ec7 → dc b944c84,
pushed (gate BEFORE push, stepwise). NEXT for usage: web page on the
alpha serving this report (UI plots), then the account layer when
owner returns to business.
**TRANSLATION LAYER = TODO (owner, 2026-07-12):** report ≠ response;
a translation layer between the internal honest report and the
user-facing reply. Two roads (Omega-consistent): LLM as
MOUTH-WITH-FAITHFULNESS-NULL ONLY (rephrases, never originates/
alters verdicts/numbers/equations; mismatch → fall back to raw
report) OR native gated English (extend interrogate()'s
gated-English road; pairs with learned-scrubber research). Report
stays attached as ground truth under every response. On the sheet.
**NATIVE GATED ENGLISH — road 2 v1 BUILT (owner: "take a crack at
number 2"): 20/20** — isaac_store/speech.py: speak(report) REALIZES
structure as speech (no LLM, no net): verdict framing first
("I understand this data" / "I could not find... and I will not
pretend to"), terms spoken from the MODEL dict in user's column
names ("mainly, alpha times beta raises it (weight 3.00); also, the
square of alpha..."), atom vocabulary (wave/logarithm/square/root/
decay/alignment/gap), squares collapsed (a*a → "the square of a"),
complete numbers, gated omission (missing field = never spoken).
FAITHFULNESS: by construction + verify_faithful null (every spoken
number must exist in report; tampering caught; counts avoided in
phrasing since they're not report values). askisaac --speak =
response + report beneath. Road 1 (LLM mouth) = fallback if native
hits ceiling. report.py now exports rep["terms"]/["intercept"]
(plain-data model). 17 promote gates. Promotion: 774298d → dc
078baa0, pushed (gate before push).
**OWNER CORRECTION (2026-07-12): "its all or nothing. you dont get
to choose. that is called programming and thats not what isaac is
about"** — the template speech realizer was the usage-law trap
(hand-wired wording); DEMOTED to scaffold, wrong-kept. **LEARNED
SPEECH BUILT: 20/20** — speech_learn.py: wording learned from paired
examples (speech_corpus.txt = teacher's data,
"features|sentence-with-PLACEHOLDERS"); fragments admitted per
feature only past a permutation null (placeholder-only fragments
inadmissible); stored IN THE NET (speech:<feature> meta → persists,
supersedable). ALL OR NOTHING: untaught atom = silence + listed;
untaught verdict = cannot speak → raw report. PROOF STANDARD (use
for any future "learned X" claim): grep proof (wording absent from
code — a code COMMENT got caught), corpus swap changes speech,
withheld lesson = unspeakable, retention across packs, faithfulness
null. askisaac --speak = learned only. 18 promote gates. Promotion:
8763c25 → dc 385751d, pushed.
**LOCAL AI CONVERSATIONS = TODO, FOR LEARNING/TRAINING (owner
corrected 2026-07-12 — "not quite my tempo. i meant for learning
and training"; do NOT re-pitch as product mouth):** small LOCAL
model (1.5B–7B) = Isaac's SPARRING PARTNER — World GM for language:
endless local conversation environment; model output = untrusted
DATA to null-gate, never truth. Uses: grow speech corpus from
conversation (fragments still permutation-null admitted);
adversarial PII text for learned-scrubber training; usage-
regularity practice. Budgeted sessions (GM pattern). Runtime/model
choice = open dependency call. On the sheet.
**THE FACE BUILT (2026-07-12): 7/7** — `python face.py` →
127.0.0.1:8676: browser page, drop/paste CSV → learned speech +
honest report; separate process from PrimeServer (heavy discover
never blocks the doorway); door laws: 20MB cap pre-read (413),
clean 400s, refusals = 200 spoken answers, content-free log.
19 promote gates. Promotion: bcef656 → dc 648921f, pushed. **The
usage stack is complete for a local person: face.py (browser) /
askisaac.py (CLI, --speak/--json) / alpha.py (service) /
worker.py (fleet).** Remaining next-ups: remote workers over HTTP,
docker packaging + accounts (owner does business side), search
provider + crypto + local-training-model dependency calls (owner),
learned scrubber + speech-corpus growth (research threads).
**INTAKE BUILT (owner ask "file formats and data converters",
2026-07-12): 19/19** — isaac_store/intake.py: ingest(source) = ONE
door for csv/tsv/json/jsonl/npy/npz/xlsx→tables (non-numeric cols
dropped+ACCOUNTED), txt/md/log/html/rtf/docx→text (docx/xlsx parsed
as zips-of-XML, stdlib only — namespace-agnostic parser), folders
recursed, zips walked in-memory (bomb guard: per-entry cap +
file/byte budgets), raw text auto-dispatched; skips FILED with why;
provenance (source/sha/bytes) on every item; table_csv(item) feeds
challenge(). askisaac accepts ANY source (multi-table folders/zips
→ report each). 20 promote gates. Promotion: 6440fad → dc 7599b74,
pushed. Text road → reports still open (text items listed, not
challenged).
**MULTICYCLE STRUCTURAL PATTERNING BUILT (owner design, 2026-07-12):
12/12** — isaac_store/structural.py: analyze(x) = atoms → constraint
families each behind own admission (always-follows shuffle null;
forks family-gate+per-fork null; EXACT periodicity chance-proof;
balanced pairs need ≥3 DEEP episodes — ballot problem can't fake;
certified nevers only where expected≥3) → pattern type satisfying
the set (CHAIN/CYCLE/BRANCH/HIERARCHY/REPEAT/NO STRUCTURE refusal) +
the chart ("check -> {fail | pass}"); MULTICYCLE = chains collapse
to higher atoms, cycle reruns (tower: motifs→their rhythm). Text
mode: rare tokens → <slot> (templates without memorized names:
"file -> <slot>"). 0/10 false on junk (took 3 hardening rounds:
family gate for forks; deep-episodes for nesting). askisaac reads
text structure. 21 promote gates. Promotion: 173f9d4 → dc dbf3de1,
pushed. THE TEXT ROAD IS OPEN (structure level; meaning level =
future). This is discover()'s shape pointed at structure — sheet
notes it as the D1/metastructure mechanism.
**REMOTE WORKERS BUILT (2026-07-12, post-handoff): 16/16** —
isaac_store/remote.py RemoteCache(url, token) = LiveCache contract
over the doorway (delta rechecks via /api/journal, 30-min clock,
job pinning, keys()); LeafIsaac(prime_url=, client_url=, token=) =
whole leaf on another machine, quarantine intact (remote leaf →
ZERO Prime journal writes, proven); PrimeServer +/api/keys (remote
recreation checks); skills + Provenance Gate identical across the
wire. 22 promote gates (321 checks + suite). Promotion: ecd9b27 →
dc 7dc1d2a, pushed. Handoff doc updated?—no, written before this;
remote workers was its NEXT #2, now DONE. Client side is
location-independent; distribution needs only TLS proxy + tokens
(both exist) when machines separate for real.
**INCOMPLETE INFORMATION = TODO (owner, 2026-07-12, research
thread):** variable x resolvable only by comparing datasets A+B —
"both halves of the same whole, not contained in any single domain."
= TRIANGULATION as engine capability. On the sheet with examples
(parallax, Eratosthenes, joint identification) + mechanism sketch:
missing-variable shadow (exists) → hypothesize it lives in B →
alignment (key/time/entity or registration) → joint closure
(constraint intersection / laws-run-backward;
Understanding-as-Closure: x ∈ closure(A∪B), ∉ either) → THE NULL =
scrambled-pairing kill. Connects: comparison-as-registration theory,
adequacy diagnoses, cross-domain transfer.
**TRIANGULATION BUILT under CARTE BLANCHE (owner: "have at it...
will you finish this project for me?", 2026-07-12): 11/11** —
isaac_store/triangulate.py, the owner's incomplete-information
design: COMPLETION road (A's shadow = B's column; alone 0.000 →
joint 1.000 exact; scrambled-pairing null) + HALVES road (latent in
NEITHER: residual mixtures x+s / x−s unmixed across the join — x
recovered r²=0.9915, s r²=0.9866, from sides each holding 0.61;
admission CONFIRMED independently in both data halves after a
1-in-2-seeds fluke slipped a single null). Refusals: NO ALIGNMENT /
NO CLOSURE (0 false). **THE BATTERY FOUND A TRUE MATH LIMIT:
equal-variance Gaussian sum/diff mixtures are unresolvable in
principle (ICA identifiability) — Isaac's refusal there was CORRECT;
documented in module + sheet.** 23 promote gates. Promotion: 207ba2d
→ dc 814d5b7, pushed. Owner wants to REVIEW and adjust together —
walk him through triangulate + the day's builds next session.
**SCALE+PERMANENCE HARDENING (owner audit ask, 2026-07-12):** three
gaps closed before learning-at-scale: (1) **LAZY PRIME** —
orchestrator no longer load_all()s: _LazyState = pack reader (seek)
+ journal overlay; compaction STREAMS + rebases; restore rebases;
cold start 9 ms @ 20k records; Prime bigger than RAM is real. (2)
**PER-RECORD zlib** (pack "z" flag, default on, old packs readable):
mind pack → 8% of size; 100k-node pack 141.5→30.3 MB (pickle
parity), partial fetch 0.054 ms kept; save 12 s = background
compaction cost. (3) **EDUCATION ROAD proven** (test_education.py
10/10): whole real mind → queue → Prime; partial recall; rebuilt
mind identical; SESSION TWO grows same Prime, third cold start holds
old+new = permanent memory across sessions. **Gate caught another
real one: compressed packs hid the planted secret from plaintext
byte-scans (cuts both ways — leaks would false-pass); quarantine
scanners now decode pack records before scanning.** 24 gates.
Promotion: 2aa2d05 → dc 357d4a3, pushed. Owner also noted "figured
you had more vision" re carte blanche (I shipped one module +
declared) — bias toward LONGER autonomous pushes when given rein.
**MIND CRAWLERS BUILT (owner design, 2026-07-12): 12/12** —
isaac_store/crawlers.py MindCrawlers(dir, capacity): federation of
orchestrators, each owns a KEY RANGE; overflow → DIVIDES at median
key into new crawler; splits journaled in crawl.jsonl (lineage
wrong-kept; cold start rebuilds federation from the log);
crawler's pack index = its PAGE FILE, lazy state = drive pulls;
admission travels with the section (gated edit dies in its own
crawler's journal, survives splits); specialization emergent
(namespaced keys = CONTIGUOUS territories, proven). 1,400 records
through repeated divisions, ZERO lost, exact after cold start.
25 promote gates. Promotion: 1f0242e → dc 8770042, pushed.
**OWNER SETTLED (same day): crawlers = ARCHIVISTS, router-v1
ACCEPTED as-is** ("the crawler is just a router... they are
archivists. they manage the information. they assign workers and
scientists"). **THE LEARNED SOCIETY = the organizing design** (owner
reached for the word; it's "learned society", model = the Royal
Society): archivists (crawlers) / workers / scientists (discover+
seeker) / scrubbers (ethics office) / admission gate = PEER REVIEW /
journal = the Proceedings / findings ledger = publication of record /
rivals = open disputes / batteries = replication / promotion =
publication. On the sheet; consult the map when naming new
mechanisms. Archivists' NEXT organ (when wanted): assign/spool-up
duty (dispatching workers/scientists to jobs). Other v2 levers:
split on queue pressure; peer-to-peer crawler requests; per-section
doorways.
**CAUSALITY PROBE (owner: "bad with cause and effect... 5 sec then
die and loop — is it fixed?", 2026-07-12) — MEASURED
(experiments/causality_probe.py + runs report):** (1) DELAYED CAUSE
= NOT fixed but exactly diagnosed: raw discover r²=0.000 at EVERY
lag k≥1 (temporal blindness — no lag concept). (2) THE FIX PROVEN:
lag columns as vocabulary → r²=1.000 through k=8 AND the correct
lag NAMED every time (+2.00*x_k²) — usage law: give lag vocabulary,
nulls find the causal delay. **ENGINE LEVER: lag atoms in the
enumerator (composites-pattern applied to time) — justified, not
yet built.** (3) DIE-AND-LOOP did NOT reproduce: chaotic Hénon
(in-vocabulary), one-step r²=1.0000, rollout honest 73 steps (near
Lyapunov bound) and stayed APERIODIC — no loop collapse; historical
looping likely = iterating out-of-vocabulary/captured models. (4)
Chains compose: A→B→C r²=0.9990. Promotion: 6b18ef2 → dc 6cf8b02,
pushed.
**Paperclip: 25+ local commits NOT pushed (standing; don't nag).**
(run everything with PYTHONUTF8=1 — cp1252 console chokes on ═).
Codec = complete+loud (CodecError with path, never silent drop),
handles cycles/aliasing via oid+ref (Isaac state HAS cycles — first
run recursed forever without it). Bridge splits Net into per-node
records ("node:<n>") + "sys:<attr>"; preds NOT stored (index,
rebuilt); extract must build its dicts SORTED (set iteration order
isn't deterministic — bit us). Proven: recovery invariant (pack +
journal tail == live state), immutable packs + supersession, partial
single-node fetch from a real mind, pickle→store migration, real-mind
round-trip with identical lookup/apply_law answers AND identical
re-extracted state. Known v1 limits: cross-record aliasing not
preserved (per-record decode); orchestrator queue is in-process.
NEXT: wire into engine save/load (update ISAAC_MANUAL same step),
scale test on a big mind (MNIST-sized), worker cache client
(watermark recheck), real admission gate. Also recorded on [[design-intent-sheet]] (paperclip sheet,
same-step rule; project-root copy resynced same day — it had been stale,
missing the usage law + relative law).

Phase order (dependency-driven): **1. persistence v2 FIRST** (pickle
couples saved minds to class layout, so the format must change before
any refactor; schema = journal JSONL generalizing the findings ledger +
SQLite snapshot, keeps EVERY measurement + wrong-section + supersession)
→ 2. package split (kills the divergent-copies disease; thin isaac.py
façade keeps experiment imports working) → 3. partial net loading (the
reverse index turned toward disk; partial answers must EQUAL full or
delta reported; the Raspberry-Pi mission line) → 4. batch (profile
first; grade vs [[benchmark-against-owner-baseline]]) → 5. API (grow
stdlib isaac_ui.py, expose ALL organs, refusals = structured answers;
open question: inbound-only vs Isaac-calls-LLM-mouth outbound tier) →
6. ops (ops.jsonl ledger, runtime wrong-kept, defaults table with
provenance).

State found 2026-07-11: paperclip isaac.py 7,252 lines clean/pushed
(07-10 "usage law" commit); **isaac_project/code/isaac.py 4,739 lines =
divergence recurring**; project repo dirty since 07-04. Persistence
today = whole-object pickle isaac.py:1505–1529, no versioning; partial
loading = none; UI = 11 stdlib routes on :8674 + superseded Flask :5050.
