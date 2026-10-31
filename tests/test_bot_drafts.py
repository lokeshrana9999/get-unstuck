"""Keep bot/ drafts consistent with data/flowchart.json."""

import re
import unittest
from pathlib import Path

from get_unstuck import load_flowchart

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "bot" / "skills"
# Flowchart flows (one skill each) plus skills outside the chart.
FLOWS = {"triage", "break-it-down", "interrupt-inertia", "resist-impulses",
         "make-it-tolerable", "wellbeing-check", "extension-or-delegate"}
EXPECTED = FLOWS | {"onboarding"}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise AssertionError(f"{path}: missing YAML frontmatter")
    return m.group(1)


class SkillDraftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = load_flowchart()

    def test_one_skill_per_flow(self):
        found = {p.parent.name for p in SKILLS.glob("*/SKILL.md")}
        self.assertEqual(found, EXPECTED)

    def test_frontmatter_name_matches_folder_and_nodes_exist(self):
        covered = set()
        for path in SKILLS.glob("*/SKILL.md"):
            fm = frontmatter(path)
            self.assertRegex(fm, rf"(?m)^name: {re.escape(path.parent.name)}$")
            self.assertRegex(fm, r"(?m)^description: \S")
            nodes = re.search(r"flowchart_nodes: \[(.*?)\]", fm).group(1)
            for nid in (n.strip() for n in nodes.split(",") if n.strip()):
                self.assertIn(nid, self.chart.nodes, f"{path}: unknown node {nid}")
                covered.add(nid)
        # every flow-tagged node the bot can reach is covered by some skill
        for nid in self.chart.reachable(bot=True):
            if self.chart.node(nid).get("flow"):
                self.assertIn(nid, covered, f"node {nid} not referenced by any skill")

    def test_node_flows_are_skill_names(self):
        for nid, node in self.chart.nodes.items():
            if "flow" in node:
                self.assertIn(node["flow"], FLOWS, nid)

    def test_guardrails_include_required_items(self):
        text = (ROOT / "bot" / "guardrails.md").read_text(encoding="utf-8")
        for needle in ["not** medical", "14416", "988", "116 123", "explicit **\"yes\"**"]:
            self.assertIn(needle, text)


if __name__ == "__main__":
    unittest.main()
