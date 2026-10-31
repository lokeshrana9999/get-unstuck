# Action plan: building the Get Unstuck Grok Bot

*Merged 2026-10-31 from four parallel planning passes:*
- *[01 content & evidence](action-plan/01-content-evidence.md)*
- *[02 safety & guardrails](action-plan/02-safety-guardrails.md)*
- *[03 Grok Bot implementation](action-plan/03-grokbot-implementation.md)*
- *[04 testing & launch](action-plan/04-testing-launch.md)*

*The part files have the full steps. This document covers order, owners, gates and risks. It is driven by [verdict.md](verdict.md) and [verdict-response.md](verdict-response.md). It replaces the milestone list in [PLAN.md](PLAN.md) as the working plan.*

**Owners:**
- **Bot**: work an AI agent can do in this repo (drafting, code, tests, docs).
- **Lokesh**: human decisions and everything done in the Grok Bot app.

Task IDs point to the part files: C = content, S = safety, I = implementation, T = testing.

**Ground rules:**
- **Fixes go into the repo first, then into the app.** Never edit only in the app.
- Never claim platform features that [research-grok-bot.md](research-grok-bot.md) doesn't verify.
- No bot is created until Phase 3.

---

## Phase 0: Baseline ✅ (done in this pass)

| Item | Where |
|---|---|
| Bot adaptation layer: every strategy has a `bot` overlay (keep / reword / replace / drop, plus an honesty tag). Nodes have `bot_title`, `bot_text` and `bot_repeat_next`; options have `bot_label` and `bot_to`. Chart text is unchanged. | `data/flowchart.json` v0.2.0, schema |
| The verdict's drops (unsafe hack, snack, "look back", willfulness worksheet) and rewords (Quick reset, Pause and reflect, Check the facts, noise rather than music, small immediate rewards, 10–20 min movement, swap the reward, if-then rescheduling, "just" removed) | overlays |
| Reroutes: "worried I'll fail" → BREAK IT DOWN; the comic exchange is one round; the loop cap offers Step ⑤ on a second pass | `bot_to`, `bot_repeat_next` |
| `--bot` CLI mode: honesty-ordered tips, dropped tips hidden, tags shown in plain words | `get_unstuck/` |
| Tests: honesty ceiling, contradicted claims never kept as-is, banned words in bot copy ("dopamine", "proven", "evidence-based", "just", "lazy", Zeigarnik, Ariely), unsafe hack absent, bot-mode reachability | `tests/test_bot_mode.py` |
| Guardrails: don't assume ADHD; movement only if safe; don't push food; ≤ 3 check-ins a day; banned claims made absolute (closes the §5 conflict found in C-02); Tele-MANAS toll-free number added to the template reply (found in S-01) | `bot/guardrails.md` |
| Persona, skills and routines updated: best-supported first, friction first for impulses, if-then plan as the default close, "Half-ass it" offered earlier, "adapted from" credit | `bot/` |

---

## Phase 1: Decisions (Lokesh), blocks Phase 3

| ID | Decision | Recommendation | Ref |
|---|---|---|---|
| D-1 | The 5 ambiguous routings, plus the `go_again` target: confirm, change, or accept as `most_likely` | Accept the breakdown readings. Two are overridden in the bot anyway. | C-01 |
| D-2 | Keep the name "Get Unstuck: Task Starter for ADHD & Executive Dysfunction"? | Keep it, **only if** the T-08 gate passes. Otherwise use "Get Unstuck: Task Starter". | verdict §3, T-08 |
| D-3 | Honesty-tag wording users see, and how often it's shown | Current tags, shown on first mention and whenever the user asks | C-05 |
| D-4 | "Half-ass it" or "do a good-enough version"? | Use "good-enough version" in prompts, and keep "Half-ass it" as the playful endpoint | C-07 |
| D-5 | Connect Gmail, Slack or X in v1? | **No.** Drafts in chat only. Sheets is optional. | S-04 |
| D-6 | Adults-only beta, and how to say so | Yes. State it in the consent note and the template description. | S-06/R-06, T-07 |
| D-7 | Default state store | Memory, opt-in. The Sheet is for people who want history. | I-09 |
| D-8 | A private beta feedback channel, since GitHub issues are public | A private form, with the issue template kept as a fallback | T-07 |
| D-9 | Commit `build/kit/` or build it only at release? | Commit it, so non-developers can copy-paste | I-01 |
| D-10 | Who besides Lokesh can pull the template; a 72-hour safety-fix target | Name a backup person, or accept "delete the template" as the fallback | S-08, T-10 |

**Exit:** each decision recorded, dated, in `docs/decisions.md` (to be created).

---

## Phase 2: Repo hardening before any build (mostly Bot)

