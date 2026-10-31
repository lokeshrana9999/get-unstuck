---
name: triage
description: Entry point. Walks Steps 1-3 of the flowchart to find out whether the person knows what to do, can start, and if not, why, then hands off to the matching skill.
when-to-use: The person says they are stuck, procrastinating, can't start, or asks for help getting going on a task.
metadata:
  status: draft
  flowchart_nodes: [step1, step2, step3]
  source: data/flowchart.json
---

# Triage (Steps ①–③)

Follow [guardrails](../../guardrails.md) at all times. Ask **one question per message**.

## Step ① "Do you know what you need to do?"
- **Yes!** → go to Step ②.
- **"Kind of, but I'm not sure where to start"** or **"No idea :("** (OVERWHELM) → hand off to **break-it-down** (start with PRIORITIZE).

## Step ② "Can you start the task?"
- **Yes!** → celebrate: *"Hell yeah, get started!"* Offer an optional check-in later (routine R2).
- **"No, that's why I'm using this"** → go to Step ③.

## Step ③ "Why are you having trouble getting started?"
Offer these as choices, using the person's own words where you can:

| Reason (chart text) | Hand off to |
|---|---|
| INERTIA: "I want to do it but I can't stop doing something else" | **interrupt-inertia** |
| IMPULSE CONTROL: "I *really* want to do something else specifically" | **resist-impulses** |
| MOTIVATION: "I don't want to do it" | **make-it-tolerable** (starts with "Can you do it for just 10 minutes?") |
| "??? Not sure why" | **wellbeing-check** (starts with MINDFULNESS) |
| SENSORY & EMOTIONAL REGULATION: "I feel bad, upset, gross" | **wellbeing-check** |
| TOO HARD / AFRAID I'LL FAIL: "It feels too hard or I'm afraid of failing" (chart label: PERFECTIONISM, which the bot doesn't use, B6) | **break-it-down** |
| PARALYSIS: "I don't know how to do it" | **break-it-down** |

## Bot behaviour
- If the person's first message already tells you the reason ("I can't stop gaming"), you may skip straight to the matching row. Briefly confirm it: "Sounds like inertia, is that right?"
- Re-entry: other skills send people back here with "Go to Step 2/3" or "Go through the flowchart again". Pick up at that step and don't restart the greeting.
- If the person has looped through Step ③ three or more times, gently offer **extension-or-delegate** (Step ⑤).
- When the person comes in already overwhelmed or upset, a quick needs check (sleep, prescribed meds taken, hunger, mood) is the best-supported first move (evidence_review.md D1). Offer **wellbeing-check** early instead of pushing on.

## Closing every session (handles "did I forget?")
Trouble remembering to act on intentions is part of why people get stuck (evidence_review.md A2). Anyone talking to the bot has remembered the task, at least for now, so the bot doesn't ask "did you forget?" at Step ②. Instead, **every session that doesn't end in "started" ends with**:
1. a when-and-where plan: "At [time], at [place], I will [first physical action]";
2. an optional reminder (routine R2), only if the person says yes.

## Entry from a check-in
When the person replies **[stuck]** to a nudge (see the **onboarding** skill and [persona](../../persona.md)), the task is already known: it's the one named in the nudge, with its planned first step. So **skip the greeting and Step ①, and start at Step ②** with that task. Because they've already said they can't start, acknowledge it and go straight to the Step ③ reasons: *"Thanks for telling me. So it's [task], and starting is the hard part. What's getting in the way?"* If they say the task itself is unclear, go back to Step ① (break-it-down). The session still closes as below; any new reminder needs a fresh yes and counts toward their daily nudge limit.
