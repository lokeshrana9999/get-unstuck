# Routines (drafts)

> Grok Bot routines use plain-language schedules (at least 5 minutes apart, in the timezone set in Settings). They can also start from triggers such as email or webhook. See [research](../docs/research-grok-bot.md#routines). **Every routine is opt-in, off by default, and only sends a nudge.** No routine acts on the person's behalf (see [guardrails](guardrails.md#3-no-outbound-actions-without-an-explicit-yes)).

Each routine below gives a suggested schedule, the message the Bot sends, and what it may read or write.

---

## R1. Morning "one next thing"

- **Schedule:** "every weekday at 9:00 AM" (the user picks the time)
- **Message:** "Good morning! What's *one* thing you'd like to get started on today? Tell me, and we'll find the tiniest first step together. Or say 'skip' and enjoy your morning."
- **Flow:** starts the [triage](skills/triage/SKILL.md) skill if the user replies.
- **Reads/writes:** nothing. If logging is on, the Sheet gets a new row only after the user confirms a task.

## R2. Gentle check-in on a planned start

- **Schedule:** one-off, at the time the user set ("At 3 PM I'll open the report").
- **Message:** "Hey, it's 3 PM, the time you planned to open the report. Want to start now, push it 15 minutes, or talk through what's in the way?"
- **Why:** turns "set another day/time" into a concrete if-then plan (evidence_review.md H2, B3).
- **Reads/writes:** reads the plan from chat memory, or from the Sheet `Plans` tab if logging is on.

## R3. Inertia interrupt (user-requested timer)

- **Schedule:** one-off, 10–30 minutes after the user asks: "Nudge me in 20 minutes to stop scrolling."
- **Message:** "Time check! Do you want to be doing this right now? If not, stand up and take one step toward the task."
- **Source:** the chart's "Set a recurring alarm to check in: do you want to be doing this?"
- **Caution:** too many interruptions raise stress (F3). Default to a single nudge, and only repeat if the user asks.

## R4. Weekly reflection (optional, logging only)

- **Schedule:** "every Sunday at 6:00 PM"
- **Message:** a short, kind summary from the Sheet. For example: "This week you started 4 things. 'Break it down' helped most, and inertia was the most common blocker. Anything you want to try differently?"
- **Reads:** the Sheet `Sessions` tab. **Writes:** nothing.
- **Tone rule:** never count "failures". Count starts and things tried.

## R5. Clinician nudge (rare, opt-in)

- **Trigger:** the weekly routine sees that most sessions ended at Step ④ or ⑤ over the last 4 weeks.
- **Message:** "I've noticed a lot of weeks where starting has been really hard, even with lots of strategies. That's not a willpower problem. Talking to a doctor or ADHD specialist could help, and I can help you write down what you'd want to say."
- **Source:** evidence_review.md takeaway 10.

---

### Not planned

- Routines that message other people, post publicly, or edit files without a live "yes".
- High-frequency nagging, such as reminders every 5 minutes.
- Any routine that runs during the user's quiet hours. (Whether Grok Bot supports quiet hours is an open question.)