| ID | Task | Owner | Acceptance | Prio |
|---|---|---|---|---|
| C-01b | Record D-1 per option as a `decision` field and apply `review_v2.md` "still to fix" 1–6 to `breakdown_v2.md` | Bot | A test fails if any `most_likely` option has no decision | P0 |
| C-02 | Audit all 50 overlays against `evidence_review.md` | Bot drafts, Lokesh signs | Audit table has zero open rows; ceiling tests pass | P0 |
| C-03 / T-03 | Shame-word lint across bot copy **and** skills (allowlist for lines that forbid a word) | Bot | Lint in CI. *Bot copy part done; skills part open.* | P0 |
| C-04 | One canonical if-then template with rules and an event-cue fallback | Bot | A test checks the slots in every if-then overlay | P0 |
| C-05 | Implement the D-3 wording, plus a one-line "why?" answer per tag | Bot | `--bot` prints the approved phrases | P0 |
| S-01 / T-04 | Crisis-line table `docs/safety-tests/crisis-lines.md` (source URL, date, checker); test that every number appears in every location | Bot builds, **Lokesh verifies** | Every row checked within 90 days; presence test in CI | P0 |
| S-02 | Region handling: help is never gated on a question; findahelpline.com first when the region is unknown | Bot | R-01–R-03 pass | P0 |
| S-03 / T-06 | Red-team suite R-01…R-12 plus 3–5 scripted dialogues per skill in `docs/safety-tests/` and `docs/transcripts/SCRIPTS.md`, with the 0–2 rubric | Bot | Files exist, each with pass criteria | P0 |
| S-04 | Per-action confirm card in guardrails §3 ("one yes = one action") | Bot | Card text present; tested in Phase 3 | P0 |
| S-05 | Routine audit table: sends per day for each routine, ≤ 3 in total; "stop / pause / fewer" take effect at once | Bot | Table in `routines.md` | P0 |
| S-06 | Document the keyword limits; ≥ 5 expected-fail tests | Bot | README and `safety.py` say "not a safety system" | P0 |
| I-01 / I-02 | `tools/build_kit.py` builds paste-ready setup prompt, profile, skills (from SKILL.md plus overlays), routines and a MANIFEST; `--check` catches a stale kit; kit tests | Bot | Deterministic; banned words absent; well-supported tips first; crisis numbers match; CI runs `--check` | P0 |
| T-01 / T-02 | Golden `--bot` transcripts (≥ 10 paths) and a `bot_copy.json` snapshot | Bot | Copy or routing changes show up as reviewed diffs | P0 |
| T-05 | Offline relative-link checker in CI; external links opt-in | Bot | A broken link fails CI | P1 |
| C-06 | 28 illustrative dialogues (7 skills × happy / loop / refusal / distress) | Bot, 3 testers review | They pass C-03 and C-05; testers rate them warm and short | P1 |
| C-07 | "Good-enough version" offered early; end-of-session plan in every skill | Bot | Visible in the C-06 dialogues. *Skills done.* | P1 |
| C-09 | Record the `evidence_review.md` revision date in `meta`; banned-citations list in CI | Bot | Stale refs or banned citations fail CI. *Refs test exists.* | P1 |

**Exit (gate to Phase 3):** CI is green with the kit, golden, lint and crisis tests, and every P0 row is done.

---

## Phase 3: Spike, then build in Grok Bot (Lokesh, with the Bot preparing materials)

| ID | Task | Acceptance |
|---|---|---|
| I-03 | **Spike on a throwaway Bot.** Test SKILL.md import, truncation of the longest skill, Sheets append vs cells only, a routine at night or quiet hours, and what a template carries from a second account. Log the results, dated, in `research-grok-bot.md`. | The decision table in part 03 is resolved for U1–U7 |
| I-04 | Create the Bot: name and label (D-2), an original picture (never the chart image), paste `setup-prompt.txt` | In a new chat, the Bot restates the no-diagnosis, crisis and explicit-yes rules |
| I-05 | Add the 7 skills from the kit, in order | All 7 are in the library with descriptions; MANIFEST hashes recorded |
| I-06 / T-06 / S-03 | Run all scripts and red-team prompts in fresh chats, with *Always allow* **on** for the consent tests. Store scrubbed transcripts in `docs/transcripts/`. | Every script scores ≥ 8/10; **Safety = 2 on every safety case**; loop cap, one-round comic exchange, fail-worry reroute and if-then close all observed |
| I-07 | Routines R1–R5, all off by default | A fresh Bot or template has no active routines |
| I-08 / I-09 | Optional Sheet per `sheet-design.md`; document memory vs Sheet | Nothing is written without a "yes"; "stop logging" works; view-only case handled |

**Exit:** every safety case passes in the app, and all fixes are back-ported to the repo and kit.

---

## Phase 4: Private beta (Lokesh, with Bot support)

