"""Data tests: integrity, schema, and fidelity to source/breakdown_v2.md + review_v2.md."""

import json
import unittest
from pathlib import Path

from get_unstuck import load_flowchart

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "flowchart.json"
SCHEMA = ROOT / "data" / "flowchart.schema.json"

try:
    import jsonschema  # optional; installed in CI
except ImportError:  # pragma: no cover
    jsonschema = None


def option_to(chart, node_id, label_prefix):
    for opt in chart.options(node_id):
        if opt["label"].startswith(label_prefix):
            return opt
    raise AssertionError(f"{node_id}: no option starting with {label_prefix!r}")


class IntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart(DATA)

    def test_validate_reports_no_errors(self):
        self.assertEqual(self.chart.validate(), [])

    def test_every_node_is_reachable_and_can_finish(self):
        self.assertEqual(self.chart.reachable(), set(self.chart.nodes))
        for nid in self.chart.nodes:
            self.assertTrue(self.chart.can_finish(nid), nid)

    def test_validate_catches_broken_link(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        data["nodes"]["step1"]["options"][0]["to"] = "nowhere"
        from get_unstuck import Flowchart
        errors = Flowchart(data).validate()
        self.assertTrue(any("missing node 'nowhere'" in e for e in errors), errors)

    def test_validate_catches_unknown_strategy_and_level(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        data["nodes"]["prioritize"]["strategies"].append("made_up")
        data["strategies"]["snack"]["evidence"]["claim"] = "amazing"
        from get_unstuck import Flowchart
        errors = Flowchart(data).validate()
        self.assertTrue(any("unknown strategy 'made_up'" in e for e in errors), errors)
        self.assertTrue(any("unknown evidence claim 'amazing'" in e for e in errors), errors)

    @unittest.skipIf(jsonschema is None, "jsonschema not installed")
    def test_matches_json_schema(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.validate(json.loads(DATA.read_text(encoding="utf-8")), schema)

    def test_schema_is_valid_json_with_expected_defs(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertIn("node", schema["$defs"])
        self.assertIn("strategy", schema["$defs"])


class FidelityTests(unittest.TestCase):
    """Routings and wording that the source documents explicitly settle."""

    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart(DATA)

    def test_step3_has_seven_reasons_with_first_line_strategies(self):
        targets = [o["to"] for o in self.chart.options("step3")]
        self.assertEqual(targets, ["interrupt_inertia", "resist_impulses", "ten_minutes",
                                   "mindfulness", "wellbeing", "break_it_down", "break_it_down"])

    def test_dotted_lines_into_break_it_down(self):
        dotted = [o for o in self.chart.options("step3") if o.get("line") == "dotted"]
        self.assertEqual(len(dotted), 2)

    def test_non_step4_fallbacks(self):
        # breakdown_v2 §1 / fixes_log B1, B4
        self.assertEqual(option_to(self.chart, "make_tolerable", "This didn't help")["to"], "diy_dopamine")
        self.assertEqual(option_to(self.chart, "mindfulness", "I still don't know")["to"], "wellbeing")
        self.assertEqual(option_to(self.chart, "break_it_down", "It still feels too hard")["to"], "wellbeing")
        self.assertEqual(option_to(self.chart, "resist_impulses", "I'm sort of resisting")["to"], "interrupt_inertia")

    def test_prioritize_only_escalates_when_still_overwhelmed(self):
        self.assertEqual(option_to(self.chart, "prioritize", "I know what")["to"], "great_job_step2")
        self.assertEqual(option_to(self.chart, "prioritize", "OVERWHELM")["to"], "break_it_down")

    def test_review_v2_ambiguous_routings_are_marked_most_likely(self):
        ambiguous = [
            ("resist_impulses", "I'm sort of resisting"),
            ("resist_impulses", "I still can't resist"),
            ("why_bad", "It's an unpleasant"),
            ("why_bad", "I'm worried"),
            ("prioritize", "I know what"),
            ("interrupt_inertia", "I can start"),
            ("step4_tried", "I may have skipped"),
        ]
        for node_id, prefix in ambiguous:
            self.assertEqual(option_to(self.chart, node_id, prefix).get("confidence"), "most_likely",
                             f"{node_id} / {prefix}")

    def test_step5_has_five_endpoints(self):
        outcomes = {n["outcome"] for n in self.chart.nodes.values()
                    if n["type"] == "terminal" and n.get("flow") == "extension-or-delegate"}
        self.assertEqual(outcomes, {"reschedule", "delegate", "partial", "accept", "push_through"})

    def test_comic_exchange_order_ends_in_radical_acceptance(self):
        path = ["comic_go_step4", "comic_willfulness", "comic_please", "comic_fine"]
        for a, b in zip(path, path[1:]):
            self.assertIn(b, self.chart.targets(a))
        self.assertEqual(self.chart.node("comic_fine")["next"], "radical_acceptance")

    def test_chart_spelling_preserved(self):
        self.assertEqual(self.chart.strategies["accommodate_task"]["text"],
                         "Accomodate the task to make it less bad")
        self.assertTrue(self.chart.strategies["look_forward"]["text"].startswith("Look forward :"))
        self.assertIn("rest sensory", option_to(self.chart, "wellbeing", "No, I need something. It's... PHYSICAL")["label"])

    def test_bullet_counts_match_chart(self):
        counts = {"make_tolerable": 7, "interrupt_inertia": 10, "diy_dopamine": 5,
                  "resist_impulses": 12, "prioritize": 2, "break_it_down": 2}
        for nid, n in counts.items():
            self.assertEqual(len(self.chart.node(nid)["strategies"]), n, nid)


class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart(DATA)

    def test_every_strategy_cites_evidence_review_sections(self):
        for sid, strat in self.chart.strategies.items():
            self.assertTrue(strat["evidence"]["refs"], sid)

    def test_key_ratings_from_evidence_review(self):
        s = self.chart.strategies
        self.assertEqual(s["snack"]["evidence"]["claim"], "contradicted")         # E2
        self.assertEqual(s["body_double"]["evidence"]["pop_science_flag"], "strong")  # C7
        self.assertEqual(s["smallest_step"]["evidence"]["claim"], "moderate")     # B3
        self.assertEqual(s["reward_after"]["evidence"]["claim"], "partly_contradicted")  # C4

    def test_risky_hack_carries_safety_note(self):
        self.assertIn("safety", self.chart.strategies["harmless_problem"])

    def test_refs_exist_in_evidence_review_if_present(self):
        review = ROOT / "source" / "evidence_review.md"
        if not review.exists():
            self.skipTest("source/evidence_review.md not present")
        text = review.read_text(encoding="utf-8")
        for sid, strat in self.chart.strategies.items():
            for ref in strat["evidence"]["refs"]:
                self.assertIn(f"### {ref}.", text, f"{sid} cites missing section {ref}")


if __name__ == "__main__":
    unittest.main()
