# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Pivot: ADHD productivity bot (2026-10-31, `docs/PIVOT.md`)

The bot changes from a "get unstuck when stuck" helper to a productivity companion. It onboards goals and reminder preferences, sends proactive nudges through Grok Bot routines, and uses the flowchart as the in-the-moment engine when a check-in finds someone stuck. Nothing was renamed, and no bot was created.

#### Added
- `docs/research-adhd-productivity.md`: research on reminders and prompting, if-then plans in ADHD, accountability and body doubling, time-blindness aids, notification fatigue and habituation, just-in-time adaptive interventions (JITAIs), and ADHD coaching and digital trials. It also covers app retention, the ADHD app landscape and pitfalls (Tiimo, Inflow, Goblin Tools, Structured, Focusmate, Llama Life, Routinery, Finch, Habitica), and what Grok Bot's scheduling docs confirm or leave unknown. Sources are linked, with evidence levels, weak or contested flags and unverified items marked.
- `bot/skills/onboarding/SKILL.md`:
  - 3 core questions;
  - a first if-then plan;
  - a preview of each routine and an explicit yes for each;
  - quiet hours and timezone;
  - opt-in memory (the Sheet is deferred);
  - re-onboarding after a gap with no guilt;
  - evidence notes with honesty tags.
- `docs/naming.md`: an assessment of the current name and 3 descriptive options. No rename was made; the decision is Lokesh's.
- `tests/test_pivot_drafts.py`: document checks that the drafts keep the agreed rules. They cover the routines sections, cap, quiet hours and snooze limit, guardrails §8, the onboarding flow and setup prompt, the Sheet tabs, the naming options, the research doc's sources and flags, and the absence of banned or guilt words in example lines. Enforcing the cap and quiet hours is still open.

#### Changed
- `bot/persona.md`: now productivity-focused. It adds proactive-nudge, stuck check-in and end-of-day examples, and the setup prompt runs onboarding first and encodes the nudge rules. The name is unchanged.
- `bot/routines.md`, rewritten:
  - platform facts and unknowns;
  - Cadence: at most 3 proactive contacts a day by default, 0–5 allowed, 5 as a hard ceiling;
  - Quiet hours: 21:00–08:00 by default, built into the schedules because the platform has no do-not-disturb;
  - Snooze: at most 2 per nudge;
  - Escalation limits: no escalation; ignored nudges are never followed up; after 3 ignored nudges of one type, that type is paused; after 7 days of silence, everything is paused;
  - Opt-out: acts immediately;
  - a catalogue of routines R1–R8, a daily load budget, a nudge state machine, and a list of what the design does NOT do.
- `docs/sheet-design.md`: rewritten with Goals, Tasks, Check-ins, Sessions, Wins, Settings and Summary tabs, plus "Streaks without shame" (counts only go up), batched logging behind a preview and a yes, privacy rules and untested formula drafts.
- `bot/guardrails.md`: new §8 Proactive messaging. It covers consent per routine, the cap and quiet hours, no escalation, snooze and ignore rules, opt-out, usage cost, forbidden guilt patterns, and crisis screening of replies to nudges. It also covers rest over productivity, accountability partners (drafts only), not implying human presence in body-doubling sessions, app data treated as data, minors, dependence and retention ethics. Requested follow-ups (snoozes, session messages) have their own limits and don't count toward the daily cap, consistent with `routines.md`.
- `bot/skills/triage/SKILL.md`: "Entry from a check-in" section. A [stuck] reply starts at Step ② with the task already known.
- `docs/ACTION-PLAN.md`, revised for the pivot:
  - Phase 0 pivot items;
  - decisions D-11 to D-17 (name, cadence, body doubling, calendar, store, usage-cost wording, beta thresholds);
  - repo tasks P-01 to P-10;
  - a platform spike first, with a decision table;
  - drop-off-aware beta metrics;
  - pivot conditions in the go/no-go gate;
  - new risks.
- README: describes the productivity bot ("How it works", "What the evidence says", name under review). `docs/PLAN.md` gets a pivot note marking which milestones no longer apply as they were written.
- Consistency fixes:
  - one entry step for [stuck] (Step ②);
  - the guardrails crisis-recheck pointer now points to S-01;
  - the part-03 routine description updated (R2 is a recurring slot);
  - Sheet tone values aligned with onboarding.

### Response to the verdict

Response to the independent verdict (`docs/verdict.md`). The bot is now an explicit *adaptation* of the chart, not a port.

