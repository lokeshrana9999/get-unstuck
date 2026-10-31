---
name: extension-or-delegate
description: Steps 4 and 5. Checks for other reasons and honest effort, then helps decide what to do about the task itself (reschedule, delegate, do it partly, push through, or accept).
when-to-use: Any "Go to Step 4" from another skill, or when strategies aren't working and the person needs to decide about the task itself.
metadata:
  status: draft
  flowchart_nodes: [step4, step4_tried, go_again, step5, delegate_q, partial_q, worth_q, reschedule, ask_for_help, half_ass, radical_acceptance, push_through]
  source: data/flowchart.json
---

# Extension or delegate (Steps ④–⑤)

## Step ④ "Are there other reasons you can't start the task?"
- **Yes** → "Go through the flowchart again to solve them first" → triage from Step ①. The chart doesn't draw a target, so this is interpretive. If the person already knows the task and the new reason, skip ahead to Step ③.
- **Nope** → "Did you *actually* follow/try the suggestions on the flowchart?"
  - "I may have skipped some" → "Go through the flowchart again to solve them first" *(most likely routing)*
  - "I did, I promise!" → Step ⑤

Tone: keep the chart's playful honesty ("*actually*"), never accuse. Accept "I did, I promise!" at face value.

**Loop cap (verdict §4e.3):** the second time someone reaches "go through the flowchart again", offer Step ⑤ first: "Let's look at what to do about the task itself". They can still name a new reason (`bot_repeat_next` in the data). If this keeps happening across sessions, mention the clinician nudge (routine R5).

## Step ⑤ "Do *you* need to *complete* the task *right now*? Can you get an extension or make more time?"

**Bot ordering:** after "No flexibility", offer delegation **and** a good-enough version together ("Could someone help, or could a rough version do?"). The chart only reaches "Half-ass it" after delegation fails. Offering it earlier fits the perfectionism-concerns evidence (B6, H4), where quality allows.

| Path | Endpoint (chart text) | Bot behaviour |
|---|---|---|
| It can wait | **Set another day/time** to complete the task | Required: an if-then plan, "At [time], at [place], I will [first physical action]". A vague "another day" is procrastination in disguise (H2). Then offer routine R2 (only with a yes). |
| No flexibility → can it be delegated? **Yes!** | **Ask for help!** | Offer to **draft** a message or request. The person sends it; the bot never sends without an explicit yes. |
| … **Nope** → partially or badly? **Yes!** | **Half-ass it.** Something is better than nothing! | Help define the "good enough" minimum. |
| … **No, it's high-stakes** → worth pushing? **Not worth suffering for** | **Practice radical acceptance.** This task may not get done right now. It might feel like a catastrophe, but it'll be okay. | Acceptance means accepting reality, not giving up. Be warm. |
| … **It's worth it** | Do the task. Use **distress tolerance** skills and harm reduction tools to minimize its impact on you. | Suggest breaks, comfort and support. Point to a therapist for distress-tolerance skills. |

## After an endpoint
- Log the outcome if logging is on ([sheet-design.md](../../../docs/sheet-design.md)).
- If most sessions end here over several weeks, the weekly routine R5 may gently suggest a clinician ([guardrails §1](../../guardrails.md#1-not-medical-advice)).
