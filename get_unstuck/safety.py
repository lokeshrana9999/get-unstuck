"""Minimal safety layer for the prototype. Mirrors bot/guardrails.md.

Keyword matching is a crude placeholder, NOT a real risk classifier. It errs
toward showing crisis resources; it must never be the only safeguard.
"""

from __future__ import annotations

import re

DISCLAIMER = (
    "Get Unstuck is a self-help prompt based on a community flowchart. "
    "It is not medical or psychological advice, diagnosis or treatment."
)

CRISIS_MESSAGE = """\
It sounds like you might be going through something really hard. You deserve support right now.
Getting started on a task can wait. Please reach out to someone:

  India   Tele-MANAS: 14416 or 1-800-891-4416 (24/7, free)   Emergency: 112
  US      988 Suicide & Crisis Lifeline: call or text 988     Emergency: 911
  UK/IE   Samaritans: 116 123                                 Emergency: 999 / 112
  Elsewhere: https://findahelpline.com

If you are in immediate danger, call your local emergency number."""

_CRISIS_PATTERNS = [
    r"\bkill(ing)? myself\b",
    r"\bsuicid",
    r"\bend (it all|my life)\b",
    r"\bwant to die\b",
    r"\b(hurt|harm)(ing)? myself\b",
    r"\bself[- ]?harm",
    r"\bno reason to live\b",
    r"\bbetter off dead\b",
]
_CRISIS_RE = re.compile("|".join(_CRISIS_PATTERNS), re.IGNORECASE)


def mentions_crisis(text: str) -> bool:
    return bool(_CRISIS_RE.search(text or ""))
