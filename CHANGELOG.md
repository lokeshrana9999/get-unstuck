# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
