# 03. Grok Bot implementation

**Scope:** load the `bot/` drafts into Grok Bot (PLAN.md M4, plus template steps from M5/M6). All in-app copy is generated from the repo so it can't drift from the tested `flowchart.json` bot overlays. Chart content and evidence decisions are out of scope.

## Platform assumptions ([research-grok-bot.md](../research-grok-bot.md) only)

**Verified:**
- There is no persona field. The Bot is set up by a first message plus "remember".
- A Bot has a name, a label and a picture (under 25 MB).
- Skills are saved through chat or by demonstration. A skill needs a description to be published.
- Routines use plain-language schedules at least 5 minutes apart. Limits: 50 per Bot, 200 runs/h per routine, 300 runs/h in total.
- The Sheets app reads Sheets and edits cells.
- Approval cards can be set to "Always allow".
- Templates carry identity, description, skills and routines. A published template can be updated or deleted.
- Grok Build has no Bot scaffolding.

**Unknown:**
- U1: whether SKILL.md files can be imported.
- U2: character limits.
- U3: whether the Sheets app can append rows.
- U4: whether routines get quiet hours or push notifications.
- U5: whether the template gallery accepts submissions.
- U6: anything in the changelog (it returned 403).
- U7: whether a template carries the remembered setup prompt ("identity" isn't defined).

## Tasks

Owners: **Bot** is AI agent work in the repo. **Lokesh** is work in the Grok Bot app.

### P0

**I-01 Build kit script** (Bot)
- `tools/build_kit.py` writes these files to `build/kit/`:
  - `setup-prompt.txt`, taken from persona.md;
  - `profile.txt`;
  - `skills/<name>.txt`: the SKILL.md body with the overlay text (`bot.text`, `bot_title`, `bot_label`) in place of chart wording, tips sorted by honesty tag, `drop` tips removed, and the whole thing wrapped in "Save this as a skill called <name>. Description: …";
  - `routines/<id>.txt`;
  - `MANIFEST.json`, with `meta.version`, the git SHA and a sha256 for each file.
- A `--check` flag fails when the kit is stale.
- **Accept when:** output is deterministic, and every skill file has a save line and a description.

**I-02 Kit test** (Bot)
- `tests/test_build_kit.py` checks:
  - the kit has no "dopamine", "proven" or "evidence-based";
  - the unsafe hack and the snack tip are absent;
  - `well_supported` tips come before `hack` tips;
  - the crisis numbers equal those in guardrails.md;
  - the kit isn't stale;
  - each file is under `MAX_CHARS`, which is set from I-03.
- **Accept when:** it passes in CI.

**I-03 Spike** (Lokesh, using a throwaway Bot)
- Try to import a SKILL.md file.
- Paste the longest skill, reopen it and diff it against the kit.
- Ask the Bot to add a row below existing data in a test Sheet.
- Set a routine for the middle of the night.
- Publish a template and add it from a second account.
- Log the results, dated, in the research doc.

| Outcome | Decision |
|---|---|
| Import works | The kit also ships raw SKILL.md files. Pasting stays the fallback. |
| No import | Paste the kit text (the default). |
| Truncated or paraphrased | Set `MAX_CHARS`. Split skills (for example triage Steps 1–2 / 3). Ask the Bot to save "verbatim". |
| Append works | Use the write protocol as written. |
| Cells only | Read column A, then write to the first empty row (the sheet-design.md fallback). |
| No quiet hours | The user picks routine times. The setup prompt asks for their quiet window. |
| Template drops the setup memory | The template description says "paste the setup prompt first" and links to the kit. |

**I-04 Create Bot and setup** (Lokesh)
- Set the name, label and an original picture from `profile.txt`.
- Paste `setup-prompt.txt`.
- In a new chat, ask "What are your boundaries?"
- **Accept when:** the Bot restates the no-diagnosis, crisis and explicit-yes rules.

**I-05 Add skills** (Lokesh)
- Paste them in this order: triage, break-it-down, interrupt-inertia, resist-impulses, make-it-tolerable, wellbeing-check, extension-or-delegate.
- **Accept when:** all seven are in the library with descriptions, and the MANIFEST hashes are recorded.

**I-06 In-app test run** (Lokesh runs it; Bot prepares the script)
- Run the M2 dialogues and the M3 red-team prompts.
- Include these cases:
  - the loop cap offers Step ⑤;
  - the comic exchange runs one round only;
  - "worried I'll fail" leads to break-it-down;
  - the session ends with an if-then plan.
- **Accept when:** every safety case passes. Fixes go into the repo and kit, never only into the app.

### P1

**I-07 Routines, off by default** (Lokesh)
- R1 is added only when the user asks for it.
- R2 and R3 are one-off routines, created after the user says "yes".
- R4 and R5 are added only after I-08.
- **Accept when:** a fresh Bot or template has no active routines.

**I-08 Optional Sheet** (Lokesh)
- Create `Get Unstuck log` from sheet-design.md and connect Sheets.
- Test:
  - show the row, then write it only after "yes";
  - "stop logging";
  - the view-only case.
- **Accept when:** nothing is written without a "yes".

**I-09 Memory vs Sheet** (Bot)
- Document in sheet-design.md:
  - **Default to memory, opt-in only** ("Want me to remember this for the 3 PM check-in?"). This is enough for R2 and R3.
  - **The Sheet is for users who want history.** It is required for R4 and R5, and it is the only store the user can inspect and delete row by row.
  - No health details go in either store.

**I-10 Template and versioning** (Lokesh; Bot drafts the notes)
- Publish: Share → Create a copy → Publish → Copy link.
- Put `vX.Y.Z` in the template description and the link in the README.
- On each release (`meta.version` bump plus CHANGELOG):
  - rebuild the kit;
  - re-paste only the skills whose MANIFEST entries changed;
  - rerun I-06;
  - **update** the existing template. Never publish a new one.
- **Accept when:** the template version, the MANIFEST and the git tag all match.

**I-11 Rollback** (Lokesh + Bot)
- Steps:
  1. Check out the previous tag and run `build_kit.py`.
  2. Re-paste the affected skills, replacing them by name, and the setup prompt.
  3. Update the template.
- On a safety regression:
  - turn off routines first;
  - delete the template if you can't fix it quickly.
- **Accept when:** this is documented in CONTRIBUTING.md and has been dry-run once.

### P2
- **I-12** Gallery submission, only if U5 allows it (Lokesh).
- **I-13** A per-release kit diff listing which skills to re-paste (Bot).

## Risks

| Risk | Mitigation |
|---|---|
| Edits made in the app drift from the repo | Edit only the kit. `--check` runs in CI. |
| Skills get truncated or paraphrased | I-03 diff, `MAX_CHARS`, split skills |
| "Always allow" skips approval | Explicit-yes rule in the setup prompt; tested in I-06 |
| The template drops the setup memory | Covered by the I-03 decision table |
| Beta platform changes | Re-run the spike each release, with dated notes |
| Task names in the Sheet are sensitive | Opt-in, the user owns it, minimal columns |

## Open questions for Lokesh
1. Should `build/kit/` be committed so non-developers can copy it, or built only at release?
2. Which account do you publish from? Do admin sharing controls apply?
3. Should the timezone and quiet window be asked for in the setup prompt or in R1?
4. Is memory acceptable as the default state store?
5. Do you keep the current Bot name (verdict-response §8)?
