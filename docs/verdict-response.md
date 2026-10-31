# Response to the verdict (`docs/verdict.md`)

*Written 2026-10-31 by the agent that built the first version of this repo. Section codes such as B3 or F1 refer to `source/evidence_review.md`. "§4b" and similar refer to sections of the verdict.*

## TL;DR

I agree with the verdict's bottom line: **conditional yes.** Build the bot on the chart's structure and tone, re-weight the content toward what the evidence supports, and drop the unsafe and misleading parts. Roughly 80% of its recommendations were already partly covered by the first version, through safety notes, `bot_tip`s, evidence levels and guardrails. Two of its recommendations, though, need a design change rather than just more notes:

1. **The bot is an *adaptation*, not a port.** Until now, `flowchart.json` encoded only the chart, with the bot's changes added as side notes. Now every strategy carries an explicit **bot overlay** in the data: keep, reword, replace or drop, plus a plain-word **honesty tag**. That way every departure from the chart can be audited and tested.
2. **Lead with what works.** The bot should present the best-supported tips first and the fun hacks after them. This is now a rule in the skills, and the CLI's new `--bot` mode orders tips by honesty tag.

I disagree in a few places, mostly where the verdict would throw away information the project needs (details below).

---

## Where I agree, and what it changes

| Verdict point | Agree? | What changes in the repo |
|---|---|---|
| Overall vibe: warm, sound skeleton, pop-neuro coat of paint, one unsafe hack (§1) | Yes | Nothing to change. This matches `evidence_review.md` and how the persona is already written. |
| Drop the "harmless problem" hack (§4a.1) | Yes (already a guardrail) | Bot overlay `replace`: "Set a timer or alarm across the room". The node gets a `bot_text` in place of the chart wording. |
| Drop "Delicious snack" as a reset (§4a.2) | Yes | Overlay `drop`, tagged *not supported*. Hunger stays covered in the needs check. |
| Rename "Follow the dopamine" to "swap the reward" (§4a.3) | Yes | Overlay `reword`. Bot copy must never use "dopamine" (enforced by a test). |
| Drop the willfulness worksheet; shorten the comic exchange to one round (§4a.4, §4e.4) | Yes | Overlay `drop`. In bot mode, refusing "Go to Step 4" leads straight to "Fine." and then radical acceptance (`bot_to`). |
| Drop "Look back" (§4a.5) | Mostly (see disagreements) | Overlay `drop`. The chart text stays in the data. |
| No Zeigarnik explanation, no Ariely & Wertenbroch citation (§4a.6–7) | Yes | Already absent. Added to the guardrails' banned-claims list. |
| Rewordings (§4b): Quick reset, exercise dose, noise rather than music, small and immediate rewards, "Pause and reflect", DBT "check the facts", if-then rescheduling, "1 next thing", body-doubling caveat | Yes | Each is now a `bot.text` overlay. Node titles get `bot_title` (MINDFULNESS → PAUSE AND REFLECT, DIY DOPAMINE → QUICK RESET). The PERFECTIONISM option gets a `bot_label` ("TOO HARD / AFRAID I'LL FAIL"). |
| "Goblin Tools: the bot does this itself" (§4b) | Yes | Overlay `replace`: "Let's break it down together right here". Goblin Tools is mentioned only as an optional outside tool. |
| If-then plan as the default output (§4c.2) | Yes; this is the single most important change | The overlays for `smallest_step`, `prioritize_top3` and `reschedule` all end in "At [time], at [place], I will [first action]". The break-it-down skill makes it the required output. |
| Re-route "I'm worried I'll fail" to BREAK IT DOWN (§4c.3) | Yes | `bot_to: break_it_down` on that option. The chart routing (→ Step ④) stays in `to`. |
| "Get assessed" nudge (§4c.4) | Yes (already routine R5 and guardrails §1) | Also surfaced in the extension-or-delegate skill after a loop. |
| Honesty tags in plain words (§4c.5) | Yes | New `bot.honesty`: `well_supported` / `reasonable_untested` / `hack` / `not_supported`. A test enforces that nothing is tagged *well supported* unless its own claim is rated moderate or higher. |
| Credit and permission line (§4c.6) | Yes, with an addition | Credit now reads **"adapted from"**, not just "based on". Because we change the content, the permission request must cover the adaptations too. |
| Safety guardrails (§4d) | Yes | Already covered: no diagnosis, crisis lines, water caveat, food not framed as a booster. **Added:** movement only if safe for the person's body; a cap on check-ins (default ≤ 3 a day, user sets the cadence); don't keep pushing food; never imply the user has ADHD (A1); a banned-claims list ("proven", "evidence-based", "dopamine"). |
| Lead with the best-supported steps (§4e.2) and friction first for impulses (§4e.8) | Yes | Skills reordered. `--bot` mode sorts tips by honesty tag. In resist-impulses, distance, make-it-harder, find an out and accountability now come before naming, waiting and looking forward. |
| Cap the loops (§4e.3) | Yes, but softer (see below) | `bot_repeat_next: step5` on `go_again`. On a second "go through again", the bot offers Step ⑤. |
| "Half-ass it" earlier (§4e.6) | Yes | Skills only: offered next to delegation after "No flexibility", and early for "too hard / afraid I'll fail". The JSON stays chart-shaped here. |
| Close the loop with the user's data (§4e.7) | Yes (Sheet design exists) | Unchanged. Noted that Grok Bot memory is an opt-in, lighter alternative to the Sheet. |
| Honest pitch: "a structured coaching flow built on reasonable principles" (§3) | Yes | The persona description and README now say this. |

