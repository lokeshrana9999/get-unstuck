# Verdict for Lokesh: the "Getting Started with Executive Dysfunction" flowchart and the proposed Grok bot

Everything below is grounded in `evidence_review.md` (section codes like B3 or F1 refer to it), `breakdown_v2.md` (the node-by-node transcription) and `review_v2.md` (the fidelity check of that transcription). I have not added any sources of my own.

---

## 1. The overall vibe

It's a warm, practical, peer-made self-help chart written by someone who clearly lives with this. The tone is non-judgemental ("it'll be okay", "Half-ass it", "Hell yeah, get started!"), it never claims to replace treatment, and its structure is sensible: figure out *what* to do, try to start, diagnose *why* you can't, pick a matching tactic, and if nothing works, decide what to do about the task itself (reschedule, delegate, do it badly, push through, or accept).

Its weaknesses are the ones you'd expect from community ADHD content:

- **Pop-neuroscience wrapping.** "DIY Dopamine" and "Follow the dopamine" dress up ordinary mood, movement and reward effects as brain chemistry you can steer. The evidence review flags this as its strongest pop-science problem (A3, E1–E5, G7).
- **Lay labels that sound clinical.** "Paralysis", "inertia" and "executive dysfunction" are relatable but aren't diagnostic categories (A1, A2).
- **Clinical skill-sets squeezed into one line.** "Use DBT skills" compresses a multi-week, therapist-led course into a starburst, and even gets the skill's name wrong (D2).
- **A few personal hacks presented as strategies**, one of which is physically unsafe (F1).

The evidence review's own summary (H7, takeaway 9) is fair: the chart's *endpoints* and *tone* are well-judged, even where individual tips are untested.

---

## 2. Are the methodologies legit? Grouped by evidence strength

A caveat that applies to everything (evidence review, "Caveats that apply throughout"): almost none of this was tested on adults with ADHD trying to start tasks. The ADHD evidence is mostly for *packages* (multi-week CBT/DBT group programmes) that bundle several of these tips; no trial isolates a single tip.

### Well supported (build on these)

| Chart item | Why it holds up | Ref |
|---|---|---|
| Meds (in the Wellbeing "physical needs" list) | Strongest short-term treatment for adult ADHD, from a 133-trial network meta-analysis | A4 |
| Rest / sleep | Sleep loss reliably impairs attention most of all | D1 |
| "Smallest, measurable first step" | Specific goals and near-term subgoals beat vague ones; "when X, I will Y" plans had a medium-to-large effect on getting started (d ≈ 0.65 across 94 tests); taught in both positive adult-ADHD CBT trials | B3 |
| Physical and emotional needs check before blaming willpower | Procrastination is well described as short-term mood repair; sleep and meds are the best-evidenced items | D1 |
| "Too hard / afraid of failing" as a reason | Task aversiveness and low self-efficacy are the strongest known correlates of procrastination | B6 |
| Content blockers / make it harder / physical distance | Moderate evidence in the general population that friction cuts use; avoiding temptation beats resisting it | F2, G2, G6 |
| Recurring check-in / accountability | Monitoring progress improves goal attainment (d ≈ 0.40 over 138 RCTs), more so when reported to others | F3, F4 |
| Find an out / plan an interruption | If-then plans improved stopping in children with ADHD in the lab | G5 |
| Rewards | Reinforcement helps performance in ADHD, *but* see "timing" under Contradicted | C4 |

### Plausible but untested in this form (keep, but label honestly)

