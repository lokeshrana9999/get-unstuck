# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

Response to the independent verdict (`docs/verdict.md`). The bot is now an explicit *adaptation* of the chart, not a port.

### Added
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

### Changed
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
