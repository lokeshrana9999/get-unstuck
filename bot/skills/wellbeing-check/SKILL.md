---
name: wellbeing-check
description: Runs MINDFULNESS ("consider why") and WELLBEING (are physical and emotional needs met?) from the chart, then routes back to Step 2 or on to Step 4.
when-to-use: Person feels bad, upset or gross; doesn't know why they're stuck; or break-it-down/mindfulness still leaves them stuck.
metadata:
  status: draft
  flowchart_nodes: [mindfulness, great_job_step3, wellbeing, need_emotional, need_physical, dbt_skills, attend_need]
  source: data/flowchart.json
---

# Wellbeing check

**Safety first:** if anything in the person's answers suggests crisis, self-harm or danger, stop and follow [guardrails §2](../../guardrails.md#2-crisis-and-safety).

## A. MINDFULNESS (when the reason is "??? Not sure why")
Chart: "Take 5 minutes to sit quietly and consider why. How about now?" *(evidence: weak. This is really reflection, not formal mindfulness.)*
- Offer to keep quiet for 5 minutes. Optionally set a timer, with a yes.
- "I know why now!" → **"Great job! Go to Step 3."** → triage Step ③
- "I still don't know…" → section B.

## B. WELLBEING: "Are your physical & emotional needs met right now?"
*(evidence: moderate-strong overall. Sleep and prescribed medication are the best supported.)*
- "Needs are met!" → **extension-or-delegate** (Step ④). That's fine: it just means needs aren't the blocker.
- "No, I need something. It's…"
  - **EMOTIONAL:** social interaction, managing shame, fear, anxiety, etc
  - **PHYSICAL:** meds, food, rest sensory, water, movement, etc

Then ask: **"Can the need be met right now, even partially?"**
- **Yes!**
  - EMOTIONAL → "Use DBT skills- fit the facts, opposite action, loving kindness. Go to Step 2."
    - *Bot note:* the DBT skill is called "check the facts". Offer simple versions: "Does the feeling fit the facts of the situation?", "What would acting opposite to the urge look like?", "A kind phrase to yourself". DBT is a full multi-week programme, so mention a therapist if this comes up often.
  - PHYSICAL → "Attend to the need. Go to Step 2"
    - Meds: *only* "Have you taken any medication you're prescribed?" Never advise on medication.
    - Water: ⚠ unless on fluid restrictions. Food: if hungry. Rest, sensory: reduce noise or light. Movement: gentle and optional.
  - → triage Step ②
- "Need can't be met" → **extension-or-delegate** (Step ④)

## Tone
Be extra gentle here. Feeling bad is a legitimate reason to be stuck, not a character flaw.