- **Important/urgent matrix** targets a real bias (the "mere urgency effect") but no trial shows the matrix fixes it (B1).
- **Top 3 / 1 next thing**: no study of the numbers; "1 next thing" overlaps with if-then plans (B2).
- **"Just 10 minutes"**: no trial of a time box; procrastination treatments work modestly in students. The usual Zeigarnik justification is contradicted; the Ovsiankina effect (people tend to resume interrupted tasks) is the better rationale (B5).
- **5-minute "mindfulness"**: this is really reflective introspection, not mindfulness; the 8-week mindfulness programme evidence doesn't transfer, and shows no EF effect against active controls after bias correction (B7).
- **Name the emotion / impulse**: affect labelling reduces reactivity in the lab; weak for changing behaviour; untested in ADHD (G1).
- **Look forward**: episodic future thinking reduces impulsive choice in lab settings, non-ADHD. **Look back** has no support and one hint it doesn't work the same way (G4).
- **Wait 5 minutes**: weak; the delay was a minor contributor in the one relevant app study (G3).
- **Exercise**: the right direction, but studied doses are 10–30 minutes, not 60 seconds (E3).
- **White/pink noise** has modest ADHD-specific support; **music** does not, and harms reading; **audiobooks** only have support as a *bundled treat*, not as background during thinking work (C1, C2).
- **Body doubling**: popular in a 220-person survey, zero controlled trials, and social facilitation theory suggests it suits routine chores better than demanding thinking. Often marketed as "proven"; it isn't (C7).
- **Goblin Tools / AI task breakdown**: no study, but plausible via the B3 mechanism (B4). This matters for your bot: see section 3.
- **Half-ass it, radical acceptance, distress tolerance, set another day/time, self-compassionate tone**: consistent with CBT-for-perfectionism, ACT and self-compassion research; none tested in this form (H2, H4–H7).
- **Pretend to teach, Scientist Hat, grumbling, stretch, change of scenery, novelty, dance break, pretend to be excited**: weak, adjacent, or no evidence; harmless (C3, C5, C6, E1, E4, E5, F5, F6).

### Contradicted (fix or drop)

- **"Dopamine" as a pleasure hit you can top up.** Dopamine supports *wanting* and prediction error, not pleasure; the "dopamine menu" has no peer-reviewed study (A3). Pop-science flag: strong.
- **"Delicious snack" as a boost.** Glucose-fuels-willpower had limited evidential value; ego depletion was near zero in a 23-lab replication; sugar doesn't affect behaviour or cognition. Eating when hungry is still fine (E2, D1).
- **"Reward for after."** People with ADHD discount delayed rewards more steeply (d ≈ 0.43). One big reward at the end is a weak motivator; small, frequent, close rewards fit the evidence (C4).
- **"Perfectionism" as the cause.** Overall perfectionism correlates near zero with procrastination; only *perfectionistic concerns* (fear of mistakes) do. The chart's branch *text* ("too hard or afraid of failing") is right; the *label* is wrong (B6).
- **Executive dysfunction as the defining feature of ADHD.** EF weaknesses are "neither necessary nor sufficient"; EF problems also occur in depression, autism and sleep loss (A1).

### Mislabelled or unsafe

- **"Fit the facts"** is not a DBT skill. The skill is "check the facts" (D2).
- **"Create a harmless but immediate problem: toss phone across room, knock over water."** No evidence, and a real hazard: electrical, device damage, falls, injury. Drinking "lots" of water is unsafe for people on fluid restriction (F1).
- **Ariely & Wertenbroch (2002)**, the classic self-imposed-deadline study often used to justify accountability tips, was retracted in September 2026. Don't let the bot cite it (F4).

---

## 3. Should you build the Grok bot on it?

**Conditional yes.** Build it, but not as a faithful port of the chart. Build it on the chart's *structure* and *tone*, with the content re-weighted toward what the evidence supports and the dangerous or misleading bits removed.

Why yes:

- **The skeleton is sound.** Know what → try → diagnose why → matching tactic → decide about the task. Every endpoint is low-risk and consistent with acceptance-based and perfectionism research (H4–H7, takeaway 9).
- **A bot is uniquely good at the best-evidenced step.** Turning a vague task into a specific, measurable first step with a when/where/how plan is the single most consistently supported technique in the review (B3, H2, takeaway 2). That is exactly what an LLM does well. It's also what Goblin Tools is for (B4), so the bot absorbs that tip natively.
- **Most tips are untested but harmless.** The review's position is "low-risk to try, don't call them evidence-based" (takeaway 6). A bot can offer them as options while being honest about that.
- **The emotional-needs and self-compassion framing fits the evidence** on procrastination as mood repair (D1, H7).

Why not an unconditional yes:

