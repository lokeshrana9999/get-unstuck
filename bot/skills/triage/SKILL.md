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
| PERFECTIONISM: "It feels too hard or I'm afraid of failing" | **break-it-down** |
| PARALYSIS: "I don't know how to do it" | **break-it-down** |

## Bot behaviour
- If the person's first message already tells you the reason ("I can't stop gaming"), you may skip straight to the matching row. Briefly confirm it: "Sounds like inertia, is that right?"
- Re-entry: other skills send people back here with "Go to Step 2/3" or "Go through the flowchart again". Pick up at that step and don't restart the greeting.
- If the person has looped through Step ③ three or more times, gently offer **extension-or-delegate** (Step ⑤).
