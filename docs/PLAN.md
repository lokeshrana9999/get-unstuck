# Plan

> **Superseded (2026-10-31) by [ACTION-PLAN.md](ACTION-PLAN.md),** which adds owners, gates and the changes prompted by the verdict. This file is kept for history.

> **Pivot (2026-10-31).** The scope changed ([PIVOT.md](PIVOT.md)). Get Unstuck is no longer only a helper for the moment someone is stuck. It is now a **productivity bot for ADHD people**: onboarding asks what they want to get done and when they want reminders; Grok Bot routines send check-ins, start nudges, body-doubling sessions and end-of-day reviews; and the flowchart is the in-the-moment engine when a check-in finds someone stuck. Proactive messages bring new rules (default ≤ 3 contacts a day with a hard ceiling of 5, quiet hours 21:00–08:00, no escalation, opt-out words that act at once) and a platform spike before any build. The milestones below are kept as they were written; each is marked **still applies**, **applies, expanded** or **no longer applies as-is**. The working plan is [ACTION-PLAN.md](ACTION-PLAN.md).

**Goal (original):** publish *Get Unstuck: Task Starter for ADHD & Executive Dysfunction* as a Grok Bot template. *(After the pivot the name is under review in [naming.md](naming.md), decision D-11.)* It should be faithful to the flowchart, honest about evidence, and safe by default.

**Status (2026-10-31): planning.** The repo structure, data model, drafts and CLI prototype exist. The bot itself has not been created.

Each milestone ends with a checklist. "Exit criteria" must be met before moving on.

---

## M0. Foundations ✅ (this commit)
*Still applies (done). The pivot added more drafts: onboarding skill, rewritten routines, guardrails §8, research and naming docs (ACTION-PLAN Phase 0).*
- [x] Source material collected in `source/`: chart image, reviewed breakdown, review, fixes log and evidence review.
- [x] Platform research: [research-grok-bot.md](research-grok-bot.md).
- [x] `data/flowchart.json` and its JSON Schema, including evidence levels and routing confidence.
- [x] A dependency-free CLI prototype with tests and CI.
- [x] Drafts: persona, 7 skills, routines, guardrails, sheet design.

## M1. Fidelity sign-off
*Still applies: the flowchart is still the stuck-flow engine (ACTION-PLAN D-1, C-01b, C-08).*
- [ ] Settle the "still to fix" items from `source/review_v2.md` in `breakdown_v2.md`, then re-check `flowchart.json` against them.
- [ ] Get a second person to walk every path with the CLI (`python -m get_unstuck`) beside `chart.png`.
- [ ] Decide the "Go through the flowchart again" target (currently Step ①, marked interpretive).
- [ ] Try to identify and contact the chart's original author for credit and permission (see README).

**Exit:** no open fidelity issues. Every `most_likely` routing has either been confirmed or is accepted as-is.

## M2. Conversation design
*Applies, expanded: onboarding transcripts, nudge template tests and a guilt-pattern lint are added (ACTION-PLAN P-02, P-03, P-05).*
- [ ] Write 3–5 example dialogues per skill, covering a happy path, a loop, a refusal and distress.
- [ ] Write a tone check list ("no shame words" and similar) and apply it to every draft.
- [ ] Add evidence-informed tips (`bot_tip`), clearly labelled, and have someone review them.
- [ ] Optional: get a review from someone with lived ADHD experience, and ideally a clinician.

**Exit:** the dialogues read as warm, short and shame-free to at least 3 testers.

## M3. Safety review
*Applies, expanded: red-team cases must also run as replies to proactive nudges (guardrails §8.9; ACTION-PLAN P-06).*
- [ ] Re-verify the crisis lines (Tele-MANAS 14416 / 1-800-891-4416, 988, Samaritans 116 123, findahelpline.com).
- [ ] Write red-team prompts: indirect distress, medication questions, requests to message someone, "just do it for me", minors.
- [ ] Confirm the bot asks for an explicit yes before **every** app action, even when "Always allow" is on.
- [ ] Check the physical-safety substitutions (no phone-tossing or spilled water).

**Exit:** every red-team prompt has a passing transcript in `docs/safety-tests/` (to be created).

## M4. Build in Grok Bot (manual, in the app)
*No longer applies as-is: a platform spike on scheduling now comes first; there are 8 skills (onboarding added); routines are created only through onboarding with a preview and a yes each; the cap, quiet hours and opt-out must be verified in the app (ACTION-PLAN Phase 3).*
- [ ] Create the Bot: set the name, label and picture from `bot/persona.md`.
- [ ] Paste the setup prompt and ask the Bot to remember it.
- [ ] Add each skill by pasting its `SKILL.md` and asking "save this as a skill called …". (Direct import is an open question.)
- [ ] Optional: connect Google Sheets and create the log from [sheet-design.md](sheet-design.md).
- [ ] Add the routines from `bot/routines.md`, all off or opt-in.
- [ ] Run the M2 dialogues and M3 red-team prompts inside Grok Bot and record the results.

**Exit:** the in-app behaviour matches the drafts, and safety tests pass.

## M5. Private beta
*No longer applies as-is: feedback goes to a private form, not a GitHub issue (D-8); the beta runs 30 days; metrics are built around drop-off (ACTION-PLAN Phase 4).*
- [ ] Share as a template link with 5–10 testers.
- [ ] Collect feedback through a GitHub issue template (no personal health data).
- [ ] Iterate, then bump `data/flowchart.json` `meta.version` and `CHANGELOG.md`.

## M6. Public template
*Applies, expanded: the go/no-go gate adds no treatment claims and in-app checks of the cap, quiet hours and opt-out (ACTION-PLAN Phase 5).*
- [ ] Publish the template link in the README.
- [ ] Recheck the crisis numbers and the docs links.
- [ ] Decide whether to apply for the *Bot templates* gallery, if submissions are possible.

---

## Later / ideas (not committed)
*Partly absorbed: per-strategy tracking now has a `strategy_that_helped` column in the optional Sheet (sheet-design.md).*
- Translations, starting with Hindi given Tele-MANAS.
- Export `flowchart.json` to Mermaid for a text-based, accessible diagram.
- Track which strategies help *this* person most and suggest those first, opt-in and stored only in their Sheet.

## Risks
*Still applies, but incomplete after the pivot. See ACTION-PLAN risks 11–15 (notification fatigue, drop-off, usage cost, scheduling unknowns, over-reliance).*

| Risk | Mitigation |
|---|---|
| Platform features change, or the skill format is unknown | Keep the drafts portable (plain markdown). Track open questions in research-grok-bot.md. |
| The bot is seen as medical advice | Disclaimer in the description, guardrails, no diagnosis or medication advice. |
| Missing a crisis signal | Prompt-level instructions plus red-team tests. Never rely on keywords alone. |
| Unknown chart author and image rights | Don't redistribute the image in the bot. Credit it and keep trying to find the author. |
| Overstating evidence | Evidence levels in the data, plus an honesty guardrail. |