#### Added
- `docs/verdict-response.md`: where we agree or disagree with the verdict, and what it changes.
- `docs/ACTION-PLAN.md`: a phased plan with owners (Bot or Lokesh), acceptance criteria, a go/no-go gate and consolidated risks. It was merged from four parallel planning parts in `docs/action-plan/`: content and evidence, safety and guardrails, Grok Bot implementation, and testing and launch.
- **A bot adaptation layer in `data/flowchart.json` (v0.2.0)** and the schema:
  - Every strategy has a `bot` overlay: `action` (keep, reword, replace or drop) and a plain-word `honesty` tag (well supported, reasonable but untested, a hack some people like, not supported).
  - Node fields `bot_title`, `bot_text` and `bot_repeat_next`, and option fields `bot_label` and `bot_to`.
  - The top-level `bot_honesty_labels`.
  - Chart text is unchanged.
- **A `--bot` CLI mode.** It shows the adapted flow, leads with the best-supported tips, hides dropped tips, shows honesty tags and follows the bot reroutes. With `--evidence`, chart mode also shows each tip's bot version.
- `tests/test_bot_mode.py`. It enforces:
  - the honesty ceiling: `well_supported` requires the tip's own claim to be rated moderate or higher;
  - contradicted claims are never kept as-is;
  - banned words in bot copy ("dopamine", "proven", "evidence-based", "just", "lazy", Zeigarnik, Ariely);
  - the unsafe hack and the snack tip never appear in bot copy;
  - "Check the facts" and "Accommodate" are spelled correctly in bot copy;
  - the reroutes, the one-round comic exchange, the loop cap, tip ordering and bot-mode reachability.
- `Flowchart.validate()` now also checks overlay presence, honesty tags, bot reroute targets, and that bot mode never traps the user in a loop.

#### Changed
- Overlays apply the verdict's §4a drops and §4b rewords:
  - **Dropped:** snack, "look back", the willfulness worksheet.
  - **Replaced:** the throw-your-phone / spill-water hack becomes a timer across the room; Goblin Tools becomes "let's break it down together".
  - **Renamed:** DIY DOPAMINE → QUICK RESET, MINDFULNESS → PAUSE AND REFLECT, PERFECTIONISM → "TOO HARD / AFRAID I'LL FAIL".
  - **Reworded:** "fit the facts" → "check the facts"; white or pink noise rather than music for word tasks; small rewards during and right after each step; move for 10–20 minutes if safe; "swap the reward" in place of "follow the dopamine"; if-then plans for "1 next thing", the smallest step and rescheduling; "just" removed.
- Bot reroutes:
  - "I'm worried I'll fail" goes to BREAK IT DOWN.
  - The comic "can't resist" exchange is one round.
  - A second "go through the flowchart again" offers Step ⑤ first.
- `bot/guardrails.md`:
  - don't assume the person has ADHD;
  - movement only if safe for their body;
  - don't push food;
  - at most 3 check-ins a day, with no follow-ups to unanswered nudges;
  - banned claims made absolute (fixes a conflict with the verdict);
  - Tele-MANAS toll-free number 1-800-891-4416 added to the crisis template reply.
- `bot/persona.md`: credit changed to "adapted from"; the honest pitch ("a structured coaching flow built on reasonable principles"); honesty tags; best-supported tips first; an if-then plan as the default close.
- Skills:
  - interrupt-inertia, resist-impulses and make-it-tolerable rewritten with bot wording and honesty tags;
  - resist-impulses puts friction first;
  - break-it-down makes an if-then plan the required output and offers a "good-enough version" early;
  - triage closes every unfinished session with a plan, which handles "did you forget?";
  - extension-or-delegate gets the loop cap and offers delegation and a good-enough version together.
- `bot/routines.md`: daily nudge cap.
- README: "adapted from" credit, honest pitch, `--bot` usage, and a note that the crisis keyword check isn't a safety system. `docs/PLAN.md` is marked superseded by `ACTION-PLAN.md`. CONTRIBUTING has the overlay rules. CI runs `unittest discover -s tests`.

## [0.1.0] - 2026-10-31

### Added
- Project structure for planning the *Get Unstuck* Grok Bot.
- `data/flowchart.json` (v0.1.0) and `data/flowchart.schema.json`:
  - 39 nodes and 50 strategies
  - evidence levels from `source/evidence_review.md`
  - `most_likely` confidence on the routings that `source/review_v2.md` flags as ambiguous
- `get_unstuck/`, a dependency-free CLI walker. Commands are `walk`, `validate` and `list`, with an `--evidence` flag and a crisis-keyword safety net.
- Tests covering data integrity, fidelity to the breakdown, CLI behaviour and consistency of the bot drafts. CI runs them on GitHub Actions.
- Bot drafts: `bot/persona.md`, `bot/guardrails.md`, `bot/routines.md`, and 7 `bot/skills/*/SKILL.md`.
- Docs: `docs/research-grok-bot.md`, `docs/PLAN.md`, `docs/sheet-design.md`.
- README, LICENSE (MIT for code; chart image rights reserved to its creator), CONTRIBUTING, CODE_OF_CONDUCT, issue templates.
