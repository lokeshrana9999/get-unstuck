# Get Unstuck: Task Starter for ADHD & Executive Dysfunction

[![tests](https://github.com/lokeshrana9999/get-unstuck/actions/workflows/tests.yml/badge.svg)](https://github.com/lokeshrana9999/get-unstuck/actions/workflows/tests.yml)
![status: planning](https://img.shields.io/badge/status-planning-yellow)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE)

**Get Unstuck** is a planned [Grok Bot](https://docs.x.ai/grok-bot): a warm, encouraging companion that helps you *start* a task when executive dysfunction has you stuck. It works for ADHD-style inertia, overwhelm, paralysis, perfectionism, impulse pulls, low motivation, or just feeling rough.

It asks one small question at a time to find out **why** you're stuck. Then it offers a few small things to try. If today isn't the day, it helps you reschedule, ask for help, do a "good enough" version, or let it go kindly.

> **Status: planning.** This repo holds the plan, the data model, draft bot content and a small command-line prototype. **The Grok Bot hasn't been created yet.** See [docs/PLAN.md](docs/PLAN.md).

## Based on a community flowchart

Get Unstuck follows the flowchart **"Getting Started with Executive Dysfunction"** ([`source/chart.png`](source/chart.png)).

**Original author: unknown.** The chart carries no signature, and web searches haven't found its creator. If you made this chart or know who did, please [open an issue](../../issues/new?template=credit.yml). We'd love to credit you properly and ask your permission.

What's in `source/`:
- `breakdown_v2.md`: a faithful text breakdown of every box and arrow.
- `review_v2.md` and `fixes_log.md`: an independent fidelity review and the fixes made after it.
- `evidence_review.md`: each strategy checked against peer-reviewed research.

The bot uses the evidence review to stay honest. Some tips are well supported, for example breaking a task into a concrete first step, or removing temptations. Some are untested folk wisdom, like body doubling or the "Scientist Hat". A few rest on myths, such as snacks boosting willpower or "dopamine top-ups".

## Disclaimer

**Get Unstuck is not medical, psychological or psychiatric advice, diagnosis or treatment.** It's a self-help prompt. If starting things is hard most of the time, talk to a qualified professional. Medication and structured CBT/DBT programmes have far more evidence behind them than any single tip.

**If you are in crisis or thinking about harming yourself, please reach out now:**
- India: **Tele-MANAS 14416** (or 1-800-891-4416), free, 24/7
- US: call or text **988**
- UK/Ireland: **Samaritans 116 123**
- Anywhere else: [findahelpline.com](https://findahelpline.com)
- Immediate danger: your local emergency number

## Quickstart (CLI prototype)

The prototype walks the flowchart in your terminal. It needs **Python 3.9+** and nothing else.

```bash
git clone https://github.com/lokeshrana9999/get-unstuck.git
cd get-unstuck
python -m get_unstuck              # walk the chart from Step 1
python -m get_unstuck --evidence   # show evidence levels next to each tip
python -m get_unstuck validate     # check data/flowchart.json integrity
python -m unittest                 # run the tests
```

In the walker:
- type a number to choose
- `b` goes back
- `q` quits
- `?` shows help

Options marked `*` aren't chart text.

## Repository layout

```
bot/                     Draft Grok Bot content (not yet loaded into the app)
  persona.md             Name, label, description, first-message setup prompt
  guardrails.md          Not medical advice, crisis lines, no actions without "yes"
  routines.md            Opt-in nudges (morning "one next thing", check-ins, ...)
  skills/<flow>/SKILL.md One skill per flow: triage, break-it-down, interrupt-inertia,
                         resist-impulses, make-it-tolerable, wellbeing-check,
                         extension-or-delegate
data/
  flowchart.json         Nodes, branches, strategies and evidence levels
  flowchart.schema.json  JSON Schema (draft 2020-12)
get_unstuck/             Dependency-free CLI prototype (engine, CLI, safety)
tests/                   unittest suite (data integrity, fidelity, CLI, drafts)
docs/
  PLAN.md                Milestones toward the bot
  research-grok-bot.md   What Grok Bot and Grok Build can actually do, with sources
  sheet-design.md        Optional Google Sheet log
source/                  Flowchart image and its reviewed breakdown and evidence check
```

## Contributing

Contributions are welcome, especially fidelity checks against the chart, tone reviews, translations, and input from people with lived ADHD experience or clinicians. See [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

- **Code and original docs:** [MIT](LICENSE) © 2026 Lokesh Rana and contributors.
- **The flowchart image** (`source/chart.png`) and its content belong to **its original creator (author unknown)**. They are **not** covered by the MIT license. They're included for reference and attribution only. If you are the creator and want changes or removal, please open an issue.
- Research cited in `source/evidence_review.md` belongs to its respective authors.

"Grok" and "Grok Bot" are products of xAI. This project isn't affiliated with or endorsed by xAI.
