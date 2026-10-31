# Plan

**Goal:** publish *Get Unstuck: Task Starter for ADHD & Executive Dysfunction* as a Grok Bot template. It should be faithful to the flowchart, honest about evidence, and safe by default.

**Status (2026-10-31): planning.** The repo structure, data model, drafts and CLI prototype exist. The bot itself has not been created.

Each milestone ends with a checklist. "Exit criteria" must be met before moving on.

---

## M0. Foundations ✅ (this commit)
- [x] Source material collected in `source/`: chart image, reviewed breakdown, review, fixes log and evidence review.
- [x] Platform research: [research-grok-bot.md](research-grok-bot.md).
- [x] `data/flowchart.json` and its JSON Schema, including evidence levels and routing confidence.
- [x] A dependency-free CLI prototype with tests and CI.
- [x] Drafts: persona, 7 skills, routines, guardrails, sheet design.

## M1. Fidelity sign-off
- [ ] Settle the "still to fix" items from `source/review_v2.md` in `breakdown_v2.md`, then re-check `flowchart.json` against them.
- [ ] Get a second person to walk every path with the CLI (`python -m get_unstuck`) beside `chart.png`.
- [ ] Decide the "Go through the flowchart again" target (currently Step ①, marked interpretive).
- [ ] Try to identify and contact the chart's original author for credit and permission (see README).

**Exit:** no open fidelity issues. Every `most_likely` routing has either been confirmed or is accepted as-is.

## M2. Conversation design
- [ ] Write 3–5 example dialogues per skill, covering a happy path, a loop, a refusal and distress.
- [ ] Write a tone check list ("no shame words" and similar) and apply it to every draft.
- [ ] Add evidence-informed tips (`bot_tip`), clearly labelled, and have someone review them.
- [ ] Optional: get a review from someone with lived ADHD experience, and ideally a clinician.

**Exit:** the dialogues read as warm, short and shame-free to at least 3 testers.

## M3. Safety review
- [ ] Re-verify the crisis lines (Tele-MANAS 14416 / 1-800-891-4416, 988, Samaritans 116 123, findahelpline.com).
- [ ] Write red-team prompts: indirect distress, medication questions, requests to message someone, "just do it for me", minors.
- [ ] Confirm the bot asks for an explicit yes before **every** app action, even when "Always allow" is on.
- [ ] Check the physical-safety substitutions (no phone-tossing or spilled water).

**Exit:** every red-team prompt has a passing transcript in `docs/safety-tests/` (to be created).

## M4. Build in Grok Bot (manual, in the app)
- [ ] Create the Bot: set the name, label and picture from `bot/persona.md`.
- [ ] Paste the setup prompt and ask the Bot to remember it.
- [ ] Add each skill by pasting its `SKILL.md` and asking "save this as a skill called …". (Direct import is an open question.)
- [ ] Optional: connect Google Sheets and create the log from [sheet-design.md](sheet-design.md).
- [ ] Add the routines from `bot/routines.md`, all off or opt-in.
- [ ] Run the M2 dialogues and M3 red-team prompts inside Grok Bot and record the results.

**Exit:** the in-app behaviour matches the drafts, and safety tests pass.

## M5. Private beta
- [ ] Share as a template link with 5–10 testers.
- [ ] Collect feedback through a GitHub issue template (no personal health data).
- [ ] Iterate, then bump `data/flowchart.json` `meta.version` and `CHANGELOG.md`.

## M6. Public template
- [ ] Publish the template link in the README.
- [ ] Recheck the crisis numbers and the docs links.
- [ ] Decide whether to apply for the *Bot templates* gallery, if submissions are possible.

---

## Later / ideas (not committed)
- Translations, starting with Hindi given Tele-MANAS.
- Export `flowchart.json` to Mermaid for a text-based, accessible diagram.
- Track which strategies help *this* person most and suggest those first, opt-in and stored only in their Sheet.

## Risks
| Risk | Mitigation |
|---|---|
| Platform features change, or the skill format is unknown | Keep the drafts portable (plain markdown). Track open questions in research-grok-bot.md. |
| The bot is seen as medical advice | Disclaimer in the description, guardrails, no diagnosis or medication advice. |
| Missing a crisis signal | Prompt-level instructions plus red-team tests. Never rely on keywords alone. |
| Unknown chart author and image rights | Don't redistribute the image in the bot. Credit it and keep trying to find the author. |
| Overstating evidence | Evidence levels in the data, plus an honesty guardrail. |
