# Research: evidence and landscape for an ADHD productivity bot

*Researched 2026-10-31 for the pivot in [PIVOT.md](PIVOT.md). Two research passes ran (evidence and app landscape) and were merged and edited here. Sources are real and linked. Items not confirmed from an abstract, a journal page or an official page are marked **unverified**. No full texts were read, so effect sizes are as reported in abstracts or secondary summaries. Builds on [`source/evidence_review.md`](../source/evidence_review.md); items reused from it are marked "(from evidence_review.md)".*

**Evidence levels used here:**
- **Strong:** consistent meta-analytic evidence in a relevant population.
- **Moderate:** a meta-analysis in a general or adjacent population, or several RCTs.
- **Weak:** small, uncontrolled or single studies.
- **None:** no studies found.
- **Contradicted:** studies point the other way.

## Bottom line

- **Almost nothing here has been tested in adults with ADHD.** The bot should be pitched as a productivity aid built on reasonable, general-population principles, never as an ADHD treatment.
- **Reminders work modestly in the general population** (SMS adherence OR ≈ 1.7–2.1; health-promotion d ≈ 0.33). Personalised reminders work better, and effects fade over weeks. No reminder trials were found in ADHD adults.
- **If-then plans have the strongest general evidence** (d = 0.65). In ADHD the evidence is lab tasks with children only; there are **no trials in ADHD adults** and none of digitally delivered plans.
- **Time-perception deficits in ADHD are robust** (Marx 2022, 55 studies). Evidence that timers or time aids *help* is one small child RCT; there is **none for adults**.
- **Notifications cost attention even when ignored** (Stothart 2015) and raised self-reported inattention (Kushlev 2016). Batching them about 3 times a day beat hourly batching, and turning them all off raised anxiety (Fitz 2019, a single trial).
- **Body doubling and virtual coworking have no peer-reviewed outcome data.** Company productivity figures are marketing.
- **ADHD coaching evidence is weak**, mostly uncontrolled studies of college students. The best adult digital trial included a human coach (Moëll 2015).
- **People drop apps fast.** Median 30-day retention of mental-health apps is 3.3% (Baumel 2019). Design for coming back, not for streaks.
- **Existing ADHD apps** offer visual timelines, timers, task breakdown, CBT lessons, coworking and gamification. None except Inflow has a peer-reviewed study, and Inflow's is a feasibility study with no control group.
- **Grok Bot:** routines post to the Bot's chat, and push notifications are best-effort. **The docs describe no quiet hours, do-not-disturb or snooze**, so the bot has to build these into its own scheduling.

---

## Part A: Evidence

### 1. Reminders and prompting

- **Thakkar et al. 2016, *JAMA Intern Med* 176(3):340-9.** https://doi.org/10.1001/jamainternmed.2015.7667
  - 16 RCTs, n = 2,742 adults with chronic disease.
  - Text messages raised the odds of medication adherence: OR 2.11 (95% CI 1.52-2.93). After adjusting for publication bias, OR 1.68 (1.18-2.39). I² = 62%.
  - The authors illustrate this as 50% adherence rising to 67.8%, but the 50% baseline is their assumption, not a pooled finding.
  - The effect did not vary with personalisation, two-way messaging or message frequency.
  - Trials were short and used self-reported adherence, so durability is unknown.
  - **Moderate** (general adult patients). Abstract-level via secondary pages.
- **Head, Noar, Iannarino & Harrington 2013, *Soc Sci Med* 97:41-48.** https://doi.org/10.1016/j.socscimed.2013.08.003
  - 19 RCTs of SMS health promotion in 13 countries: d = 0.33 (0.27-0.39), I² = 68%.
  - Tailored plus targeted messages did better (d ≈ 0.44). That figure comes from a secondary source and is unverified.
  - Text-only programmes performed as well as texting plus other components.
  - **Moderate** (general).
- **Fry & Neff 2009, *JMIR* 11(2):e16.** https://www.jmir.org/2009/2/e16
  - Systematic review of periodic prompts (messages, reminders or brief feedback) in weight-loss, activity and diet programmes: 19 studies, n = 15,655, 11 with positive results.
  - Personalised prompts beat generic ones. Prompts plus contact with a human counsellor worked better.
  - Little long-term follow-up. **Moderate/Weak** (general).
- **Reminders for using a digital programme.** A 2022 RCT (n = 109) of weekly SMS reminders for a self-guided internet intervention found no improvement in logins or module completion. https://doi.org/10.3389/fdgth.2022.821031 (snippet, unverified). **Weak.** Reminders that only say "use the app" may not help.
- **Prospective memory in ADHD.**
  - Altgassen et al. 2014 compared 25 adults with ADHD and 25 controls (snippet, unverified). Time-based prospective memory looks more impaired than event-based; event-based findings are mixed. https://link.springer.com/article/10.1007/s12402-018-0273-x
  - Adults with ADHD carried out fewer of their own real-life intentions (2018 study, snippet).
  - Prospective memory partly mediates the link between ADHD symptoms and procrastination (Altgassen 2019, from evidence_review.md).