- **Shipping it as-is would spread three strong pop-science claims** (dopamine, snacks, body doubling as "proven") and one unsafe hack under a health-adjacent brand name (A3, E2, C7, F1).
- **It names a clinical population.** "ADHD & Executive Dysfunction" in the title means you need disclaimers, no-diagnosis behaviour and crisis handling that a paper chart doesn't.
- **Five routings in the chart are ambiguous at its resolution** (review_v2, Error 1). You will have to decide those yourself before you can encode a flow at all.
- **No trial supports the chart, the bot, or any single tip in adults with ADHD.** The honest pitch is "a structured coaching flow built on reasonable principles", not "evidence-based ADHD tool".

If you can't do the changes in section 4, don't ship it under that name.

---

## 4. What needs improving before building

### 4a. Content to drop

1. **"Create a harmless but immediate problem (toss phone, knock over water)."** Replace with "set a timer or alarm across the room". Same logic, no hazard (F1, takeaway 7).
2. **"Delicious snack" as a motivational tool.** Keep "are you hungry?" in the needs check; drop snacks from the reset list (E2).
3. **"Follow the dopamine"** as a phrase. Keep the technique underneath it (swap an open-ended reward for a time-limited one, close to the effort) under a plain name like "swap the reward" (G7, C4).
4. **"Do DBT worksheet on willfulness."** No measure, no study; it's an in-joke that only works inside a DBT programme (G8). The comic exchange can still end at radical acceptance.
5. **"Look back"** at the last time you acted on the impulse. No support and a hint it doesn't work the way "look forward" does (G4). Low cost to cut; keep "look forward".
6. **The Zeigarnik explanation** if it was ever going to appear in bot copy (B5).
7. **Any citation of Ariely & Wertenbroch 2002** (F4).

### 4b. Content to reword

| Current | Change to | Why |
|---|---|---|
| "DIY DOPAMINE" | "Quick reset" / "Mood & energy reset" | The activities may help via mood, arousal and movement; the dopamine story is wrong (A3, takeaway 4) |
| "Exercise: 60s jumping jacks" | "Move for 10–20 minutes if you can; even a minute is a start" | Studied doses are 10–30 min; 60 s is a 25-person non-ADHD pilot (E3) |
| "Listen to music or an audiobook" | "Try white or pink noise. Save music with lyrics and audiobooks for tasks that don't involve words, or as a treat you only get while doing the chore" | C1, C2 |
| "Decide on a reward for after" | "Set small rewards you get *during* and right after each step" | Delay discounting in ADHD (C4, takeaway 3) |
| "PERFECTIONISM: It feels too hard or I'm afraid of failing" | Keep the text, drop the label; call it "Too hard / afraid I'll fail" | Only perfectionistic concerns matter; the text is already right (B6) |
| "MINDFULNESS: Take 5 minutes to sit quietly and consider why" | "Pause and reflect: 5 minutes to work out what's in the way" | It's introspection, not mindfulness (B7) |
| "Use DBT skills- fit the facts, opposite action, loving kindness" | "Check the facts: is the feeling proportionate to what's actually true? Then try the opposite action. (These come from DBT; a full course teaches them properly.)" | Wrong skill name; packages, not one-liners, are what have evidence (D2, takeaway 8) |
| "Set another day/time" | Force an if-then plan: specific time, place, first action | Vague rescheduling is functionally procrastination (H2) |
| "Pick the top 3 things or 1 next thing" | "Pick the 1 next thing, and say when and where you'll do it" | B2, B3 |
| "Body double with a friend" | Keep, add "works for many people; untested in trials; best for routine tasks" | C7 |
| "Accomodate the task" | "Accommodate" | Spelling (breakdown_v2) |
| "Use Goblin Tools!" | The bot does this itself | B4 |

### 4c. Content to add

1. **A "did you forget?" check.** Trouble remembering to act on intentions partly explains the ADHD–procrastination link (A2). The chart has no branch for it. Add a reminder/if-then option at Step ②.
2. **An if-then plan generator** as the default output of BREAK IT DOWN, "1 next thing" and "Set another day/time": "At [time], at [place], I will [first physical action]" (takeaway 2).
3. **A better route for "I'm worried I'll fail."** The chart sends it straight to Step ④. Low self-efficacy is one of the two strongest drivers (B6), so route it to BREAK IT DOWN and offer "do it badly" early (H4).
4. **A "get assessed" nudge.** If a user keeps landing at Step ④ or ⑤, say that medication and structured CBT/DBT programmes have far more evidence than any tip here, and suggest a clinical assessment (takeaway 10, A4).
5. **Honesty tags** on each tip, in plain words: "well supported", "reasonable but untested", "a hack some people like". The review's main finding is the gap between the specific claim and the nearest principle (evidence review intro); the bot should show that gap rather than hide it.
6. **A proper credit and permission line** for the original chart author. (This is a product point, not something the evidence review covers.)

