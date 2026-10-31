# Research: Grok Bot and Grok Build

*Researched 2026-10-31. Both products are new and change quickly. Check the linked pages before you rely on any detail here.*

This note covers what Get Unstuck can actually use. Every claim links to a source. Each claim's confidence is marked as one of:

- **[docs]**: stated on an official xAI page that was fetched.
- **[absence]**: an official page was read and the feature isn't mentioned there. This doesn't prove the feature doesn't exist.
- **[unverified]**: seen only in third-party pages or search snippets.

Nothing here is invented. Where something isn't known, it says so.

---

## 1. Grok Bot (the assistant app)

### What it is
- Grok Bot is a team of "always-on agents". Each Bot has its own memory and chats, and all your Bots share one persistent cloud computer with a browser, filesystem and terminal. Bots can work in parallel and hand off tasks. **[docs]** <https://docs.x.ai/grok-bot>
- It launched in beta on 2026-08-11, on macOS and iOS first. **[docs]** <https://x.ai/news/introducing-grok-bot>
- The desktop app now runs on macOS, Windows and Linux. The mobile app runs on iPhone, iPad and Android. **[docs]** <https://docs.x.ai/grok-bot/faq>
- The docs mention Cursor in several places. For example, Bots' computers run in Cursor's cloud, and Grok Bot is included with paid Cursor plans. We have not confirmed the business relationship between xAI and Cursor. **[docs]** for the mentions; the relationship is **[unverified]**. <https://docs.x.ai/grok-bot/faq>

### How a Bot is defined (this matters for `bot/persona.md`)
- Each Bot has a **name**, a **picture** (under 25 MB) and a **label**. On the phone, the label is called the **Title**. **[docs]** <https://docs.x.ai/grok-bot/bots>
- **There is no persona or instructions field.** Personal Bots "no longer have a description or a Bot settings page". Instead, your first message should "give the Bot its job, sources, and approval boundaries, and ask it to remember them". **[docs]** <https://docs.x.ai/grok-bot/bots>
- **Shared** Bots do have a description, which the owner or a Manager edits under *About*. **[docs]** <https://docs.x.ai/grok-bot/bots>
- No character limits are documented for the name, label or description. **[absence]** We still keep the name descriptive and the label short, because listings may truncate them.

**Consequence:** `bot/persona.md` is written as four parts: a name, a label, a description (for shared Bots and templates), and a **first-message setup prompt** that sets the persona and boundaries and asks the Bot to remember them.

### Skills
- "A skill is a reusable set of instructions for how to do a task. A skill captures steps, decision rules, expected output, and safety boundaries." **[docs]** <https://docs.x.ai/grok-bot/skills-routines-and-automations>
- You can create a skill by asking the Bot in chat (for example, "Save the process we just used as a skill called …"). You can also teach it a browser workflow by demonstration, which produces a draft skill. **[docs]** (same page)
- All your Bots share one private skill library. A skill needs a description before you can publish it to a team. **[docs]** (same page)
- **The Grok Bot docs don't document a skill file format.** They don't mention SKILL.md either. **[absence]**

**Consequence:** `bot/skills/*/SKILL.md` uses the SKILL.md layout from Grok Build (below), which is also the common Agent Skills layout. These files are **portable drafts**. For now, we plan to bring them into Grok Bot by pasting each one into chat and asking the Bot to "save this as a skill". We don't know whether a direct import exists.

### Routines
- Schedules are written in plain language (for example "every weekday at 8:00 AM"). They use the timezone in Settings, must be at least 5 minutes apart, and a new routine waits for its next scheduled time. **[docs]** <https://docs.x.ai/grok-bot/skills-routines-and-automations>
- Routines can also be triggered by Slack, GitHub, Linear, Sentry, PagerDuty, email to the Bot's address, or a webhook (`Authorization: Bearer <key>`). **[docs]** (same page)
- Limits: 50 routines per Bot, 20 run records kept per routine, 300 runs per hour across all routines, and 200 per hour per routine. **[docs]** (same page)

### Connectors ("apps")
- The docs name these apps: Google Calendar, Google Sheets, Google Drive, Gmail, Slack, X, an agent email address, 1Password and SharePoint. You can also add custom MCP servers. **[docs]** <https://docs.x.ai/grok-bot/computer-and-apps>
- **Google Sheets:** the Bot can read spreadsheets the connected account can open, and it can edit cells. A file shared as Viewer stays view-only. It uses Drive to find files. **[docs]** (same page)
- Apps are connected per account, so every Bot can use them. A Google Workspace admin may need to approve the app first. **[docs]** (same page)

### Permissions and safety controls
- Approval cards offer *Allow once*, *Always allow* or *Deny*. An optional **Auto Review** model can allow, ask about or deny risky actions. **[docs]** <https://docs.x.ai/grok-bot/security>
- Email sent from a routine stays a draft until you press Send. Bots act as the signed-in user and never get more access than that user has. **[docs]** (same page)

**Consequence for `bot/guardrails.md`:** we add our own rule that the Bot takes no outbound action without an explicit "yes" from the user. We don't rely only on the platform's approval cards, because "Always allow" can be switched on.

