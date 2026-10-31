"""Interactive terminal walker.

Usage:
    python -m get_unstuck                 # walk the chart from Step 1
    python -m get_unstuck --evidence      # also show evidence levels per tip
    python -m get_unstuck --start step3   # jump to a node
    python -m get_unstuck validate        # check data/flowchart.json integrity
    python -m get_unstuck list            # list node ids
"""

from __future__ import annotations

import argparse
import sys
import textwrap
from typing import Optional, TextIO

from . import __version__
from .engine import Flowchart, Session, load_flowchart
from .safety import CRISIS_MESSAGE, DISCLAIMER, mentions_crisis

HELP = "Type a number to choose, 'b' to go back, 'q' to quit, '?' for help."
LEVEL_LABELS = {
    "moderate_strong": "moderate-strong",
    "weak_moderate": "weak-moderate",
    "partly_contradicted": "partly contradicted",
    "not_testable": "not testable",
    "not_reviewed": "not reviewed",
}


def _level(name: str) -> str:
    return LEVEL_LABELS.get(name, name)


def _wrap(text: str, indent: str = "") -> str:
    return textwrap.fill(text, width=78, initial_indent=indent, subsequent_indent=indent + "  ")


def render_node(chart: Flowchart, session: Session, show_evidence: bool) -> str:
    node = session.node
    lines = []
    header = node.get("title") or ""
    if node.get("step"):
        header = f"Step {node['step']}" + (f" - {header}" if header else "")
    if header:
        lines.append(f"== {header} ==")
    if node.get("text"):
        lines.append(_wrap(node["text"]))
    for sid in node.get("strategies", []):
        strat = chart.strategies[sid]
        # Don't repeat a strategy whose text is the node's own text.
        if strat["text"] != node.get("text"):
            lines.append(_wrap("- " + strat["text"], "  "))
        if show_evidence:
            ev = strat["evidence"]
            lines.append(_wrap(
                f"[evidence: tip {_level(ev['claim'])}; nearest principle {_level(ev['principle'])}; "
                f"see evidence_review.md {', '.join(ev['refs'])}]", "    "))
        if strat.get("safety"):
            lines.append(_wrap("Safety: " + strat["safety"], "    "))
        if strat.get("bot_tip"):
            lines.append(_wrap("Tip (not from the chart): " + strat["bot_tip"], "    "))
    if session.looping() and not session.finished:
        lines.append(_wrap(
            "(You've been here a few times. That's okay. If you keep looping, "
            "Step 5 helps you decide what to do about the task itself.)"))
    for i, opt in enumerate(session.options(), 1):
        mark = " *" if opt.get("interpretive") else ""
        lines.append(_wrap(f"{i}) {opt['label']}{mark}", "  "))
    return "\n".join(lines)


def walk(chart: Flowchart, start: Optional[str] = None, show_evidence: bool = False,
         stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout) -> int:
    session = Session(chart, current=start or "")

    def say(text: str = "") -> None:
        print(text, file=stdout)

    say(DISCLAIMER)
    say(HELP)
    while True:
        say()
        say(render_node(chart, session, show_evidence))
        if session.finished:
            say()
            say("That's the end of this path. Be kind to yourself, whatever happens next.")
            return 0
        print("> ", end="", file=stdout, flush=True)
        raw = stdin.readline()
        if not raw:  # EOF
            say()
            return 0
        answer = raw.strip()
        if mentions_crisis(answer):
            say()
            say(CRISIS_MESSAGE)
            continue
        low = answer.lower()
        if low in ("q", "quit", "exit"):
            say("Okay. Come back any time.")
            return 0
        if low in ("?", "h", "help"):
            say(HELP + " Options marked * are not chart text.")
            continue
        if low in ("b", "back"):
            if not session.back():
                say("You're at the start already.")
            continue
        if answer == "" and len(session.options()) == 1:
            session.choose(0)
            continue
        try:
            session.choose(int(answer) - 1)
        except (ValueError, IndexError):
            say(f"Please type a number from 1 to {len(session.options())}.")


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(prog="get_unstuck", description="Walk the Get Unstuck flowchart.")
    parser.add_argument("command", nargs="?", default="walk", choices=["walk", "validate", "list"])
    parser.add_argument("--data", help="path to flowchart.json (default: data/flowchart.json)")
    parser.add_argument("--start", help="node id to start from (default: step1)")
    parser.add_argument("--evidence", action="store_true", help="show evidence levels for each tip")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    chart = load_flowchart(args.data)
    if args.command == "validate":
        errors = chart.validate()
        for err in errors:
            print("ERROR:", err)
        print(f"{len(chart.nodes)} nodes, {len(chart.strategies)} strategies: "
              + ("OK" if not errors else f"{len(errors)} problem(s)"))
        return 1 if errors else 0
    if args.command == "list":
        for nid, node in chart.nodes.items():
            print(f"{nid:20} {node['type']:9} {node.get('title') or node.get('text', '')}")
        return 0
    if args.start and args.start not in chart.nodes:
        parser.error(f"unknown node '{args.start}'")
    return walk(chart, start=args.start, show_evidence=args.evidence)
