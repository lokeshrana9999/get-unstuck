# Action plan 01: Content and evidence fixes

**Scope.** This plan covers what the bot *says* and how honestly it says it: the routing decisions, the overlay wording, tone, the if-then template, the honesty tags, the example dialogues, keeping in sync with `source/evidence_review.md`, outside review, and credit for the chart author. It does not cover platform build (M4), crisis lines or red-teaming (M3), or the Sheet.

**Baseline (Phase 0, treated as done).** `data/flowchart.json` has these overlays:
- a `bot` overlay on every strategy (`action`, `honesty`, optional `text`; evidence `refs` stay in `evidence`);
- node fields `bot_title`, `bot_text` and `bot_repeat_next`;
- option fields `bot_label` and `bot_to`. "Worried I'll fail" goes to `break_it_down`, and the comic exchange is one round.

The CLI also has a `--bot` mode. Chart text stays verbatim.

---

## P0: must be done before building (M4)

### C-01 Decide and document the 5 ambiguous routings (Lokesh)
Refs: verdict §3, §4e.1; review_v2 Error 1; verdict-response disagreement 7.

These are the 5 routings, plus a sixth open item:

| # | Routing | Options affected | Bot override? |
|---|---|---|---|
| 1 | Bottom of RESIST IMPULSES | `resist_impulses` → `interrupt_inertia` / `comic_go_step4` | Partly (comic exchange shortened) |
| 2 | Split below "Why?" | `why_bad` → `make_tolerable` / `go_step4` | Yes (`bot_to: break_it_down` for "worried") |
| 3 | PRIORITIZE "I know what to do now!" | → `great_job_step2` | No |
| 4 | INTERRUPT INERTIA outcomes | → `hell_yeah` | No |
| 5 | Step ④ "I may have skipped some" | → `go_again` | No |
| + | `go_again.next` (marked `next_interpretive`) | → `step1` | `bot_repeat_next` |

Steps:
1. Bot writes a one-page decision sheet. For each row it gives the current encoding, the plausible alternative reading, the effect on the chart walk and on `--bot` mode, and a recommendation.
2. Lokesh picks one of three for each row: confirm, change, or accept as `most_likely`.
3. Bot records each decision and its date next to the option (proposed field: `decision`), and updates `breakdown_v2.md` with the review_v2 "still to fix" items 1–6.

Acceptance:
- A test fails if any `most_likely` option or `next_interpretive` node has no recorded decision.
- The CLI walk of each changed path matches the decision.

### C-02 Audit every bot overlay against the evidence review (Bot drafts; Lokesh signs off)
Refs: verdict §2, §4a–b; verdict-response disagreements 2 and 6.

Steps: for all 50 strategies, make a table with these columns:
- chart text;
- `action`;
- `bot.text`;
- `honesty`;
- the claim and principle levels from evidence_review;
- any overreach found.

Check that each overlay follows these rules:
- **drop** only for harm or contradiction, otherwise label;
- `bot.text` never claims more than the *claim* rating supports;
- principle-level support is described as "the idea behind this has support", not as support for the tip itself;
- the C4 reword says "small rewards during and right after";
- the E3 dose is 10–20 minutes, with "a minute is a start";
- C1 says noise rather than music for word tasks;
- D2 uses "check the facts";
- C7 includes the untested/routine-tasks caveat.

Also reconcile `bot/guardrails.md` §5 with the banned-claims list. At the moment §5 *allows* "evidence-based" for claims rated moderate or above, but verdict §4d.6 bans it outright.

Acceptance:
- Every `refs` code exists as a heading in evidence_review.md (test).
- The honesty-ceiling test passes.
- The audit table is reviewed, with zero open rows.

### C-03 Tone and shame-word pass (Bot)
Refs: persona "No shame words"; verdict §4e.5; H7.

Steps:
1. Fix the word list: "just", "simply", "should have", "lazy", "easy", "only takes", "obviously", "failed".
2. Apply it to `bot.text`, `bot_text`, `bot_label` and the "Bot approach" sections of the skills. Chart quotes are exempt.
3. Fix the known conflicts. "Can you do it for just 10 minutes?", "Wait just 5 minutes" and "Stop … for just 5 minutes" need bot wording without "just".
4. Check the comic and playful lines ("*actually*", "Hell yeah", "Half-ass it") by reading them aloud. Keep them unless Lokesh objects.

Acceptance:
- A test scans all bot copy for the list and passes.
- No bot message is longer than about 3 short sentences plus one question.

### C-04 One canonical if-then plan template (Bot)
Refs: B3, H2, G5; takeaway 2; verdict §4c.2.

Steps:
1. Define the template once, for example in `data/flowchart.json` `meta` or in guardrails: **"At [time], at [place], I will [first physical action]."** Use it in `smallest_step`, `prioritize_top3` and `reschedule`, and as the end-of-session close.
2. Set the rules:
   - the time is concrete, or the cue is an event ("when I finish lunch");
   - the action is observable and under 5 minutes;
   - the person writes or confirms it in their own words.
3. Add a fallback for a user who can't name a time: offer an event-based cue and don't press.

Acceptance:
- A test checks that every if-then overlay contains the canonical slots.
- The skills quote the same template.

### C-05 Honesty-tag wording users see (Bot drafts; Lokesh approves)
Refs: verdict §4c.5; evidence review intro; caveat 1.

Draft wording:

