# Google Sheet log design (optional, opt-in)

Grok Bot's Google Sheets app can **read spreadsheets the connected account can open and edit cells**, per the [docs](https://docs.x.ai/grok-bot/computer-and-apps). We haven't confirmed whether it appends rows natively. The design below works either way: the Bot writes to the first empty row.

**Principles**
- **Off by default.** The user opts in once and can say "stop logging" at any time ([guardrails §3](../bot/guardrails.md#3-no-outbound-actions-without-an-explicit-yes)).
- **Store as little as possible.** Keep task names and outcomes only. No diagnoses, medications or health details.
- **The user owns it.** The Sheet lives in the user's own Drive. The Bot never shares it.
- **Positive framing.** The log counts starts and things tried, never "failures".

Spreadsheet name: `Get Unstuck log`

---

## Tab 1: `Sessions` (one row per walk through the flowchart)

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `session_id` | text, `YYYYMMDD-HHMM` | `20261031-1415` |
| B | `started_at` | datetime (Sheet timezone) | `2026-10-31 14:15` |
| C | `task` | short free text (user's words; may be sensitive) | `Email landlord` |
| D | `entry_reason` | `knows` · `overwhelm` · `inertia` · `impulse` · `motivation` · `unsure` · `wellbeing` · `perfectionism` · `paralysis` | `inertia` |
| E | `path` | node ids separated by `>` (from `data/flowchart.json`) | `step1>step2>step3>interrupt_inertia>hell_yeah` |
| F | `strategies_tried` | strategy ids, comma-separated | `content_blocker,stop_five_minutes` |
| G | `strategy_that_helped` | one strategy id or empty | `content_blocker` |
| H | `outcome` | `start` · `reschedule` · `delegate` · `partial` · `accept` · `push_through` · `paused` | `start` |
| I | `ended_at` | datetime | `2026-10-31 14:22` |
| J | `note` | optional free text from the user | `phone in kitchen worked` |

Outcome values match the `outcome` of terminal nodes in `flowchart.json`. `paused` means the user stopped partway through.

## Tab 2: `Plans` (made from "Set another day/time")

| Col | Header | Example |
|---|---|---|
| A | `plan_id` | `P-20261031-01` |
| B | `session_id` | `20261031-1415` |
| C | `task` | `Email landlord` |
| D | `when` | `2026-11-01 10:00` |
| E | `where` | `desk` |
| F | `first_action` (if-then plan) | `open Gmail and type the subject line` |
| G | `reminder_routine` | `yes` / `no` (R2 in routines.md) |
| H | `status` | `planned` · `started` · `moved` · `dropped` |

## Tab 3: `Summary` (formulas only; the Bot reads this tab and never writes to it)

| Cell | Formula | Meaning |
|---|---|---|
| B2 | `=COUNTIF(Sessions!H:H,"start")` | Starts so far |
| B3 | `=COUNTA(Sessions!A2:A)` | Sessions so far |
| B4 | `=IFERROR(INDEX(Sessions!D2:D,MODE(MATCH(Sessions!D2:D,Sessions!D2:D,0))),"")` | Most common blocker |
| B5 | `=IFERROR(INDEX(Sessions!G2:G,MODE(MATCH(FILTER(Sessions!G2:G,Sessions!G2:G<>""),Sessions!G2:G,0))),"")` | Most helpful strategy |
| B6 | `=COUNTIFS(Sessions!B:B,">="&TODAY()-28,Sessions!H:H,"accept")+COUNTIFS(Sessions!B:B,">="&TODAY()-28,Sessions!H:H,"push_through")` | Hard endings in the last 4 weeks (input to routine R5) |

*The formulas are drafts and haven't been tested in Google Sheets yet. This is M4 work in [PLAN.md](PLAN.md).*

## Bot write protocol
1. When a session reaches an endpoint, show the row it would write, for example: "Log this? *Email landlord · inertia · content blocker helped · started*".
2. Write only after an explicit **yes**. "No" means skip this one. "Stop logging" turns logging off.
3. Never edit or delete past rows unless the user asks for it explicitly and specifically.
4. If the Sheet is view-only or can't be reached, say so and carry on without logging.

## Data validation (set up once)
- D, H (Sessions) and H (Plans): dropdown lists using the values above.
- Protect the `Summary` tab, or give it a warning-only protection, so edits are less likely to break it.
