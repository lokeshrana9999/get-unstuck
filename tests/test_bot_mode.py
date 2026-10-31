"""Bot adaptation layer: rules from docs/verdict.md as accepted in docs/verdict-response.md."""

import io
import re
import unittest

from get_unstuck import Session, load_flowchart
from get_unstuck.cli import walk
from get_unstuck.engine import HONESTY_ORDER, WELL_SUPPORTED_CLAIMS

BANNED = re.compile(r"dopamine|\bproven\b|evidence[- ]based|science[- ]backed|zeigarnik|ariely|\bjust\b|\blazy\b",
                    re.IGNORECASE)


def bot_copy(chart):
    """Every string the bot can show: (where, text)."""
    for sid, s in chart.strategies.items():
        if s["bot"]["action"] != "drop":
            yield f"strategy {sid}", chart.strategy_text(sid, bot=True)
    for nid in chart.reachable(bot=True):
        yield f"node {nid}", chart.text(nid, bot=True)
        yield f"node {nid} title", chart.title(nid, bot=True)
        for opt in chart.options(nid, bot=True):
            yield f"node {nid} option", opt["label"]


def run_bot(inputs):
    out = io.StringIO()
    walk(load_flowchart(), stdin=io.StringIO("\n".join(inputs) + "\n"), stdout=out, bot=True)
    return out.getvalue()


class OverlayDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart()

    def test_every_strategy_has_overlay(self):
        for sid, s in self.chart.strategies.items():
            self.assertIn(s["bot"]["action"], {"keep", "reword", "replace", "drop"}, sid)
            self.assertIn(s["bot"]["honesty"], HONESTY_ORDER, sid)
            if s["bot"]["action"] in ("reword", "replace"):
                self.assertTrue(s["bot"].get("text"), sid)

    def test_well_supported_needs_moderate_claim(self):
        for sid, s in self.chart.strategies.items():
            if s["bot"]["honesty"] == "well_supported":
                self.assertIn(s["evidence"]["claim"], WELL_SUPPORTED_CLAIMS, sid)

    def test_contradicted_claims_are_not_shown_as_is(self):
        for sid, s in self.chart.strategies.items():
            if s["evidence"]["claim"] in ("contradicted", "partly_contradicted"):
                self.assertNotEqual(s["bot"]["action"], "keep", sid)

    def test_verdict_drops(self):
        for sid in ("snack", "look_back", "willfulness_worksheet"):
            self.assertEqual(self.chart.strategies[sid]["bot"]["action"], "drop", sid)
        self.assertEqual(self.chart.strategies["harmless_problem"]["bot"]["action"], "replace")

    def test_chart_text_is_untouched(self):
        s = self.chart.strategies
        self.assertEqual(s["accommodate_task"]["text"], "Accomodate the task to make it less bad")
        self.assertIn("fit the facts", s["dbt_skills"]["text"])
        self.assertIn("toss phone", s["harmless_problem"]["text"])
        self.assertEqual(self.chart.node("diy_dopamine")["title"], "DIY DOPAMINE")

    def test_bot_copy_has_no_banned_words(self):
        for where, text in bot_copy(self.chart):
            self.assertIsNone(BANNED.search(text), f"{where}: {text!r}")

    def test_bot_copy_spelling_and_dbt_name(self):
        texts = " ".join(t for _, t in bot_copy(self.chart))
        self.assertNotIn("Accomodate", texts)
        self.assertNotIn("fit the facts", texts)
        self.assertIn("Check the facts", texts)

    def test_unsafe_hack_never_reaches_bot_copy(self):
        texts = " ".join(t for _, t in bot_copy(self.chart)).lower()
        for phrase in ("toss phone", "knock over water", "delicious snack"):
            self.assertNotIn(phrase, texts)

    def test_if_then_plan_is_default_output(self):
        for sid in ("smallest_step", "reschedule"):
            self.assertIn("At [time], at [place], I will", self.chart.strategy_text(sid, bot=True), sid)


class BotFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart()

    def test_bot_mode_can_always_finish(self):
        for nid in self.chart.reachable(bot=True):
            self.assertTrue(self.chart.can_finish(nid, bot=True), nid)

    def test_worried_about_failing_goes_to_break_it_down(self):
        s = Session(self.chart, current="why_bad", bot=True)
        s.choose(1)
        self.assertEqual(s.current, "break_it_down")
        chart_s = Session(self.chart, current="why_bad")
        chart_s.choose(1)
        self.assertEqual(chart_s.current, "go_step4")

    def test_comic_exchange_is_one_round(self):
        s = Session(self.chart, current="comic_go_step4", bot=True)
        s.choose(1)  # refuse once
        self.assertEqual(s.current, "comic_fine")
        s.choose(0)
        self.assertEqual(s.current, "radical_acceptance")
        self.assertNotIn("comic_willfulness", self.chart.reachable(bot=True))

    def test_loop_cap_offers_step5_on_repeat(self):
        s = Session(self.chart, current="step4", bot=True)
        s.choose(0)  # Yes -> go_again (1st visit)
        self.assertEqual(len(s.options()), 1)
        s.choose(0)  # -> step1
        s.current = "step4"
        s.choose(0)  # go_again again (2nd visit)
        first = s.options()[0]
        self.assertEqual(first["to"], "step5")
        s.choose(0)
        self.assertEqual(s.current, "step5")

    def test_tips_lead_with_best_supported(self):
        order = [self.chart.strategies[s]["bot"]["honesty"]
                 for s in self.chart.node_strategies("resist_impulses", bot=True)]
        self.assertEqual(order, sorted(order, key=HONESTY_ORDER.index))
        self.assertEqual(order[0], "well_supported")
        self.assertNotIn("look_back", self.chart.node_strategies("resist_impulses", bot=True))

    def test_bot_walk_renders_adaptation(self):
        # step1 Yes, step2 No, step3 inertia, "unstuck but need help" -> Quick reset, quit
        out = run_bot(["1", "2", "1", "1", "q"])
        self.assertIn("Mode: bot adaptation", out)
        self.assertIn("== QUICK RESET ==", out)
        self.assertIn("(a hack some people like)", out)
        self.assertNotIn("Delicious snack", out)
        self.assertNotIn("DIY DOPAMINE", out)
        self.assertIn("TOO HARD / AFRAID I'LL FAIL", out)


if __name__ == "__main__":
    unittest.main()
