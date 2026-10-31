"""Guards for the productivity pivot (docs/PIVOT.md): drafts must keep the agreed design rules."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def quoted_bot_lines(text):
    """Example lines the bot would say: markdown blockquotes."""
    return [line for line in text.splitlines() if line.lstrip().startswith(">")]


GUILT = re.compile(r"you missed|again\?|you promised|streak (lost|broken)|last chance|final reminder",
                   re.IGNORECASE)
BANNED = re.compile(r"dopamine|\bproven\b|evidence[- ]based|\blazy\b", re.IGNORECASE)


class RoutineDesignTests(unittest.TestCase):
    def setUp(self):
        self.text = read("bot/routines.md")
        self.headings = [l for l in self.text.splitlines() if l.startswith("#")]

    def test_required_sections(self):
        for word in ("Cadence", "Quiet hours", "Snooze", "Escalation limits", "Opt-out"):
            self.assertTrue(any(word in h for h in self.headings), f"missing section: {word}")

    def test_core_limits_stated(self):
        self.assertIn("21:00", self.text)
        self.assertIn("hard ceiling", self.text)
        self.assertRegex(self.text, r"at most 3 proactive contacts a day")
        self.assertRegex(self.text, r"(?i)at most 2 snoozes")

    def test_opt_in_and_nudge_only(self):
        self.assertIn("Every routine is opt-in, off by default, and only sends a nudge.", self.text)


class GuardrailPivotTests(unittest.TestCase):
    def test_proactive_messaging_section(self):
        text = read("bot/guardrails.md")
        self.assertRegex(text, r"(?m)^## 8\. Proactive messaging")
        for needle in ("21:00", "hard ceiling", "Requested follow-ups"):
            self.assertIn(needle, text)


class OnboardingAndPersonaTests(unittest.TestCase):
    def test_onboarding_core_flow(self):
        text = read("bot/skills/onboarding/SKILL.md")
        for needle in ("quiet hours", "[started] [snooze] [stuck] [skip]", "explicit **\"yes\"**"):
            self.assertIn(needle.lower(), text.lower(), needle)
        # canonical if-then template; the time slot may carry an event-cue variant
        self.assertRegex(text, r"At \[time[^\]]*\], at \[place\], I will")

    def test_persona_setup_prompt(self):
        text = read("bot/persona.md")
        self.assertIn("Get Unstuck: Task Starter for ADHD & Executive Dysfunction", text)  # not renamed
        prompt = text.split("```text", 1)[1].split("```", 1)[0]
        for needle in ("onboarding", "14416", "988", "116 123", "remember"):
            self.assertIn(needle, prompt, needle)

    def test_example_lines_have_no_banned_or_guilt_words(self):
        for rel in ("bot/persona.md", "bot/skills/onboarding/SKILL.md", "bot/routines.md"):
            for line in quoted_bot_lines(read(rel)):
                self.assertIsNone(BANNED.search(line), f"{rel}: {line}")
                self.assertIsNone(GUILT.search(line), f"{rel}: {line}")


class SheetAndDocsTests(unittest.TestCase):
    def test_sheet_tabs_and_no_shame_streaks(self):
        text = read("docs/sheet-design.md")
        for tab in ("`Goals`", "`Tasks`", "`Check-ins`", "`Sessions`", "`Wins`", "`Settings`", "`Summary`"):
            self.assertIn(tab, text)
        self.assertIn("Streaks without shame", text)

    def test_naming_has_three_options_and_no_rename(self):
        text = read("docs/naming.md")
        self.assertEqual(len(re.findall(r"(?m)^## Option [123]: \S", text)), 3)
        self.assertIn("No rename has been made", text)

    def test_research_doc_is_sourced_and_flags_weak_evidence(self):
        text = read("docs/research-adhd-productivity.md")
        for part in ("## Part A", "## Part B", "## Part C"):
            self.assertIn(part, text)
        for app in ("Tiimo", "Inflow", "Goblin Tools", "Structured"):
            self.assertIn(app, text)
        self.assertGreaterEqual(len(re.findall(r"https://doi\.org/10\.", text)), 15)
        self.assertIn("unverified", text.lower())
        self.assertIn("Weak/contested evidence flags", text)


if __name__ == "__main__":
    unittest.main()