- **External cueing aids in adult ADHD.** No meta-analysis or RCT of external reminder aids alone was found. **Weak/None.**

### 2. Implementation intentions (if-then plans) in ADHD

- **General population:** d = 0.65 across 94 tests (Gollwitzer & Sheeran 2006, from evidence_review.md). **Strong** (general).
- **Toli, Webb & Hardy 2016, *Br J Clin Psychol* 55(1):69-90.** https://doi.org/10.1111/bjc.12086
  - Meta-analysis of if-then plans in clinical and analogue (above-cut-off) mental-health samples: d+ = 0.99 (k = 28, N = 1,636), excluding one outlier with d = 4.99. The 95% CI of 0.40-1.60 comes from a secondary source.
  - The effect is large but the CI is wide, and the samples are lab-scale. **Moderate** (clinical, mostly not ADHD).
- **Children with ADHD (lab tasks):**
  - Response inhibition on a Go/No-Go task (Gawrilow & Gollwitzer 2008, from evidence_review.md). Children with ADHD reached the level of controls.
  - Delay of gratification (Gawrilow, Gollwitzer & Oettingen 2011, *Cogn Ther Res* 35:442-455). Inpatient children with ADHD n = 45; replicated in outpatients n = 47 plus 40 controls. https://www.socmot.uni-konstanz.de/sites/default/files/Gawrilow_Gollwitzer_Oettingen_Delay_2011-2.pdf
  - Working memory and task-switching (perseverative errors) (2011, *J Soc Clin Psychol* 30:615-645). https://www.socmot.uni-konstanz.de/sites/default/files/Gawrilow_Gollwitzer_Oettingen_Executive_Function_JSCP_2011.pdf
  - **Moderate** for lab effects in children. These are short tasks, not real-world goals.
- **Adults with ADHD:** no RCT found. A clinical source says if-then plans "have not yet [been] studied in adults with ADHD" (snippet via apsard.org, unverified). **None.**
- **If-then plans delivered digitally in ADHD:** no studies found. **None.**

### 3. External accountability and body doubling

- **Body doubling:** qualitative and descriptive evidence only (Eagle & Ringland 2024, from evidence_review.md). The audience effect improves performance on simple tasks and hurts it on complex ones (Bond & Titus 1983, from evidence_review.md).
- **Commitment devices and progress monitoring:**
  - Monitoring goal progress helps, and more so when progress is reported or made public (Harkin 2016, from evidence_review.md).
  - Commitment devices are reviewed in Bryan, Karlan & Nelson 2010 (from evidence_review.md).
  - **Moderate** in the general population, **Weak** in ADHD.