## Where I disagree or would refine

1. **"Not a faithful port" should not mean "throw away the faithful layer."** The verdict proposes changing chart text in place, for example "Accomodate" → "Accommodate". I'm keeping the chart text verbatim, including *[sic]*, in `text`, and putting the bot's wording in `bot.text`. There are three reasons:
   - fidelity review (M1) needs the original text;
   - attribution and permission need a clear diff between the author's work and ours;
   - tests can then prove that every departure is deliberate.

   The verdict is right about what *users* see. I just wouldn't destroy the source of truth to get there.

2. **"Reward for after" isn't *contradicted*; it's *partly contradicted*.** The verdict files it under "Contradicted". `evidence_review.md` C4 says rewards help in ADHD (moderate) and only the *delayed timing* is contradicted. The data keeps `partly_contradicted`. The reword ("small rewards during and right after") is the right fix either way.

3. **The executive-function framing (A1) needs no change to the chart.** The chart never claims EF deficits define ADHD. A1 rates an *implicit* framing. The fix belongs in the bot's behaviour (don't imply the user has ADHD; EF trouble also comes with sleep loss, depression and more), not in chart content.

4. **The "did you forget?" branch at Step ② (§4c.1) is in the wrong place.** Someone talking to the bot has, by definition, remembered the task for now. Prospective-memory failures (A2) are better handled *at the end* of a session and *between* sessions:
   - every session that ends without starting closes with an if-then plan and an optional reminder (routine R2);
   - the morning routine (R1) acts as the external cue.

   So I agree with the goal and disagree with the placement.

5. **Loop cap: offer Step ⑤, don't force it.** "After one full pass, go to Step ⑤" is mostly right. But a user who answered "Yes, there are other reasons" may really have a new reason (say, hunger after an hour of trying). The bot offers Step ⑤ as the first option on the second loop and still lets the person name a new reason.

6. **"Look back": demote rather than delete on principle, though dropping it is fine in practice.** Its evidence is *none*, plus a hint from one non-peer-reviewed thesis. That's not *contradicted*. Dropping it while keeping equally untested items like grumbling or the Scientist Hat is slightly inconsistent. I've accepted the drop because the cost is low and it's the only harmless tip with a negative hint. The rule I'd apply in future: **drop for harm or contradiction; otherwise label.**

7. **Resolving the five ambiguous routings "before encoding anything" (§4e.1) is backwards for this repo.** Encoding them, with `confidence: most_likely`, is what makes them reviewable. A walker and tests let reviewers check each one. The verdict's real point stands: someone must *decide* them deliberately. That decision is now a Phase 0 task for Lokesh in the action plan. Two of the five (`why_bad` → "worried I'll fail" and the RESIST IMPULSES cluster) matter less now, because the bot overrides them anyway.

8. **The bot's name.** The verdict says "If you can't do the changes in section 4, don't ship it under that name." The §4 changes are now planned and mostly made. I'd keep the name, which Lokesh chose for discoverability, together with the no-diagnosis and "doesn't assume you have ADHD" behaviour. This is Lokesh's call, and the action plan lists it as one.

## What changed in the repo as a result

- `data/flowchart.json` (v0.2.0) and its schema:
  - a `bot` overlay on every strategy (`action`, `honesty`, optional `text`; evidence `refs` stay in `evidence`)
  - `bot_title`, `bot_text` and `bot_repeat_next` on nodes, and `bot_label` and `bot_to` on options
  - chart text unchanged
- CLI: a new `--bot` mode that shows the adapted bot flow, orders tips by honesty tag, hides dropped tips and follows the bot reroutes. The default mode is still the faithful chart walk, for fidelity review.
- Tests for: honesty-tag ceilings; no "dopamine", "proven" or "evidence-based" in bot copy; the unsafe hack and snack never shown in bot mode; correct spelling in bot copy; the bot reroutes; reachability in bot mode.
- `bot/persona.md`, `bot/guardrails.md`, `bot/routines.md` and the skills updated as described in the tables above.
- `docs/ACTION-PLAN.md`: the phased plan, merged from four planning subagents.
- README credit changed to "adapted from" and the honest pitch added. `CHANGELOG.md` updated.
