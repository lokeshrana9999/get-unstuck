# Contributing to Get Unstuck

Thank you for helping! This project is for people who find starting things hard, so we try to make contributing easy and kind.

## Ways to help
- **Fidelity checks.** Compare `data/flowchart.json` (or run `python -m get_unstuck`) with `source/chart.png`. Report any routing or wording that doesn't match. Use the *Flowchart fidelity* issue template.
- **Tone review.** Does a draft in `bot/` sound shaming, preachy or too long? Suggest warmer wording.
- **Evidence.** Corrections to evidence levels must cite a peer-reviewed source, with a DOI if possible.
- **Safety.** Crisis-line corrections, red-team prompts, accessibility.
- **Credit.** Help us find the chart's original author.

## Ground rules
1. **Don't invent chart content.** Chart text in `flowchart.json` is quoted verbatim, including "Accomodate" [sic]. Additions go in `bot_tip` or options with `"interpretive": true`, and must be labelled as not chart text.
2. **Don't overstate evidence.** Use the levels defined in `data/flowchart.json`.
3. **Don't claim platform features we haven't verified.** Grok Bot facts in `docs/research-grok-bot.md` need a source link.
4. **No personal health information** in issues, PRs or test fixtures.
5. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Development
You need Python 3.9 or newer. There are no runtime dependencies.

```bash
python -m unittest -v          # run all tests
python -m get_unstuck validate # graph integrity check
pip install jsonschema         # optional: enables the JSON Schema test (CI installs it)
```

When you change `data/flowchart.json`:
- keep `python -m get_unstuck validate` passing (all nodes reachable, no dead ends)
- update or add tests in `tests/test_flowchart.py` if a routing changes
- if a node's `flow` changes, update the matching `bot/skills/*/SKILL.md` `flowchart_nodes`
- bump `meta.version` and add a `CHANGELOG.md` entry

## Pull requests
- Keep PRs small and focused, and describe *why* the change helps.
- Make sure CI is green.
- By contributing, you agree your contributions are licensed under the MIT license. The chart image is excluded; see [LICENSE](LICENSE).
