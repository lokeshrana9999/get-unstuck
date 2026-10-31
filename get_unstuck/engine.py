"""Load, validate and walk data/flowchart.json. Standard library only."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

NODE_TYPES = {"question", "strategy", "redirect", "terminal"}
CONTINUE_LABEL = "OK, continue"


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

    def options(self, node_id: str) -> List[Dict[str, Any]]:
        """Choices for a node. Redirects get one synthetic 'continue' option."""
        node = self.nodes[node_id]
        if node["type"] == "redirect":
            return [{"label": CONTINUE_LABEL, "to": node["next"], "interpretive": True}]
        return list(node.get("options", []))

    def targets(self, node_id: str) -> List[str]:
        return [opt["to"] for opt in self.options(node_id)]

    def reachable(self, start: Optional[str] = None) -> set:
        seen, stack = set(), [start or self.start]
        while stack:
            nid = stack.pop()
            if nid in seen or nid not in self.nodes:
                continue
            seen.add(nid)
            stack.extend(self.targets(nid))
        return seen

    def can_finish(self, node_id: str) -> bool:
        return any(self.nodes[n]["type"] == "terminal" for n in self.reachable(node_id))

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
                for target in self.targets(nid):
                    if target not in self.nodes:
                        errors.append(f"node '{nid}': option points to missing node '{target}'")
        if errors:
            return errors
        for sid in sorted(set(self.strategies) - used):
            errors.append(f"strategy '{sid}' is never used by a node")
        reach = self.reachable()
        for nid in sorted(set(self.nodes) - reach):
            errors.append(f"node '{nid}' is unreachable from start")
        for nid in sorted(reach):
            if not self.can_finish(nid):
                errors.append(f"node '{nid}' cannot reach any terminal (trap loop)")
        return errors


@dataclass
class Session:
    """One walk through the flowchart, with history for 'back'."""

    chart: Flowchart
    current: str = ""
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
        return [] if self.finished else self.chart.options(self.current)

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
