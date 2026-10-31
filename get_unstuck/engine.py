"""Load, validate and walk data/flowchart.json. Standard library only."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

NODE_TYPES = {"question", "strategy", "redirect", "terminal"}
CONTINUE_LABEL = "OK, continue"
# Bot mode leads with the best-supported tips (verdict §4e.2).
HONESTY_ORDER = ["well_supported", "reasonable_untested", "hack", "not_supported"]
# A strategy may only be tagged well_supported if its own claim is at least moderate.
WELL_SUPPORTED_CLAIMS = {"strong", "moderate_strong", "moderate"}


def default_data_path() -> Path:
    return Path(__file__).resolve().parent.parent / "data" / "flowchart.json"


def load_flowchart(path: Optional[Path] = None) -> "Flowchart":
    path = Path(path) if path else default_data_path()
    with path.open(encoding="utf-8") as f:
        return Flowchart(json.load(f))


class Flowchart:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.nodes: Dict[str, Dict[str, Any]] = data.get("nodes", {})
        self.strategies: Dict[str, Dict[str, Any]] = data.get("strategies", {})
        self.start: str = data.get("start", "")

    def node(self, node_id: str) -> Dict[str, Any]:
        return self.nodes[node_id]

    def options(self, node_id: str, bot: bool = False) -> List[Dict[str, Any]]:
        """Choices for a node. Redirects get one synthetic 'continue' option.

        In bot mode, option labels and targets use the bot overlay
        (bot_label / bot_to) where present.
        """
        node = self.nodes[node_id]
        if node["type"] == "redirect":
            return [{"label": CONTINUE_LABEL, "to": node["next"], "interpretive": True}]
        opts = [dict(opt) for opt in node.get("options", [])]
        if bot:
            for opt in opts:
                opt["label"] = opt.get("bot_label", opt["label"])
                opt["to"] = opt.get("bot_to", opt["to"])
        return opts

    def targets(self, node_id: str, bot: bool = False) -> List[str]:
        targets = [opt["to"] for opt in self.options(node_id, bot)]
        if bot and "bot_repeat_next" in self.nodes[node_id]:
            targets.append(self.nodes[node_id]["bot_repeat_next"])
        return targets

    def text(self, node_id: str, bot: bool = False) -> str:
        node = self.nodes[node_id]
        return (node.get("bot_text") if bot else None) or node.get("text", "")

    def title(self, node_id: str, bot: bool = False) -> str:
        node = self.nodes[node_id]
        return (node.get("bot_title") if bot else None) or node.get("title", "")

    def node_strategies(self, node_id: str, bot: bool = False) -> List[str]:
        """Strategy ids for a node. Bot mode hides dropped tips and leads with the best supported."""
        sids = list(self.nodes[node_id].get("strategies", []))
        if not bot:
            return sids
        sids = [s for s in sids if self.strategies[s]["bot"]["action"] != "drop"]
        return sorted(sids, key=lambda s: HONESTY_ORDER.index(self.strategies[s]["bot"]["honesty"]))

    def strategy_text(self, sid: str, bot: bool = False) -> str:
        strat = self.strategies[sid]
        return (strat["bot"].get("text") if bot else None) or strat["text"]

    def reachable(self, start: Optional[str] = None, bot: bool = False) -> set:
        seen, stack = set(), [start or self.start]
        while stack:
            nid = stack.pop()
            if nid in seen or nid not in self.nodes:
                continue
            seen.add(nid)
            stack.extend(self.targets(nid, bot))
        return seen

    def can_finish(self, node_id: str, bot: bool = False) -> bool:
        return any(self.nodes[n]["type"] == "terminal" for n in self.reachable(node_id, bot))

    def validate(self) -> List[str]:
        """Return a list of integrity problems (empty means OK).

        This checks graph integrity, which a JSON Schema cannot express.
        Shape checks live in data/flowchart.schema.json.
        """
        errors: List[str] = []
        if self.start not in self.nodes:
            errors.append(f"start node '{self.start}' does not exist")
        levels = set(self.data.get("evidence_levels", {}))
        for sid, strat in self.strategies.items():
            ev = strat.get("evidence", {})
            for key in ("claim", "principle"):
                if ev.get(key) not in levels:
                    errors.append(f"strategy '{sid}': unknown evidence {key} '{ev.get(key)}'")
            bot = strat.get("bot")
            if not bot:
                errors.append(f"strategy '{sid}': missing bot overlay")
            elif bot.get("honesty") not in HONESTY_ORDER:
                errors.append(f"strategy '{sid}': unknown honesty tag '{bot.get('honesty')}'")
            elif bot["honesty"] == "well_supported" and ev.get("claim") not in WELL_SUPPORTED_CLAIMS:
                errors.append(f"strategy '{sid}': tagged well_supported but claim is '{ev.get('claim')}'")
        used = set()
        for nid, node in self.nodes.items():
            ntype = node.get("type")
            if ntype not in NODE_TYPES:
                errors.append(f"node '{nid}': unknown type '{ntype}'")
                continue
            if ntype in ("question", "strategy") and not node.get("options"):
                errors.append(f"node '{nid}': {ntype} needs options")
            if ntype == "redirect" and "next" not in node:
                errors.append(f"node '{nid}': redirect needs 'next'")
            if ntype == "terminal" and (node.get("options") or node.get("next")):
                errors.append(f"node '{nid}': terminal must not have options or next")
            for sid in node.get("strategies", []):
                used.add(sid)
                if sid not in self.strategies:
                    errors.append(f"node '{nid}': unknown strategy '{sid}'")
            if ntype != "terminal":
                for target in set(self.targets(nid)) | set(self.targets(nid, bot=True)):
                    if target not in self.nodes:
                        errors.append(f"node '{nid}': option points to missing node '{target}'")
        if errors:
            return errors
        for sid in sorted(set(self.strategies) - used):
            errors.append(f"strategy '{sid}' is never used by a node")
        reach = self.reachable()
        for nid in sorted(set(self.nodes) - reach):
            errors.append(f"node '{nid}' is unreachable from start")
        for bot in (False, True):
            mode = "bot mode" if bot else "chart mode"
            for nid in sorted(self.reachable(bot=bot)):
                if not self.can_finish(nid, bot):
                    errors.append(f"node '{nid}' cannot reach any terminal in {mode} (trap loop)")
        return errors


@dataclass
class Session:
    """One walk through the flowchart, with history for 'back'."""

    chart: Flowchart
    current: str = ""
    bot: bool = False
    history: List[str] = field(default_factory=list)
    visits: Dict[str, int] = field(default_factory=dict)

    def __post_init__(self):
        if not self.current:
            self.current = self.chart.start
        if self.current not in self.chart.nodes:
            raise KeyError(f"unknown node '{self.current}'")
        self._visit(self.current)

    def _visit(self, nid: str) -> None:
        self.visits[nid] = self.visits.get(nid, 0) + 1

    @property
    def node(self) -> Dict[str, Any]:
        return self.chart.node(self.current)

    @property
    def finished(self) -> bool:
        return self.node["type"] == "terminal"

    def options(self) -> List[Dict[str, Any]]:
        if self.finished:
            return []
        opts = self.chart.options(self.current, self.bot)
        repeat_next = self.node.get("bot_repeat_next")
        # Bot loop cap (verdict §4e.3): on a repeat visit, offer the cap target first.
        if self.bot and repeat_next and self.visits.get(self.current, 0) >= 2:
            label = "Let's look at what to do about the task itself (Step 5)"
            opts = [{"label": label, "to": repeat_next, "interpretive": True}] + opts
        return opts

    def choose(self, index: int) -> str:
        """Pick option by 0-based index; returns the new node id."""
        opts = self.options()
        if not 0 <= index < len(opts):
            raise IndexError(f"choice {index + 1} is out of range (1-{len(opts)})")
        self.history.append(self.current)
        self.current = opts[index]["to"]
        self._visit(self.current)
        return self.current

    def back(self) -> bool:
        if not self.history:
            return False
        self.current = self.history.pop()
        return True

    def looping(self, threshold: int = 3) -> bool:
        """True once the walker has returned to the current node `threshold` times."""
        return self.visits.get(self.current, 0) >= threshold