### 4d. Safety guardrails

1. **No diagnosis, no medication advice.** "Meds" means "take your prescribed medication as prescribed". The bot must never suggest starting, stopping or changing a dose. Executive dysfunction occurs without ADHD (A1), so don't imply the user has ADHD.
2. **Crisis handling.** The Wellbeing branch deliberately asks about shame, fear and anxiety, and the endpoint talks about "catastrophe". If a user expresses self-harm, hopelessness or crisis, the bot must stop the flow and point to local crisis resources. (Standard duty for anything in this space; the evidence review doesn't address it because the chart is a paper artefact.)
3. **Physical safety.** Remove the throw/spill hack (F1). Add a line to the water tips: "skip this if you've been told to limit fluids" (F1). Make "stretch", "dance break" and "jumping jacks" conditional on the user being able to move safely.
4. **Food.** Frame eating as meeting hunger, never as a performance booster (E2, D1). Avoid pushing snacks repeatedly, since you don't know who's on the other end. (Product judgement on my part, not a review finding.)
5. **Interruption load.** Frequent alarms raise stress and frustration (F3). Cap how many check-ins the bot proposes and let the user set the cadence.
6. **No "evidence-based" or "proven" language** for body doubling, dopamine menus, the 10-minute rule, the Eisenhower matrix, Goblin Tools or DBT one-liners (C7, A3, B5, B1, B4, D2).
7. **Scope disclaimer** up front: a self-help coaching flow, not treatment; complements, doesn't replace, clinical care (A4).

### 4e. Design changes for the bot

1. **Resolve the five ambiguous routings** before encoding anything (review_v2, Error 1): the bottom of RESIST IMPULSES, the split below "Why?", PRIORITIZE's "I know what to do now!" link, the INTERRUPT INERTIA outcomes, and the Step ④ "skipped some" junction. The breakdown's readings are plausible; pick them deliberately and document them.
2. **Lead with the best-supported steps** (takeaway 1): needs check (sleep, meds, hunger, mood), one specific first step with an if-then plan, friction on temptations, progress tracking. Put the fun hacks behind those, not in front.
3. **Cap the loops.** "Go through the flowchart again" from Step ④ is fine on paper; in a bot it's an infinite loop for a frustrated user. After one full pass, go to Step ⑤.
4. **Keep the comic exchange, but shorter.** The "No!!! / Fine." back-and-forth is charming once. Don't make the bot argue with the user more than one round before offering radical acceptance (H5).
5. **One question at a time, short messages, remembered state.** The audience is people who are already overwhelmed; the chart's own logic says reduce choice (B2).
6. **Make "Half-ass it" the second option, not the fourth.** The chart only reaches it after extension and delegation. "Good enough" fits the perfectionism-concerns evidence (B6, H4), and is cheap to offer early where quality isn't critical.
7. **Close the loop with the user's own data.** Writing down or reporting progress is where self-monitoring works best (F3). Let the bot record which tactics the user tried and what happened, and use that instead of generic tips next time.
8. **Treat "resist impulses" as mostly friction, not willpower.** The supported items there are physical distance, deleting/hiding, if-then outs and accountability (G2, G5, G6, F4). Put those first; put naming, waiting and looking forward second (G1, G3, G4).

---

## Bottom line

The chart is a thoughtful, kind, structurally sound piece of peer self-help with a pop-neuroscience coat of paint and one genuinely unsafe tip. Its strongest parts are the boring ones: needs, meds, sleep, a specific first step with a plan, friction, and tracking. Build the bot on those, keep the tone and the endpoints, relabel or drop the dopamine and snack content, fix the DBT naming, cut the throw-your-phone hack, add crisis and no-diagnosis guardrails, and never call any of it "proven".
