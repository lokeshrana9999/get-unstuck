---
name: break-it-down
description: Handles overwhelm, perfectionism and paralysis with the chart's PRIORITIZE and BREAK IT DOWN boxes, ending in one small, measurable first step.
when-to-use: Person doesn't know what to do or where to start, feels the task is too hard, fears failing, or doesn't know how to do it.
metadata:
  status: draft
  flowchart_nodes: [prioritize, break_it_down, great_job_step2, revisit_step1]
  source: data/flowchart.json
---

# Break it down

## A. PRIORITIZE (used when coming from OVERWHELM at Step ①)
Bot wording (from the overlays):
- Use an important/urgent matrix *(reasonable but untested: the urgency bias it targets is real, but the matrix itself is untested)*
- Pick the 1 next thing, and say when and where you'll do it. *(reasonable but untested)*

Bot approach: ask for a brain-dump of everything on their mind. Help sort it quickly (urgent? important?). Then ask them to pick **one** next thing and attach a time and place to it.

Outcomes:
- "I know what to do now!" → **"Great job! Move to step 2."** → triage Step ② *(routing marked most likely in review_v2.md)*
- "OVERWHELM: I still don't know…" → section B.

## B. BREAK IT DOWN (from PRIORITIZE, TOO HARD / AFRAID I'LL FAIL, PARALYSIS, or "I'm worried I'll fail")
This is the bot's core job. Breaking a task into a specific first step with a when-and-where plan is the best-supported technique in the evidence review (B3, H2, takeaway 2). The bot does the breakdown itself; the chart's "Use Goblin Tools!" becomes "Let's break it down together right here. (If you like apps, Goblin Tools does this too.)"

Bot approach:
1. Ask what "done" looks like for the **first** piece, not the whole task.
2. Shrink it until it takes under 5 minutes and is observable ("open the doc and type the title"). *(well supported)*
3. **Required output:** an if-then plan, "At [time], at [place], I will [first physical action]." If they're starting now, use "Right now, at [place], I will …".
4. For "too hard / afraid I'll fail", offer the **good-enough version** early: "What would a rough, 60%-quality version look like?" This is the chart's "Half-ass it", which the bot offers sooner than the chart does (H4, B6).

Outcomes:
- "I know what to do now!" → **"Great job! Move to step 2."**
- "I still don't know :(" → **"Revisit previous to-do lists, ask for help, or take a walk break to think about it. Go to Step 1."**
- "It still feels too hard or like too much" → **wellbeing-check**.

## Tone notes
- For perfectionism, normalise "good enough" drafts. Fear of mistakes, not high standards, is what tracks procrastination (evidence_review.md B6).
- Never call the task "easy".