| Tag | What the user sees | Rule |
|---|---|---|
| `well_supported` | "Good research support (mostly not in ADHD specifically)" | Shown as is |
| `reasonable_untested` | "Reasonable idea, not tested in this form" | Shown as is |
| `hack` | "A hack some people like; no real evidence" | Shown as is |
| `not_supported` | Never offered | Explained only if the user asks about it |

Steps: put the mapping in one place, decide where the tag goes (a short suffix, at most one per message), and give the bot a one-line "why?" answer per tag.

Acceptance:
- `--bot` mode prints the approved phrases.
- A test checks that no `not_supported` tip is offered.

---

## P1: before the beta (M5)

### C-06 Example dialogues for each skill (Bot; reviewed by 3 testers)
Refs: PLAN M2; verdict §4e.4–5; guardrails §2.

Steps: write 4 dialogues for each of the 7 skills:
1. a happy path;
2. a loop, which must show the second-pass offer of Step ⑤ and still allow a new reason to be named;
3. a refusal, such as "No!!!", which takes one round and then moves to radical acceptance;
4. a distress hand-off, where the flow stops, crisis resources are given, and there is no tip-giving. Coordinate these with the M3 safety plan.

Mark the dialogues as illustrative and not scripts, so the bot doesn't copy them word for word.

Acceptance:
- All 28 dialogues exist.
- Each one passes C-03 and C-05.
- The distress dialogues match guardrails §2.
- Testers rate them warm, short and shame-free (PLAN M2 exit).

### C-07 "Half-ass it" earlier, and "did you forget?" handled at session end (Bot)
Refs: verdict §4e.6, §4c.1; verdict-response disagreement 4; B6, H4, A2.

Steps:
1. In extension-or-delegate, offer "do a good-enough version" as the second option after "No flexibility".
2. In break-it-down, offer it early for "too hard / afraid I'll fail", unless the user says quality is critical.
3. Any session that ends without a start closes with a C-04 plan and an *optional* R2 reminder. This stays within the check-in cap (default ≤ 3 a day).

Acceptance: the C-06 dialogues show all three behaviours, and a skills-text test finds them.

### C-08 Credit and permission from the chart author (Lokesh; Bot drafts)
Refs: verdict §4c.6; verdict-response "adapted from"; PLAN M1, Risks.

Steps:
1. Search for the author (reverse image search, the community where the chart was first posted).
2. Bot drafts a request that lists the adaptations, generated from the overlay diff, so that permission covers the changes.
3. Log each attempt with its date.
4. If the author is found, set `meta.chart_author` and the README credit. If not, keep "adapted from; author unknown, please contact us" and don't redistribute the image.

Acceptance: before public launch (M6) there is either written permission, or a dated attempt log plus the fallback credit.

### C-09 Evidence-sync mechanism (Bot)
Refs: evidence review caveat 3; F4.

Steps:
1. Record the evidence_review revision date in `meta`.
2. Add a test that every `refs` code resolves, and that the honesty ceilings still hold after any edit to the evidence review.
3. Add a banned-citations list: Ariely & Wertenbroch 2002, retracted September 2026, plus any Zeigarnik rationale.

Acceptance: CI fails on stale refs or banned citations in bot copy.

---

## P2: later

### C-10 Re-verification cadence and retraction watch (Bot runs it; Lokesh schedules)
Steps:
1. Every quarter, and before M6:
   - re-check that the DOIs behind every rating moderate or above resolve and have not been retracted, using Crossref and retraction notices;
   - re-check the "considered but not verified" list.
2. If a citation is retracted or a rating is downgraded, re-tag the affected overlays and log the change in CHANGELOG.

Acceptance: a dated check entry exists for each quarter.

### C-11 Clinician and lived-experience review (Lokesh; optional)
Steps:
1. Share the C-02 audit table, the C-05 wording and the C-06 dialogues with one person who has lived ADHD experience and, ideally, one clinician.
2. Fold their notes into the overlays.

Acceptance: the notes are recorded and each one is accepted or rejected with a reason.

---

## Risks

| Risk | Mitigation |
|---|---|
| Users read "good research support" as "proven for me" | The C-05 wording names the gap ("mostly not in ADHD"); no "proven" or "evidence-based" anywhere |
| Overlays drift from the evidence review over time | C-09 CI tests; C-10 cadence |
| The tone pass sands off the chart's warmth and humour | Keep the playful lines by default (C-03 step 4); testers judge warmth (C-06) |
| The bot overfits to the example dialogues | Label them illustrative; vary the wording across the four |
| The routing decision stalls the build | C-01 sheet arrives with recommendations; "accept as most_likely" is a valid choice |
| The author objects to the adaptation | Ask early (C-08); faithful mode keeps a clean diff; be ready to rename or withdraw |
| The evidence review is a single unreviewed source | C-11; ratings stay as stated, with no new citations added by the bot |

## Open questions for Lokesh

1. For each of the 5 routings and `go_again`: confirm, change, or accept as `most_likely`?
2. Should honesty tags show on every tip, or only on the first mention and when the user asks?
3. Should the bot say "Half-ass it" as-is, or "do a good-enough version"?
4. Is the C-05 wording acceptable, especially "mostly not in ADHD"?
5. If the chart author can't be found by M6, do we ship with the fallback credit or wait?
6. Is there a budget or contact for the clinician or lived-experience review (C-11)?
7. Who owns the quarterly re-verification (C-10)?