### Sharing and templates
- A **template** shares the Bot's "identity, description, skills, and routines". It never includes your computer, logins or conversation history. **[docs]** <https://docs.x.ai/grok-bot/bots>
- To publish one: Share → Create a copy → Publish → Copy link. Recipients see a preview on x.ai and choose *Add to Grok Bot*. You can update or delete a template later. **[docs]** (same page)
- Admins control whether members can share templates publicly. **[docs]** <https://docs.x.ai/grok-bot/teams-and-enterprises>
- There's a *Bot templates* gallery under Connect apps. **[docs]** <https://docs.x.ai/grok-bot/bots>. **We don't know whether that gallery is curated or open to submissions. [unverified]**

### Pricing and availability
- Grok Bot has no standalone subscription. It's included with X Premium, Super and Ultra, with paid Cursor plans, or by linking a SuperGrok or X Premium+ subscription. Usage draws on a weekly pool. **[docs]** <https://docs.x.ai/grok-bot/faq>

---

## 2. Grok Build (xAI's coding-agent CLI)

**URL note:** <https://docs.x.ai/build> returned **404** when we checked. The subpages load, for example <https://docs.x.ai/build/overview>.

- "Grok Build is a powerful and extensible coding agent." It runs as an interactive terminal UI or headless. **[docs]** <https://docs.x.ai/build/overview>. ACP support appears only in a search snippet. **[unverified]**
- **Install:**
  - macOS/Linux: `curl -fsSL https://x.ai/cli/install.sh | bash`
  - Windows: `irm https://x.ai/cli/install.ps1 | iex`
  - Sign in through the browser, or set `XAI_API_KEY`. The CLI provides `grok login` (`--device-auth` for headless machines) and `grok logout`.
  - **[docs]** <https://docs.x.ai/build/overview>, <https://docs.x.ai/build/cli/reference>
- **Modes and commands:** the modes are Plan, Auto and Always-approve. Slash commands include `/plan`, `/agents`, `/personas`, `/skills`, `/plugins`, `/mcps`, `/hooks` and `/import-claude`. **[docs]** <https://docs.x.ai/build/modes-and-commands>
- **Config:** settings live in `~/.grok/config.toml` and in a project-level `.grok/config.toml`. It reads AGENTS.md, CLAUDE.md, `.grok/rules/*.md` and similar instruction files. **[docs]** <https://docs.x.ai/build/settings>, <https://docs.x.ai/build/features/project-rules>
- **Skills:** each skill is a `SKILL.md` file with YAML frontmatter. Fields include `name`, `description`, `when-to-use`, `paths`, `allowed-tools`, `argument-hint`, `user-invocable`, `disable-model-invocation` and `metadata`. Skills live in `.grok/skills/` or `~/.grok/skills/`. The docs say Grok Build is compatible with Claude Code skills and plugins. **[docs]** <https://docs.x.ai/build/features/skills-plugins-marketplaces>
- **No Bot scaffolding or publishing commands are documented.** **[absence]** <https://docs.x.ai/build/cli/reference>

**Consequence:** Grok Build is useful for *developing this repo* (for example running tests, or editing skills as SKILL.md). It can't create or publish the Grok Bot itself. Publishing happens in the Grok Bot app through templates.

---

## 3. How this shapes the project

| Repo artifact | Grok Bot concept | Confidence |
|---|---|---|
| `bot/persona.md` name, label, description | Bot name and label; shared-Bot or template description | docs |
| `bot/persona.md` setup prompt | First message plus "remember" (no persona field exists) | docs |
| `bot/skills/*/SKILL.md` | Skills, saved by pasting into chat; file import unknown | docs (concept); format unverified |
| `bot/routines.md` | Plain-language scheduled routines | docs |
| `docs/sheet-design.md` | Google Sheets app (read and edit cells) | docs |
| `bot/guardrails.md` | Our own rules, layered on approval cards and Auto Review | docs |
| Shareable bot | Template link (identity, description, skills, routines) | docs |

## 4. Open questions

1. Can a SKILL.md file be imported into Grok Bot directly, or do we have to paste it into chat?
2. Are there character limits on Bot names, labels, template descriptions or skill descriptions?
3. Is the *Bot templates* gallery curated? Can a community template be listed there?
4. Can a routine's message prompt a mobile push notification? Do routines respect quiet hours?
5. Does Google Sheets access support appending rows, or only editing cells? (The docs say "edit cells".)
6. The latest changelog (<https://x.ai/changelog/bot>) returned 403 and wasn't reviewed.

## 5. Sources consulted

Fetched successfully:
- <https://docs.x.ai/grok-bot>
- <https://docs.x.ai/grok-bot/bots>
- <https://docs.x.ai/grok-bot/skills-routines-and-automations>
- <https://docs.x.ai/grok-bot/computer-and-apps>
- <https://docs.x.ai/grok-bot/shared-bots>
- <https://docs.x.ai/grok-bot/security>
- <https://docs.x.ai/grok-bot/faq>
- <https://docs.x.ai/grok-bot/teams-and-enterprises>
- <https://x.ai/news/introducing-grok-bot>
- <https://docs.x.ai/llms.txt>
- <https://docs.x.ai/build/overview>
- <https://docs.x.ai/build/features/skills-plugins-marketplaces>
- <https://docs.x.ai/build/cli/reference>
- <https://docs.x.ai/build/settings>
- <https://docs.x.ai/build/features/subagents>
- <https://docs.x.ai/build/features/project-rules>
- <https://docs.x.ai/build/modes-and-commands>

Failed:
- <https://docs.x.ai/build> (404)
- <https://x.ai/changelog/bot> (403)

Seen only in search results, not relied on: third-party guides such as flaviocopes.com, mindstudio.ai, composio.dev and verdent.ai.
