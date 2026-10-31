# Get Unstuck: Task Starter for ADHD & Executive Dysfunction

[![tests](https://github.com/lokeshrana9999/get-unstuck/actions/workflows/tests.yml/badge.svg)](https://github.com/lokeshrana9999/get-unstuck/actions/workflows/tests.yml)
![status: planning](https://img.shields.io/badge/status-planning-yellow)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE)

**Get Unstuck** is a planned [Grok Bot](https://docs.x.ai/grok-bot): a warm, encouraging **productivity companion designed with ADHD in mind**. It helps you plan what you want to get done, sends a few gentle nudges at times you choose, and helps you *start* when executive dysfunction has you stuck. It doesn't assume you have ADHD; it's for anyone who finds starting, keeping track or finishing hard.

> **Status: planning.** This repo holds the plan, the data model, draft bot content and a small command-line prototype. **The Grok Bot hasn't been created yet.** See [docs/ACTION-PLAN.md](docs/ACTION-PLAN.md).
>
> **Pivot (2026-10-31):** the project grew from a "get unstuck when you're stuck" helper into a productivity bot with onboarding and proactive nudges ([docs/PIVOT.md](docs/PIVOT.md)). **The name is under review** ([docs/naming.md](docs/naming.md)); nothing has been renamed.

Honestly put, Get Unstuck is **a productivity aid and structured coaching flow built on reasonable, general-population principles**. Almost none of it has been tested in adults with ADHD. It is not an "evidence-based ADHD tool", and it is not a treatment.

## How it works

1. **Onboarding.** Three quick questions: one thing you want to get done this week, when reminders suit you (and when to stay quiet), and how many nudges you want and in what tone. Before the first session ends you have a small plan: "After lunch, at my desk, I will open the folder." The bot shows you each reminder it would set up, with a sample message, and creates it only if you say yes.
2. **Nudges.** At most **3 a day by default** (an optional morning plan, a start nudge for your task, an optional end-of-day review). You can choose 0 to 5; 5 is the ceiling. Nothing is sent during quiet hours (9 PM to 8 AM unless you change them). Each nudge names your task and its first step, and offers `started`, `snooze`, `stuck` or `skip`. An ignored nudge is never followed up, and there's no escalation. Say "stop", "pause", "fewer" or "change time" and it takes effect straight away.
3. **Stuck?** Reply `stuck` and the bot walks the flowchart with you, one small question at a time, to find out **why** you're stuck. Then it offers a few small things to try, best-supported first. If today isn't the day, it helps you reschedule, ask for help, do a "good enough" version, or let it go kindly.
4. **Focus sessions (optional).** Ask for a 25- or 50-minute body-doubling-style session: say what you're aiming for, and report back at the end. It's popular but hasn't been tested in trials, and the bot says so.
5. **End-of-day review (optional).** What went well comes first, then anything to carry over. Wins go in a wins log. There are no streaks to break and no "you missed" messages.

Some practical points:
- The bot's chat is the guaranteed channel. Push notifications are best-effort.
- Every scheduled check-in uses some of your weekly Grok Bot usage, which is one reason the default is small.
- Memory (opt-in) is the default store. A Google Sheet log is optional, for people who want history.
- It never sends messages, edits your calendar or files, or contacts anyone without an explicit "yes" for that action. Calendar changes are only ever proposed.

## What the evidence says

The full review, with sources and verification notes, is in [docs/research-adhd-productivity.md](docs/research-adhd-productivity.md). The tips inside the flowchart are checked in [`source/evidence_review.md`](source/evidence_review.md).

| Idea the bot uses | Best evidence found | In adults with ADHD |
|---|---|---|
| If-then plans ("At [time], at [place], I will…") | **Strong** in the general population (d = 0.65) | **None**: only lab tasks with children |
| Reminders | **Moderate** in general adults; modest effects that fade over weeks | **None**: no reminder trials found |
| Keeping notifications few (about 3 a day) | **Weak/moderate**: a single trial; notifications cost attention even when ignored (moderate) | Not tested |
| Body doubling / virtual coworking | **None** (no peer-reviewed outcome data) | **None** |
| Timers and time aids | Time-perception difficulties in ADHD are **strong** (mostly young people); evidence that aids help is **weak** (one small child trial) | **None** |
| ADHD coaching and apps | **Weak**: mostly uncontrolled studies of students | **Weak**: the best digital trial (n = 57) included a human coach |
| People stop using apps fast | **Strong**: 3.3% median 30-day retention for mental-health apps | Not studied separately; assumed to apply |

So the bot is designed for coming back rather than for streaks, keeps nudges few, and tells you honestly which tips are well supported and which are popular hacks.

## Adapted from a community flowchart

Get Unstuck is **adapted from** the flowchart **"Getting Started with Executive Dysfunction"** ([`source/chart.png`](source/chart.png)). It keeps the chart's structure and tone. It rewords or drops the tips that the evidence review found misleading or unsafe, for example "DIY dopamine" becomes a "quick reset", the snack tip is dropped, and the throw-your-phone tip is replaced with a timer across the room. `data/flowchart.json` keeps the chart's own text unchanged, and every change sits beside it as a separate "bot overlay", so each departure from the chart is visible. See [docs/verdict.md](docs/verdict.md) and [docs/verdict-response.md](docs/verdict-response.md).

**Original author: unknown.** The chart carries no signature, and web searches haven't found its creator. If you made this chart or know who did, please [open an issue](../../issues/new?template=credit.yml). We'd love to credit you properly and ask your permission.

What's in `source/`:
- `breakdown_v2.md`: a faithful text breakdown of every box and arrow.
- `review_v2.md` and `fixes_log.md`: an independent fidelity review and the fixes made after it.
- `evidence_review.md`: each strategy checked against peer-reviewed research.

The bot uses the evidence review to stay honest. Some tips are well supported, for example breaking a task into a concrete first step, or removing temptations. Some are untested folk wisdom, like body doubling or the "Scientist Hat". A few rest on myths, such as snacks boosting willpower or "dopamine top-ups".

## Disclaimer

**Get Unstuck is not medical, psychological or psychiatric advice, diagnosis or treatment.** It's a self-help companion, not a treatment or a therapist. If starting things is hard most of the time, talk to a qualified professional. Medication and structured CBT/DBT programmes have far more evidence behind them than any single tip.

**If you are in crisis or thinking about harming yourself, please reach out now:**
- India: **Tele-MANAS 14416** (or 1-800-891-4416), free, 24/7
- US: call or text **988**
- UK/Ireland: **Samaritans 116 123**
- Anywhere else: [findahelpline.com](https://findahelpline.com)
- Immediate danger: your local emergency number

## Quickstart (CLI prototype)

The prototype walks the **stuck-flow only**: the flowchart you reach when you reply "stuck". Onboarding, nudges, focus sessions and reviews exist only as drafts in `bot/` and aren't in the CLI. It needs **Python 3.9+** and nothing else.

```bash
git clone https://github.com/lokeshrana9999/get-unstuck.git
cd get-unstuck
python -m get_unstuck              # walk the original chart from Step 1
python -m get_unstuck --bot        # walk the adapted bot flow (honesty tags, reworded tips)
python -m get_unstuck --evidence   # show evidence levels (and the bot version) next to each tip
python -m get_unstuck validate     # check data/flowchart.json integrity
python3 -m unittest discover -s tests   # run the tests
```

The prototype's crisis check is simple keyword matching on typed English phrases. **It is not a safety system.**

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
  guardrails.md          Not medical advice, crisis lines, no actions without "yes",
                         §8 proactive messaging (cap, quiet hours, opt-out, no guilt)
  routines.md            Opt-in nudges: morning plan, start nudges, check-ins, focus
                         sessions, end-of-day and weekly reviews, snooze, opt-out
  skills/onboarding/     First-session setup: goal, reminder times, quiet hours,
                         first if-then plan, routine previews
  skills/<flow>/SKILL.md One skill per flowchart flow: triage, break-it-down,
                         interrupt-inertia, resist-impulses, make-it-tolerable,
                         wellbeing-check, extension-or-delegate
data/
  flowchart.json         Nodes, branches, strategies, evidence levels, bot overlays
  flowchart.schema.json  JSON Schema (draft 2020-12)
get_unstuck/             Dependency-free CLI prototype (engine, CLI, safety)
tests/                   unittest suite (data integrity, fidelity, CLI, drafts)
docs/
  ACTION-PLAN.md         Phased plan to build the bot (owners, gates, risks)
  PIVOT.md               The 2026-10-31 scope change to a productivity bot
  action-plan/           The four planning parts it was merged from
  verdict.md             Independent verdict on the chart and the bot idea
  verdict-response.md    Where we agree/disagree and what changed
  PLAN.md                Original milestones (superseded by ACTION-PLAN.md)
  research-grok-bot.md   What Grok Bot and Grok Build can actually do, with sources
  research-adhd-productivity.md  Evidence on reminders, if-then plans, body doubling,
                         notification load and drop-off; existing apps; scheduling limits
  naming.md              Whether the name still fits, with 3 options (undecided)
  sheet-design.md        Optional Google Sheet log (goals, tasks, check-ins, wins)
source/                  Flowchart image and its reviewed breakdown and evidence check
```

## Contributing

Contributions are welcome, especially fidelity checks against the chart, tone reviews, translations, and input from people with lived ADHD experience or clinicians. See [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

- **Code and original docs:** [MIT](LICENSE) © 2026 Lokesh Rana and contributors.
- **The flowchart image** (`source/chart.png`) and its content belong to **its original creator (author unknown)**. They are **not** covered by the MIT license. They're included for reference and attribution only. If you are the creator and want changes or removal, please open an issue.
- Research cited in `source/evidence_review.md` belongs to its respective authors.

"Grok" and "Grok Bot" are products of xAI. This project isn't affiliated with or endorsed by xAI.
