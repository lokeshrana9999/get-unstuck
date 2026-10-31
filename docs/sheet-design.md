# Google Sheet design (optional, opt-in)

Grok Bot's Google Sheets app can **read spreadsheets the connected account can open and edit cells**, per the [docs](https://docs.x.ai/grok-bot/computer-and-apps). We haven't confirmed whether it appends rows natively (open question 5 in [research-grok-bot.md](research-grok-bot.md#4-open-questions)). The design below works either way: if append isn't available, the Bot reads column A of the tab and writes to the **first empty row**.

This version is for the ADHD productivity Bot ([PIVOT.md](PIVOT.md)): goals, tasks, check-ins from [routines](../bot/routines.md), body-doubling sessions and wins. The flowchart walk that happens when someone is "stuck" is recorded inside the check-in it came from.

**Memory vs Sheet**
- **Memory is the default store** (opt-in: "Want me to remember this?"). It's enough for every routine, including simple weekly counts.
- **The Sheet is optional, for people who want history.** It's the only store the person can inspect, edit and delete row by row. It makes the weekly reflection (R4) and the clinician nudge (R5) more reliable.
- **No health details go in either.** No diagnoses, medications, symptoms or moods.

**Principles**
- **Off by default.** The person opts in once and can say "stop logging" at any time ([guardrails §3](../bot/guardrails.md#3-no-outbound-actions-without-an-explicit-yes)).
- **Store as little as possible.** Task names, times, responses and outcomes only.
- **The person owns it.** The Sheet lives in their own Drive. The Bot never shares it.
- **Counts only go up.** No streaks, no failure counts (see [Streaks without shame](#streaks-without-shame)).

Spreadsheet name: `Get Unstuck log`. All times are local, in the timezone from `Settings`.

---

## Tab 1: `Goals`

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `goal_id` | text, `G-NN` | `G-01` |
| B | `goal` | short free text (person's words; may be sensitive) | `Keep on top of flat admin` |
| C | `why` | optional free text | `less stress on Sundays` |
| D | `target_date` | date or empty | `2026-12-31` |
| E | `status` | `active` · `paused` · `done` · `let_go` | `active` |
| F | `created_at` | datetime | `2026-10-31 10:05` |

`let_go` is a neutral status, not a failure.

## Tab 2: `Tasks` (one-off and recurring)

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `task_id` | text, `T-NNN` | `T-004` |
| B | `goal_id` | from `Goals`, or empty | `G-01` |
| C | `task` | short free text (may be sensitive) | `Email landlord` |
| D | `first_step` | the smallest physical action | `open Gmail and type the subject line` |
| E | `if_then_cue` | the situation in the if-then plan | `when I sit back down after lunch` |
| F | `recurrence` | `none`, or plain words as Grok Bot expects | `every Monday and Thursday` |
| G | `slot_time` | the start-nudge time (R2), `HH:MM` | `13:55` |
| H | `deadline` | date/datetime or empty | `2026-11-07` |
| I | `estimate_min` | minutes, optional | `15` |
| J | `routine_id` | the R2 slot that nudges it, or empty | `R2-1355` |
| K | `status` | `planned` · `active` · `paused` · `done` · `let_go` | `active` |
| L | `created_at` | datetime | `2026-10-31 10:07` |

Column D + E together form the if-then plan: "If {if_then_cue}, then I will {first_step}." Plans made by the flowchart's "Set another day/time" ending (`reschedule`) become rows here.

## Tab 3: `Check-ins` (one row per nudge or response)

One row per scheduled contact or requested follow-up, and one row when the person opens the chat stuck on their own (`nudge_type` = `self`).

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `checkin_id` | text, `C-YYYYMMDD-HHMM` | `C-20261031-1355` |
| B | `nudge_type` | `morning_plan` (R1) · `start_nudge` (R2) · `midday` (R3) · `session` (R6) · `eod_review` (R7) · `weekly` (R4) · `welcome_back` (R8) · `self` | `start_nudge` |
| C | `sent_at` | datetime (empty for `self`) | `2026-10-31 13:55` |
| D | `task_id` | from `Tasks`, or empty | `T-004` |
| E | `response` | `started` · `snoozed` · `stuck` · `skipped` · `none` | `stuck` |
| F | `responded_at` | datetime or empty | `2026-10-31 14:02` |
| G | `snooze_count` | 0–3 (3 = reached "reschedule or let it go?") | `0` |
| H | `entry_reason` | if stuck: `knows` · `overwhelm` · `inertia` · `impulse` · `motivation` · `unsure` · `wellbeing` · `perfectionism` · `paralysis` | `inertia` |
| I | `path` | if stuck: node ids from `data/flowchart.json`, separated by `>` | `step1>step2>step3>interrupt_inertia>hell_yeah` |
| J | `strategies_tried` | if stuck: strategy ids, comma-separated | `content_blocker,stop_five_minutes` |
| K | `strategy_that_helped` | one strategy id or empty | `content_blocker` |
| L | `outcome` | if stuck: `start` · `reschedule` · `delegate` · `partial` · `accept` · `push_through` · `paused` | `start` |
| M | `est_min` | optional, copied from `Tasks.estimate_min` | `15` |
| N | `actual_min` | optional, from the end-of-day review | `25` |
| O | `note` | optional free text from the person | `phone in kitchen worked` |

`none` means the nudge got no reply. It's used only for the "3 ignored in a row → pause that type" rule and is never shown to the person as a count.

## Tab 4: `Sessions` (body doubling, R6)

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `session_id` | text, `S-YYYYMMDD-HHMM` | `S-20261031-1500` |
| B | `started_at` | datetime | `2026-10-31 15:00` |
| C | `length_min` | `25` · `50` | `25` |
| D | `task_id` | from `Tasks`, or empty | `T-004` |
| E | `session_goal` | the one line stated at the start | `draft the email and send it` |
| F | `halfway_check` | `yes` · `no` | `no` |
| G | `result` | `done` · `part_done` · `got_stuck` · `no_report` | `done` |
| H | `round` | 1 or 2 (in a row) | `1` |
| I | `note` | optional free text | `easier than expected` |

`got_stuck` can open triage; the walk is then logged as a `Check-ins` row with `nudge_type` = `session`.

## Tab 5: `Wins` (wins log)

| Col | Header | Type / allowed values | Example |
|---|---|---|---|
| A | `win_id` | text, `W-NNNN` | `W-0012` |
| B | `date` | date | `2026-10-31` |
| C | `win` | short free text, the person's words | `sent the landlord email` |
| D | `source` | `started` · `session` · `eod_review` · `self` · `triage` | `eod_review` |
| E | `task_id` | from `Tasks`, or empty | `T-004` |

Anything counts as a win: starting, a partial job, deciding to let something go, or resting on purpose.

## Tab 6: `Settings` (key / value)

Two columns, `key` and `value`. **No health data.**

| Key | Allowed values | Default |
|---|---|---|
| `timezone` | IANA zone | from Grok Bot Settings, confirmed in onboarding |
| `quiet_start` / `quiet_end` | `HH:MM` | `21:00` / `08:00` |
| `daily_cap` | 0–5 | `3` |
| `morning_plan` | `off` or `HH:MM` | `off` until a yes |
| `start_slots` | comma-separated `HH:MM` | empty until a yes |
| `midday` | `off` or `HH:MM` | `off` |
| `eod_review` | `off` or `HH:MM` | `off` until a yes |
| `weekly` | `off` or day + `HH:MM` | `off` |
| `clinician_nudge` | `off` · `on` · `never` | `off` |
| `session_default_min` | `25` · `50` | `25` |
| `session_halfway` | `on` · `off` | `off` |
| `track_estimates` | `on` · `off` | `off` |
| `tone` | `gentle` · `upbeat` · `minimal` (as asked in the onboarding skill) | `gentle` |
| `logging` | `batch` (at end-of-day review) · `as_i_go` · `off` | `batch` |
| `paused_types` | comma-separated nudge types paused by the 3-ignored rule or by the person | empty |
| `last_reply_at` | datetime | — |

Memory holds the same settings when the Sheet is off. If they differ, the Bot asks which to keep.

## Tab 7: `Summary` (formulas only)

The Bot reads this tab and never writes to it. See [Formula drafts](#formula-drafts-untested).

---

## Streaks without shame

- **Counts only go up.** The Sheet and the Bot show things like "days you showed up this month", "tasks started" (this week, this month, all time), "wins logged" and "sessions done". A day "showed up" means any reply other than `none`, any session, or any win.
- **No resets.** There's no chain to break. A gap of a week changes nothing in the all-time counts.
- **No missed-day counts.** `none` responses exist only to drive the ignored-nudge pause rule. They're never summed, shown or mentioned.
- **No red marks.** Don't use conditional formatting that colours gaps, skips, `let_go` or overdue items red. If colour is used at all, use it only to highlight wins.
- **No downward comparisons.** "Fewer than last week" is never shown.
- **The weekly reflection (R4) shows wins first**: wins, starts and the most helpful strategy, before any question about changes.
- Coming back after a gap takes one message and gets no summary of what was missed ([routines R8](../bot/routines.md#r8-gap--welcome-back)).

The research found no peer-reviewed study of "streak shame"; this is a design choice grounded in steep app drop-off (Baumel 2019) and the aim of making it cheap to return ([research Part B §3](research-adhd-productivity.md#3-lessons-for-our-bot)).

---

## Bot write protocol

1. **Opt-in once.** Show what logging looks like, with one sample row per tab that will be used, and ask: "Want me to keep a log in your own Google Sheet? I'd write rows like these. [yes] [no]". Only an explicit **yes** counts.
2. **Preview + yes for rows with the person's own words** (`Goals`, `Tasks`, `Wins`, notes): "Add this task? *Email landlord · first step: open Gmail and type the subject line · when I sit back down after lunch*. [yes] [change] [no]".
3. **Check-in and session rows are batched by default** (`logging` = `batch`). The Bot holds the day's rows in memory and shows them as one short preview at the end-of-day review (R7), then writes after one **yes**. This keeps writes in a live conversation, so routine-originated approvals (which expire after about 30 minutes) don't get in the way. With `as_i_go`, the one-time opt-in covers check-in rows and the Bot says "logged" in a few words. If there's no review that day, the batch is offered at the next live chat, or dropped after 2 days.
4. **"No"** skips that row or batch. **"Stop logging"** sets `logging` to `off` at once, with a one-line confirmation. Memory keeps working.
5. **Never edit or delete past rows** unless the person asks for it explicitly and specifically. "Delete my log" means: show what will be deleted, then delete only after a yes.
6. **View-only or unreachable Sheet:** say so once ("I can't write to the Sheet right now, so I'll keep today's notes in memory"), carry on, and don't retry within the same day. A file shared as Viewer stays view-only per the docs.
7. **Append unverified:** read column A of the target tab, write to the first empty row, and re-read to check the row landed. If two writes might collide, write one at a time.

## Privacy

- **Minimal data.** Task names, times, responses and outcomes. No diagnoses, medications, symptoms or moods, even if the person mentions them in chat (guardrails §6).
- **Task names may be sensitive** ("call the debt advisor"). The opt-in tells the person this, and suggests a short label if they'd rather ("Call D.").
- **The person owns the Sheet.** It lives in their Drive. The Bot never shares it, links it elsewhere, or copies it to another file.
- **Templates and shared Bots never include anyone's Sheet or history.** Grok Bot templates exclude history by design.
- Deleting the Sheet, or saying "stop logging" and "forget my log", removes the history. Memory can be cleared on request too.

## Mapping to `data/flowchart.json`

| Sheet field | Flowchart source |
|---|---|
| `Check-ins.entry_reason` | Option chosen at `step1` (`overwhelm` → `prioritize`) or `step3`: `inertia` → `interrupt_inertia`, `impulse` → `resist_impulses`, `motivation` → `ten_minutes`, `unsure` → `mindfulness`, `wellbeing` → `wellbeing`, `perfectionism` / `paralysis` → `break_it_down`. `knows` = went straight from `step2` "Yes!" to `hell_yeah`. |
| `Check-ins.path` | Node ids in `nodes`, starting at `start` (`step1`), e.g. `step2`, `step4`, `step4_tried`, `step5`, `delegate_q`, `partial_q`, `worth_q`. |
| `Check-ins.strategies_tried`, `strategy_that_helped` | Keys in `strategies`, e.g. `smallest_step`, `goblin_tools`, `ten_minutes`, `content_blocker`, `body_double`, `recurring_alarm`, `reschedule`. |
| `Check-ins.outcome` | `outcome` of terminal nodes: `hell_yeah` → `start`, `reschedule` → `reschedule`, `ask_for_help` → `delegate`, `half_ass` → `partial`, `radical_acceptance` → `accept`, `push_through` → `push_through`. `paused` = the person stopped partway. |
| `Tasks` row from a stuck walk | Created when `outcome` = `reschedule`, using the strategy's if-then wording ("At [time], at [place], I will [first physical action]"). |
| `Sessions` | The `body_double` strategy (honesty tag `reasonable_untested`). |
| R5 input | `accept` + `push_through` outcomes over the last 4 weeks (Step ④/⑤ endings). |

## Formula drafts (untested)

> **UNTESTED.** None of these formulas have been run in Google Sheets yet. They assume headers in row 1 and data from row 2, and Sheets functions (`FILTER`, `COUNTUNIQUE`, `ARRAYFORMULA`). Test them on a copy before relying on them (M4 work in [PLAN.md](PLAN.md)). They count up only; none counts gaps or `none` responses for display.

| Cell | Formula (untested) | Meaning |
|---|---|---|
| B2 | `=IFERROR(COUNTUNIQUE(FILTER(INT('Check-ins'!F2:F),'Check-ins'!E2:E<>"none",'Check-ins'!F2:F<>"",TEXT('Check-ins'!F2:F,"yyyy-mm")=TEXT(TODAY(),"yyyy-mm"))),0)` | Days you replied this month (input to "days you showed up") |
| B3 | `=IFERROR(COUNTUNIQUE({FILTER(INT('Check-ins'!F2:F),'Check-ins'!E2:E<>"none",'Check-ins'!F2:F<>"");FILTER(INT(Sessions!B2:B),Sessions!B2:B<>"");FILTER(Wins!B2:B,Wins!B2:B<>"")}),0)` | Days you showed up, all time (union of replies, sessions and wins) |
| B4 | `=COUNTIF('Check-ins'!E2:E,"started")+COUNTIFS('Check-ins'!E2:E,"stuck",'Check-ins'!L2:L,"start")` | Tasks started, all time |
| B5 | `=COUNTIFS('Check-ins'!E2:E,"started",'Check-ins'!F2:F,">="&(TODAY()-WEEKDAY(TODAY(),2)+1))+COUNTIFS('Check-ins'!E2:E,"stuck",'Check-ins'!L2:L,"start",'Check-ins'!F2:F,">="&(TODAY()-WEEKDAY(TODAY(),2)+1))` | Tasks started this week (Monday start) |
| B6 | `=COUNTA(Wins!A2:A)` | Wins logged, all time |
| B7 | `=COUNTIFS(Sessions!G2:G,"done")+COUNTIFS(Sessions!G2:G,"part_done")` | Sessions with something done |
| B8 | `=IFERROR(INDEX(FILTER('Check-ins'!K2:K,'Check-ins'!K2:K<>""),MODE(MATCH(FILTER('Check-ins'!K2:K,'Check-ins'!K2:K<>""),FILTER('Check-ins'!K2:K,'Check-ins'!K2:K<>""),0))),"")` | Most helpful strategy |
| B9 | `=IFERROR(INDEX(FILTER('Check-ins'!H2:H,'Check-ins'!H2:H<>""),MODE(MATCH(FILTER('Check-ins'!H2:H,'Check-ins'!H2:H<>""),FILTER('Check-ins'!H2:H,'Check-ins'!H2:H<>""),0))),"")` | Most common reason for getting stuck |
| B10 | `=IFERROR(MEDIAN(FILTER('Check-ins'!N2:N/'Check-ins'!M2:M,'Check-ins'!M2:M>0,'Check-ins'!N2:N<>"")),"")` | Typical actual ÷ estimate (only if `track_estimates` is on; shown as "tasks tend to take about 1.5× your guess", never as a score) |
| B11 | `=COUNTIFS('Check-ins'!F2:F,">="&TODAY()-28,'Check-ins'!L2:L,"accept")+COUNTIFS('Check-ins'!F2:F,">="&TODAY()-28,'Check-ins'!L2:L,"push_through")` | Step ④/⑤ endings in the last 4 weeks (input to R5; never shown as a count) |
| B12 | `=COUNTIFS('Check-ins'!F2:F,">="&TODAY()-28,'Check-ins'!E2:E,"stuck")` | Stuck walks in the last 4 weeks (denominator for R5's "most") |

Known risks to check when testing: `INT` on empty or text cells inside `FILTER`; `MODE` on text needs the `MATCH` trick and fails on a single value in some versions; the array literal `{…;…}` in B3 needs matching column counts; division by an empty `est_min` in B10.

## Data validation (set up once)

- Dropdowns: `Goals.status`, `Tasks.status`, `Check-ins.nudge_type`, `response`, `entry_reason`, `outcome`, `Sessions.length_min`, `result`, `Wins.source`, using the values above.
- Protect the `Summary` tab (or use warning-only protection) so edits are less likely to break it.
- No conditional formatting that marks gaps, skips or `none` responses.