| ID | Task | Acceptance |
|---|---|---|
| T-07 | 5–10 adult testers for 2 weeks via template link; consent note (`docs/beta/consent.md`); feedback form with **no health fields** | ≥ 5 report; ≥ 50% of sessions end in "started" or "rescheduled with a plan"; median helpfulness ≥ 4/5; **zero safety incidents**. Any incident pauses the beta. |
| S-07 | Privacy: sensitivity warning at opt-in; "delete my log"; no health details in memory or the Sheet; template preview has no history | "I take 20 mg…" never reaches a proposed Sheet row |
| S-08 | Incident-response runbook, plus one dry run | Dry run logged |
| S-09 / C-11 | Lived-experience reader, and ideally a clinician, review the crisis reply, R-05, R-07 and the audit table | Each comment accepted or rejected with a reason |
| C-08 | Find the chart author; request permission **covering the adaptations** (generated from the overlay diff) | Written permission, **or** a dated attempt log plus "adapted from; author unknown" |

---

## Phase 5: Public template (go/no-go)

**T-08 gate:** every box must be ticked. Lokesh signs.
- [ ] Verdict §4a drops and §4b rewords visible in `bot_copy.json`.
- [ ] §4c additions live: if-then output, fail-worry reroute, assessment nudge, honesty tags, "adapted from" credit.
- [ ] §4d guardrails pass in the app (Phase 3).
- [ ] §4e routings decided (D-1), and the loop and comic caps confirmed.
- [ ] Crisis numbers re-verified **within the last 7 days**; external link check clean.
- [ ] Description says "a structured coaching flow built on reasonable principles", with no "evidence-based" or "proven".
- [ ] **Name rule:** if anything above is open, rename or don't publish (verdict §3).

Then:
- **T-09 / I-10:** SemVer bump of `meta.version`, CHANGELOG entry, git tag `vX.Y.Z`. Rebuild the kit, re-paste only the changed skills, re-run the safety scripts, and **update** the existing template (don't publish a new one). Put the version in the template description and the link in the README.
- **I-11:** document the rollback in CONTRIBUTING and dry-run it once.

---

## Phase 6: After launch

| ID | Task | Cadence |
|---|---|---|
| T-10 | Triage feedback (safety / fidelity / tone / idea); safety items get a patch within 72 h plus a new red-team case | Weekly |
| S-01, T-10 | Re-verify crisis lines, check external links, re-read the Grok Bot docs | Monthly (crisis lines at least quarterly) |
| C-10 | Retraction watch on cited DOIs; re-tag overlays if a rating changes | Quarterly |
| S-11 | Re-run the red-team suite after platform or model changes | Quarterly and on change |
| T-11 / I-11 | Rollback from the last good tag; delete the template on a severe issue; sunset plan. *Note: whether copies people already added are affected is unknown.* | As needed |
| I-12 / T-12 | Gallery submission, only if submissions turn out to be possible | After T-08 |
| S-10, S-12, I-13 | Hindi crisis reply (native-speaker checked); quiet hours if supported; per-release kit diff | Later |

---

## Top risks (consolidated)

| # | Risk | Likelihood / impact | Mitigation | Tasks |
|---|---|---|---|---|
| 1 | Missed indirect crisis signal | Med / **High** | Prompt-level rules, many-phrasing red-team cases, keywords only as a floor | S-03, S-06, T-06 |
| 2 | "Always allow" or Auto Review bypasses consent | Med / High | Per-action yes in the setup prompt, tested with Always allow on; no Gmail/Slack/X in v1 | S-04, D-5 |
| 3 | Bot copy drifts from the tested data (edits made in the app) | High / Med | Build kit with `--check`, golden snapshots, repo-first fixes | I-01, T-01, T-02 |
| 4 | Users read tags as "proven for me" | Med / Med | Honest wording, banned claims, honest pitch | C-05, guardrails §5 |
| 5 | Stale crisis numbers | Low / High | Dated table, a 7-day check before launch, monthly re-check | S-01 |
| 6 | Platform unknowns (skill import, truncation, Sheets append, template memory) | High / Med | Spike first; decision table; paste fallback | I-03 |
| 7 | Chart author objects to the adaptation | Low / Med | Ask early with the diff; faithful layer kept; ready to rename or withdraw | C-08 |
| 8 | Health data ends up in public issues or the Sheet | Med / Med | Forms with no health fields, consent note, minimal columns, opt-in | S-07, T-07 |
| 9 | Prompt injection via Sheet cells, email or webhook | Low / High | Treat app content as data; R-10 | S-03 |
| 10 | Evidence review drifts or a citation is retracted | Med / Low | Refs tests, banned-citations list, quarterly watch | C-09, C-10 |

## Open questions (rolled up)

Decisions D-1 to D-10 above, plus the following:
- Whether template updates or deletions reach copies already added (T-11).
- Whether a clinician reviewer is realistic before launch (S-09).
- Which beta regions need extra crisis lines (S-01).
- Whether to ask for the timezone and quiet window in the setup prompt or in R1 (I-03).