- **Focusmate-type virtual coworking:**
  - No independent peer-reviewed outcome study found.
  - Focusmate's "143% productivity increase" claim comes from an internal company study. https://focusmate.com/?p=3865
  - A blog reports a small 2025 Drake University EEG study that found no effect on focus or performance (https://blog.saner.ai/focusmate-review/). Unverified, not peer-reviewed.
  - **None** (peer-reviewed). **Contested** (anecdotal).
- **Human contact plus prompts:** this combination beat prompts alone (Fry & Neff 2009, above). This is indirect support for an accountability element.

### 4. Time-blindness aids

- **Marx, Cortese, Koelch & Hacker 2022, *JAACAP*.** https://doi.org/10.1016/j.jaac.2021.12.004
  - 55 studies comparing people with ADHD with controls.
  - Deficits by paradigm:
    - time discrimination: medium (25 studies, n = 1,633);
    - time reproduction: medium (26 studies, n = 2,364);
    - time estimation: small to medium (8 studies, n = 1,024);
    - time production: small (7 studies, n = 380).
  - No sign of publication bias. Exact g values not retrieved (summary from https://adhdevidence.org/blog/time-blindness-found-to-be-a-consistent-feature-of-adhd).
  - **Strong** that a deficit exists. Mostly children and adolescents, as far as could be determined.
- **Zheng et al. 2020/2022, *J Atten Disord*.** https://doi.org/10.1177/1087054720978557
  - Children and adolescents, 27 studies.
  - Accuracy g > 0.40 and precision g = 0.66, with a tendency to overestimate durations. The gap narrows with age.
  - Secondary summary only. **Strong/Moderate** (youth).
- **Interventions:**
  - **Wennberg, Janeslätt, Kjellberg & Gustafsson 2018, *Eur Child Adolesc Psychiatry* 27:329-342.** https://doi.org/10.1007/s00787-017-1052-5 (PMC5852175)
    - RCT, n = 38 medicated children aged 9-15.
    - Time-processing training plus time-assistive devices (such as visual timers) vs education alone.
    - Better time processing at 24 weeks, and parent-rated daily time management improved. Child self-ratings did not change.
    - **Weak/Moderate** (one small RCT, children, multimodal so the timer's own effect can't be separated).
  - **Visual timer during a maths test (PMC12731990).** n = 44 schoolchildren. Lower anticipatory anxiety and less off-task behaviour, more so in children at higher ADHD risk. No gain in test scores was reported in a related study. Use of the timer varied widely. **Weak.**
  - **Adults with ADHD:** no studies of visual timers or time-estimation training found. **None.**

### 5. Notification fatigue, habituation, timing and JITAIs

- **Alert fatigue (clinical decision support):**
  - Poly et al. 2020, *JMIR Med Inform* 8(7):e15653 (https://medinform.jmir.org/2020/7/e15653): 23 studies, alert override rates 46-96%.
  - Tailoring alerts to the recipient's role reduced fatigue (Hussain 2019, *JAMIA*, snippet, unverified).
  - This is about clinicians, not consumers, so it is an analogy only. **Moderate** that alerts which are frequent and not tailored get ignored.
- **Habituation and declining effects:**
  - Daily motivational texts initially added about 729 steps a day, and the effect "decreased over time" (TU Delft record; fetch failed, unverified).
  - Thakkar 2016 explicitly flags durability as unknown.
  - No study directly tested habituation as a function of message frequency. **Weak**, but the decline is a consistent signal.
- **Notifications, stress and attention:**
  - **Kushlev, Proulx & Dunn 2016, CHI.** https://doi.org/10.1145/2858036.2858359
    - n = 221 students, within-subject: one week with alerts on, one week with alerts off.
    - Alerts on led to more self-reported inattention and hyperactivity. Inattention in turn predicted lower productivity and well-being.
    - The authors stress this does not show phones cause ADHD.
    - **Moderate** (students, self-report).
  - **Stothart, Mitchum & Yehnert 2015, *JEP: HPP* 41(4):893-897.** https://doi.org/10.1037/xhp0000100
    - n = 166 students.
    - An unanswered call or text notification alone disrupted a sustained-attention task about as much as actually using the phone. The "3× errors" figure comes from press coverage.
    - **Moderate** (lab).
- **Timing and frequency:**
  - **Fitz, Kushlev, Jagannathan, Lewis, Paliwal & Ariely 2019, *Comput Hum Behav* 101:84-94.** https://doi.org/10.1016/j.chb.2019.07.016
    - Field RCT, n = 237.
    - Batching notifications 3×/day improved attention, productivity, mood and stress. Hourly batching was no different from control.
    - Turning notifications off entirely increased anxiety and FoMO (fear of missing out).
    - **Weak/Moderate** (single trial; Ariely is a co-author, see the flags).
- **JITAIs (just-in-time adaptive interventions):**
  - The design framework is Nahum-Shani et al. 2018, *Ann Behav Med*. Not fetched in this pass, so unverified here.
  - **Wang & Miller 2020, *Health Commun* 35(12):1531-1544.** https://doi.org/10.1080/10410236.2019.1652388 (PubMed abstract)
    - g = 1.65 vs waitlist (k = 9), g = 0.89 vs non-JITAI treatments (k = 21), g = 0.79 pre-post (k = 13).
  - **Xu & Smit 2023, *Digital Health* 9.** https://doi.org/10.1177/20552076231183543
    - g = 0.77 (0.32-1.22), but from only 21 effect sizes and n = 592, and all from uncontrolled pre-post designs.
    - Design features (theory, passive vs active sensing) did not moderate effects.
  - **Moderate/Weak.** The effects are implausibly large for small, early trials. No ADHD JITAI trials were found.

### 6. ADHD coaching, digital interventions and engagement

- **Ahmann et al. 2018 coaching review.**
  - 22 studies, 19 with outcomes, 18 of 19 positive.
  - Designs ranged from case studies to RCTs. **No studies of individual coaching for adults** were included.
  - Snippet and CHADD summary only; DOI not found. **Unverified.** https://chadd.org/attention-article/evidence-based-coaching-for-adults-with-adhd/
- **Prevatt & Yelland 2015, *J Atten Disord* 19(8):666-77.** https://doi.org/10.1177/1087054713480036
  - n = 148 college students, 8-week coaching programme, uncontrolled pre-post design.
  - Improved on all 10 study and learning-strategy scales, plus self-esteem and satisfaction.
  - The authors call the results preliminary. **Weak.**
- **Coaching RCTs:**
  - Pilot RCT, n = 20: coaching rated more acceptable, outcomes inconclusive (ECU thesis). https://thescholarship.ecu.edu/handle/10342/5892
  - Planning-focused CBT for college students vs waitlist, n = 58: only a modest effect on inattention (https://pubmed.ncbi.nlm.nih.gov/29998770/, snippet).
  - **Weak** (students; no adequately powered adult coaching RCT found).
- **Digital interventions for adult ADHD:**
  - **Living SMART: Moëll, Kollberg, Nasri, Lindefors & Kaldo 2015, *Internet Interventions* 2(1):24-31.** https://doi.org/10.1016/j.invent.2014.11.004
    - RCT, n = 57, coached online course on organising daily life with smartphone apps vs waitlist.
    - ASRS-Inattention (adult ADHD self-report scale) fell from 28.1 to 22.9, a significantly larger drop than in controls.
    - **Weak/Moderate.** Small sample and a waitlist control; the human coach is part of the intervention.
  - **Inflow app RCT.**
    - n = 154 adults, 8 weeks vs waitlist.
    - Improved inattentive and hyperactive symptoms and quality of life, but not functional impairment.
    - An author has a stake in the company. Secondary sources only, citation not retrieved: **unverified.** https://www.simplypsychology.org/?p=97474
  - **FOCUS ADHD app trial.** n = 73. Users rated the app well, but medication adherence did not improve (snippet, **unverified**).
- **Engagement: Baumel, Muench, Edan & Kane 2019, *JMIR* 21(9):e14567.** https://www.jmir.org/2019/9/e14567
  - Real-world usage panel covering 93 Android mental-health apps.
  - Median 15-day retention 3.9%, 30-day retention 3.3%, daily open rate 4.0%.
  - Peer-support apps retained users best (8.9% at day 30).
  - **Strong** that drop-off is steep (general users).

---

### Summary table

| Topic | Finding | Evidence level | Population | Source |
|---|---|---|---|---|
| SMS reminders, adherence | OR 2.11 (bias-adjusted 1.68); short trials | Moderate | Chronic-disease adults | Thakkar 2016 |
| SMS health promotion | d = 0.33; tailoring helps | Moderate | General | Head 2013 |
| Periodic prompts | 11/19 positive; personalised + human contact better | Moderate/Weak | General | Fry & Neff 2009 |
| Reminders to use a digital programme | No gain in logins or completion | Weak | Adults (internet intervention) | Front Digit Health 2022 |
| Time-based prospective memory | More impaired than event-based in ADHD | Weak/Moderate | ADHD adults | Altgassen 2014 (snippet); Altgassen 2019 (from evidence_review.md) |
| If-then plans, clinical samples | d+ = 0.99, wide CI | Moderate | Clinical/analogue | Toli 2016 |
| If-then plans, ADHD | Better inhibition, delay of gratification, working memory on lab tasks | Moderate (lab) | ADHD children | Gawrilow 2008 (from evidence_review.md), 2011a, 2011b |
| If-then plans, ADHD adults | No trials | None | ADHD adults | (search) |
| Body doubling / Focusmate | Qualitative only; company claims | None (peer-reviewed) | Neurodivergent adults | Eagle & Ringland 2024 (from evidence_review.md); Focusmate media kit |
| Progress monitoring | Helps, more when reported | Moderate (general), Weak (ADHD) | General | Harkin 2016 (from evidence_review.md) |
| Timing deficits | Medium reproduction and discrimination deficits | Strong | Mostly ADHD youth | Marx 2022; Zheng 2020 |
| Time aids + training | Improved time processing at 24 weeks | Weak/Moderate | ADHD children 9-15 | Wennberg 2018 |
| Visual timer | Less anxiety and off-task behaviour; no score gain | Weak | Schoolchildren | PMC12731990 |
| Alert fatigue | 46-96% override rates | Moderate (analogy) | Clinicians | Poly 2020 |
| Reminder habituation | Effects fade over weeks | Weak | General | TU Delft trial (unverified); Thakkar 2016 |
| Notifications and attention | More inattention; disrupt attention even unanswered | Moderate | Students | Kushlev 2016; Stothart 2015 |
| Batching | 3×/day best; none at all raises anxiety | Weak/Moderate | General adults | Fitz 2019 |
| JITAIs | g 0.77-0.89 vs non-JITAI (likely inflated) | Moderate/Weak | General | Wang & Miller 2020; Xu & Smit 2023 |
| ADHD coaching | Positive but uncontrolled; no adult individual-coaching studies | Weak | Mostly college students | Ahmann 2018 (unverified); Prevatt & Yelland 2015 |
| Digital adult ADHD | Coached smartphone course reduced inattention | Weak/Moderate | ADHD adults | Moëll 2015; Inflow (unverified) |
| App engagement | 3.3% 30-day retention | Strong | General app users | Baumel 2019 |

---

### Design implications for the bot

1. **Event-based reminders by default.** Tie each nudge to a cue ("when you sit down after lunch...") rather than only a clock time. Time-based prospective memory looks most impaired in ADHD.
2. **Write if-then plans during onboarding.** Phrase each recurring task as "If [situation], then I will [first step]." Present this as promising, not proven, for ADHD adults.
3. **Personalise and tailor every message.** Use the user's own task name, goal and words. Generic prompts underperform.
4. **Limit message volume.** Default to a small number of scheduled contacts a day (for example morning plan, one mid-day check-in, end-of-day review). Bundle non-urgent nudges together rather than sending each one separately. Never send an unbounded stream.
5. **Don't offer "all off" as the only alternative to "on".** Silencing everything raised anxiety in Fitz 2019. Offer reduced or batched modes and quiet hours.
6. **Expect habituation and plan for it.** Rotate message wording and format. Track response rate per message type. Automatically reduce or pause a nudge that is ignored about three times in a row (a heuristic, not an evidence-based threshold) and ask whether it is still useful.
7. **Adapt to responsiveness, but modestly.** Use simple rules first, such as time of day and recent replies, and evaluate before adding sensing. JITAI effects are not established, and none have been tested in ADHD.
8. **Every nudge must be actionable.** Name the task and its smallest first step, and offer one-tap replies ("started", "snooze 15", "stuck", which opens the get-unstuck flowchart). Reminders that only say "open the app" did not raise engagement.
9. **Make time visible.** Show elapsed and remaining time during body-doubling sessions, report "you estimated X, it took Y" at the end-of-day review, and add buffers to deadline countdowns. ADHD time-perception deficits are robust, so feedback is worth trying. There is no adult evidence that timers help.
10. **Use body doubling as low-risk support, and describe it honestly.** Default to short sessions with a stated goal at the start and a report-back at the end. Don't claim productivity gains.
11. **Report progress at the end-of-day review.** Self-monitoring with reporting works in the general population (Harkin 2016).
12. **Design for drop-off.** Expect most users to fade within weeks. Re-engage gently and without guilt. Give value in the first session. Measure 7-day and 30-day retention as primary metrics.
13. **Complement human support, don't replace it.** The best adult ADHD digital evidence (Living SMART) involved a human coach. Prompts combined with human contact did best in Fry & Neff. Offer an optional accountability partner, and point users towards clinical care where appropriate.
14. **Make no clinical claims.** Coaching and app evidence for ADHD adults is weak, so don't describe the bot as a treatment.

### Weak/contested evidence flags

- **If-then planning in ADHD adults: no evidence.** All the ADHD evidence is children on lab tasks.
- **Body doubling / Focusmate:** no peer-reviewed outcome data. Company "143%" figures are marketing.
- **Visual timers:** no adult evidence, and the child evidence comes from a multimodal intervention or small studies.
- **JITAI effect sizes (g up to 1.65)** come from small, early, often uncontrolled studies and are probably inflated.
- **ADHD coaching:** mostly uncontrolled studies of college students. The Ahmann 2018 review details are unverified, and no individual adult coaching studies were reported.
- **Fitz 2019** has Dan Ariely as a co-author. His unrelated 2012 field study was retracted for fabricated data, and the 2002 deadlines paper is flagged in evidence_review.md. There is no known problem with this paper, but it needs replication.
- **Alert fatigue** evidence comes from clinicians, so applying it to consumers is an analogy.
- **SMS adherence trials** are short and use self-report, so long-term effects are unknown.
- **Unverified items:** Inflow RCT, FOCUS app trial, Hussain 2019, the TU Delft step-count decline, Altgassen 2014 details, the Drake body-doubling study, and the Nahum-Shani 2018 framework (not fetched).

---

## Part B: Existing ADHD productivity apps and their pitfalls

*App prices change often and vary by region. Labels: **[official]** means a vendor site, app store page or vendor doc; **[paper]** means peer-reviewed; **[3rd-party]** means press, reviews or blogs; **[unverified]** means a claim not traced to its original source.*

### 1. Comparison table

| App | Core approach | Evidence status | Notable pitfalls | Sources |
|---|---|---|---|---|
| Tiimo | Visual timeline planner; AI Co-Planner breaks down tasks; focus timer; calendar sync | No independent study found. Company claims are unsourced. | Price not clear upfront; paywalled AI and web features; the emoji-heavy style splits opinion | [App Store](https://apps.apple.com/app/tiimo/id1480220328), [Healthify NZ](https://healthify.nz/apps/t/tiimo-app), [Tiimo B2B](https://tiimoapp.com/partnerships/b2b) |
| Inflow | CBT-based ADHD lessons, community, optional coaching | One open feasibility study (n=240, no control group) [paper]. An RCT is claimed in a press release but the publication wasn't found. | Expensive subscription; complaints that a free trial auto-converted into a yearly plan | [PMC9931323](https://pmc.ncbi.nlm.nih.gov/articles/PMC9931323/), [BusinessWire](https://secure.businesswire.com/news/home/20260324103905/en/Cerebral-Acquires-Leading-ADHD-Behavioral-App-Inflow-Expanding-Access-to-Continuous-Care) |
| Goblin Tools | Single-purpose AI tools: Magic ToDo task breakdown, Formalizer, Judge, Chef and others | None found | Copycat subscription apps with similar names; output from AI is unvalidated | [App Store](https://apps.apple.com/ae/app/id6449003064), [Warwick library](https://warwick.ac.uk/services/library/using/productivity-tools/magic-todo-gobin-tools) |
| Structured | Timeline day planner; Pro adds recurring tasks, calendar import, Replan and AI | None found | Core features such as recurring tasks are behind the paywall; prices changed several times | [Pricing blog](https://structured.app/blog/new-pricing), [App Store](https://apps.apple.com/app/structured-daily-planner/id1499198946) |
| Focusmate | Live video body doubling with a stranger, in 25- or 50-minute sessions | No study of Focusmate found. CHADD says body doubling hasn't been validated by significant research. | Free tier capped at 3 sessions per week; depends on scheduling and on a partner showing up | [CHADD](https://chadd.org/adhd-weekly/could-a-body-double-help-you-increase-your-productivity/), [lifestack pricing](https://lifestack.ai/blog/focusmate-pricing) |
| Llama Life | A countdown timer per task; single-tasking with chimes and templates | None found | Narrow feature set; another subscription | [App Store](https://apps.apple.com/us/app/adhd-organizer-llama-life/id6454469750), [Capterra](https://www.capterra.com/p/253326/Llama-Life/) |
| Routinery | Step-by-step routine timer with voice alerts and push notifications | None found | Free tier limited to about 2 routines and shows ads; a third party reports features moving behind the paywall | [App Store](https://apps.apple.com/app/id1450486923), [apppricinglab](https://apppricinglab.com/app/apple/1450486923) |
| Finch | Self-care virtual pet that grows when you check in | No controlled study found | Pet care can become "another chore"; streak mechanics; billing complaints | [YourStory](https://yourstory.com/2022/06/app-review-self-care-pet-finch-gamifies-mental-wellbeing), [Neurospicy review](https://neurospicynomnoms.beehiiv.com/p/digital-pet-bestie-for-self-care-610618d407f7afef) |
| Habitica | To-do list as a role-playing game, with parties for accountability | None found | Reviews say the game loses its pull after about a month; parties stall when members go inactive | [App Store](https://apps.apple.com/au/app/id994882113), [unstar roundup](https://unstar.app/blog/habitica-streaks-productive-way-of-life-habit-bull-habit-tracker-apps-ranked-2026) |

### 2. Per-app notes

**Tiimo** [official/3rd-party]
- A visual daily planner aimed at ADHD and autistic users. The App Store shows a 4.6-star rating from about 14.8K reviews.
- An AI Co-Planner arrived in late 2025. It breaks tasks into steps.
- Pricing: a free tier plus a Pro subscription; reported prices vary. The free tier reportedly has no web planner, no AI and no focus timer.
- Evidence: Tiimo began as a 2015 research project with neurodivergent teens. Its B2B page says that "research shows" supported neurodivergent employees raise team productivity "by up to 30%", but it names no study. Recognition so far is awards (Apple Design Award finalist, Fast Company), not efficacy ([EIF](https://www.eif.org/case-study/all/tiimo)).

**Inflow** [paper/official]
- A CBT-based programme: daily lessons, symptom tracking, a community feed and optional coaching.
- Pricing (third-party, 2025): about $95.99 a year for the app only, or about $199.99 a year with coaching ([ChoosingTherapy](https://www.choosingtherapy.com/inflow-adhd-app-review/), [Helpguide](https://helpguide.org/handbook/online-therapy/best-apps-for-adhd)). There is a 50% student discount and a needs-based Access Program.
- Evidence: Knouse et al., *PLOS Digital Health*, 2022. This was an open 7-week feasibility study with 240 adults.
  - Participants used the app a median of 3.86 times per week.
  - Those who stayed for 7 weeks self-reported fewer symptoms.
  - The authors themselves say a randomized controlled study is needed to tell whether the changes are "really due to the effects of Inflow".
- Cerebral acquired Inflow in March 2026. Its press release claims "an 8-week randomized controlled trial" with significant improvements. **I could not find that trial published [unverified].**
- Pitfall: Trustpilot complaints about free trials converting into yearly subscriptions [3rd-party].

**Goblin Tools** (developer Skyhook) [official]
- A set of single-purpose AI tools. Magic ToDo breaks a task into steps.
- Pricing: the website is free with no signup; the mobile app is a small one-time purchase (about $2.99). A "Pro" tier is reported [3rd-party].
- Apple's privacy label says collected data is not linked to the user.
- Watch out for "Magic ToDo: GoblinX", which comes from a different publisher and charges a weekly subscription.

**Structured** [official]
- A timeline day planner.
- Pricing: Pro is sold monthly, yearly or as a lifetime purchase, with regional pricing since 2024. There is a scholarship that gives a free year to people who can't afford it.
- Recurring tasks, calendar import, Replan and AI all require Pro [3rd-party guide].

**Focusmate** [3rd-party]
- Pricing: 3 free sessions a week; Plus is about $8 a month billed annually or $12 billed monthly.
- Evidence: no peer-reviewed study of Focusmate found. CHADD states "there hasn't been significant research to validate the benefits or the dynamics" of body doubling.
- A descriptive survey by Eagle and Ringland (220 respondents) describes how people use body doubling. That paper is verified in `source/evidence_review.md` C7 (*ACM TACCESS* 2024, https://doi.org/10.1145/3689648); this pass could not locate it independently. It shows popularity, not efficacy.

**Llama Life**
- A countdown timer for each task, plus templates and chimes.
- Pricing: about $6 a month, with annual plans of roughly $39-48 (sources conflict).

**Routinery**
- A guided routine timer with voice alerts.
- Pricing: Premium subscription. The yearly US price reportedly rose from $24.99 to $39.49 in May 2026 ([apppricinglab](https://apppricinglab.com/app/apple/1450486923)).

**Finch**
- A pet-care loop rewards self-care check-ins. The core app is free; prices for Finch Plus vary.
- Reviews are mixed: ADHD users report daily motivation, but some say the pet "feels like another chore" [3rd-party].

**Habitica**
- A gamified to-do list. Party features get the most praise as accountability.
- Reported downsides are "gamification fatigue" after about a month and the overhead of the role-playing setup for people who don't play games [3rd-party roundup].
- Pricing: not verified in this pass.

#### Field-level evidence [paper]
- **Retention:** Baumel et al., *JMIR* 2019;21(9):e14567, studied 93 Android mental-health apps with at least 10K installs. Median 15-day retention was 3.9% and median 30-day retention was 3.3%. Peer-support apps (8.9%) and tracker apps (6.1%) retained better. ([JMIR](https://www.jmir.org/2019/9/e14567))
- **ADHD app reviews:** Hosseinnia et al., *Frontiers in Public Health*, 2025, found 14 studies, mostly in children, and called for long-term evidence ([link](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1483923/full)). A 2025 scoping review by Hernández-Capistrán et al. found that only 2 of 35 commercial ADHD apps had medical endorsement ([link](https://ideas.repec.org/a/taf/tbitxx/v44y2025i16p4037-4064.html)).
- **Reminder fatigue:** Ancker et al. 2017 studied clinical alerts in electronic health records (not apps). The odds of accepting a reminder fell 30% for each additional reminder in the same encounter, which points to repetition as the driver ([BMC](https://bmcmedinformdecismak.biomedcentral.com/track/pdf/10.1186/s12911-017-0430-8)). Applying this to app nudges is an inference.
- **Streak shame:** I found no peer-reviewed study. The claims come only from blogs, often written by competitors ([dev.to example](https://dev.to/nucleusos/adhd-support-app-no-streaks-why-gamification-hurts-more-than-it-helps-1ae0)).

### 3. Lessons for our bot

1. **Plan for drop-off.** Assume most users will be gone by day 30 (Baumel). Make it cheap to come back: no "you missed 5 days" messages, and re-onboarding takes one message.
2. **No streaks, and no shame.** Track what got done, not unbroken chains. The end-of-day review should ask "what went well" before "what didn't" (a design choice, not an evidence-based one).
3. **Use few nudges and vary them.** Repeating the same prompt is the strongest predictor of it being ignored (Ancker, by analogy). Let users set how often they're nudged, with a cap, and change the wording.
4. **Make claims honestly.** Inflow, the best-studied app here, has only feasibility data in a peer-reviewed journal. Don't say "treatment", "clinically proven" or "ADHD therapy". Frame the bot as a productivity aid.
5. **Keep setup short.** Several apps hide their best features behind long setup or a paywall. Onboard with about 3 questions and let the rest be learned over time.
6. **Lean on social features carefully.** Peer support retained best in Baumel, and body doubling is popular, but neither has validated outcomes. Present our body-doubling sessions as an experiment.
7. **Be cost-transparent.** Grok Bot draws on a weekly usage pool, and "each run spends usage". Every routine has a cost, so keep the default schedule small.
8. **Task breakdown is the feature people value.** Goblin Tools' Magic ToDo is widely recommended, and our "get unstuck" flowchart fits that niche.

---

## Part C: Grok Bot scheduling, verified vs unknown


Sources were fetched on 2026-10-31:
- SRA = <https://docs.x.ai/grok-bot/skills-routines-and-automations>
- FAQ = <https://docs.x.ai/grok-bot/faq>
- CA = <https://docs.x.ai/grok-bot/computer-and-apps>
- SEC = <https://docs.x.ai/grok-bot/security>
- SN = <https://docs.x.ai/grok-bot/settings-and-notifications>
- MOB = <https://docs.x.ai/grok-bot/mobile>

| Question | Status | Docs wording |
|---|---|---|
| Where routine output goes | **Verified: the Bot's chat** | "the result shows up in the Bot's chat" (SRA) |
| Push notifications | **Partly verified** | "Turn on Notifications for a Bot to get a system or mobile notification when that Bot finishes or is waiting for you." "On iPhone, push delivery is rolling out gradually." "Both device permission and the Bot's notification setting must allow the notification." (SN). **Unknown:** whether a routine result counts as "finishes". No page says so explicitly. |
| Desktop routing | Verified | While the desktop app is in use, notifications go to the desktop and "Finished replies skip your phone." (SN) |
| Bot creates a routine from chat | **Verified** | "Create and change routines by asking the Bot in chat." "The Bot creates the routine, and it appears in the Bot's routines." (SRA). Auto Review covers "automation writes (changes to routines and event triggers)" (SEC), so creating a routine may prompt for approval. |
| Recurring schedules | **Verified** | "Ask for a schedule in plain words, like 'every weekday at 8:00 AM' or 'every 2 hours.'" "Routine schedules must be at least five minutes apart." (SRA) |
| One-off schedules | **Unknown** | Not documented. "A new routine waits for its next scheduled time; it doesn't run when it's created." (SRA) |
| Timezone | **Verified** | "Schedules use the time zone in Settings, under Bot, labeled Timezone. Auto-detect follows this computer." A routine can be given a different zone (SRA). |
| Quiet hours, DND, snooze | **Unknown (not documented)** | The only controls are the per-Bot notification switch and a global phone toggle: "To stop phone alerts for every Bot, open Settings on the phone and turn off Notifications." (MOB). Related: "Grok Bot may ask whether to keep routines running ... after a long period away and pause them if there is no response." (SRA) |
| Pause or delete | **Verified** | "use the switch on the row to pause or resume it"; "Deleting a routine stops its future runs and can't be undone." (SRA). On mobile: "use Active to pause or resume", "swipe a routine in the list to delete it". "Testing a routine requires the desktop app." (MOB) |
| Limits | **Verified** | "A Bot can own up to 50 routines ... 20 most recent run records"; "all of your routines together can run up to 300 times an hour, and each routine up to 200 times an hour"; "Each run spends usage" (SRA). "Grok Bot stops when weekly usage runs out" if on-demand is off (FAQ). |
| Routines reading Sheets or Calendar | **Likely, not explicit** | Routine runs can "call connected tools" (SRA, describing test runs). Apps are connected per account (CA). No sentence names Sheets or Calendar within routines. |
| Creating Calendar events | **Capability verified; approval unknown** | "the Bot can read calendars you can see, create and update events, check free time" (CA). Whether this needs approval isn't stated. "Approvals from work that started without you, like a routine ... expire after about 30 minutes." (FAQ). For comparison, email sent from a routine "waits as a draft" and "there's no option for unattended sending" (CA). |

**Design implications:**
- Treat chat as the guaranteed channel for nudges, and push as best-effort.
- Build our own "quiet hours" into the schedule, since no DND setting exists.
- Any calendar write from a routine should be proposed in chat, not executed.

**Third-party note [unverified]:** a Cursor forum thread reports iOS pushes not arriving; staff said it had been fixed ([forum](https://forum.cursor.com/t/grok-bot-ios-1-0-push-notifications-never-arrive-even-though-notifications-are-on/168245)).

See also [research-grok-bot.md](research-grok-bot.md).
