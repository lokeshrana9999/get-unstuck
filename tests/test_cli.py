"""Engine and CLI behaviour tests (no terminal needed)."""

import contextlib
import io
import unittest

from get_unstuck import Session, load_flowchart
from get_unstuck.cli import main, walk
from get_unstuck.safety import mentions_crisis


def run_walk(inputs, **kwargs):
    out = io.StringIO()
    code = walk(load_flowchart(), stdin=io.StringIO("\n".join(inputs) + "\n"), stdout=out, **kwargs)
    return code, out.getvalue()


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.chart = load_flowchart()

    def test_happy_path(self):
        s = Session(self.chart)
        s.choose(0)  # Yes! -> step2
        s.choose(0)  # Yes! -> hell_yeah
        self.assertTrue(s.finished)
        self.assertEqual(s.current, "hell_yeah")

    def test_back_and_bad_choice(self):
        s = Session(self.chart)
        s.choose(1)
        self.assertEqual(s.current, "prioritize")
        self.assertTrue(s.back())
        self.assertEqual(s.current, "step1")
        self.assertFalse(s.back())
        with self.assertRaises(IndexError):
            s.choose(99)

    def test_redirect_continues(self):
        s = Session(self.chart, current="great_job_step2")
        self.assertEqual(len(s.options()), 1)
        s.choose(0)
        self.assertEqual(s.current, "step2")

    def test_loop_detection(self):
        s = Session(self.chart)
        for _ in range(3):  # step1 -> prioritize -> great_job_step2 -> ... back to step1 via revisit
            s.choose(1)  # prioritize
            s.choose(1)  # still don't know -> break_it_down
            s.choose(1)  # still don't know -> revisit_step1
            s.choose(0)  # -> step1
        self.assertTrue(s.looping())

    def test_unknown_start(self):
        with self.assertRaises(KeyError):
            Session(self.chart, current="nope")


class WalkTests(unittest.TestCase):
    def test_full_walk_to_radical_acceptance(self):
        # step1 Yes, step2 No, step3 impulse, can't resist, refuse x3, Fine (enter)
        code, out = run_walk(["1", "2", "2", "3", "2", "2", "2", ""])
        self.assertEqual(code, 0)
        self.assertIn("RESIST IMPULSES", out)
        self.assertIn("Fine.", out)
        self.assertIn("Practice radical acceptance", out)
        self.assertIn("not medical", out)

    def test_evidence_and_safety_shown(self):
        code, out = run_walk(["1", "2", "1", "3", "q"], show_evidence=True)
        self.assertIn("INTERRUPT INERTIA", out)
        self.assertIn("[evidence:", out)
        self.assertIn("Safety:", out)
        self.assertIn("Bot version (replace, not chart text): Set a timer", out)

    def test_invalid_input_and_quit(self):
        code, out = run_walk(["banana", "9", "q"])
        self.assertEqual(code, 0)
        self.assertIn("Please type a number", out)
        self.assertIn("Come back any time", out)

    def test_eof_exits_cleanly(self):
        out = io.StringIO()
        self.assertEqual(walk(load_flowchart(), stdin=io.StringIO(""), stdout=out), 0)

    def test_crisis_text_shows_helplines_and_does_not_advance(self):
        code, out = run_walk(["I want to kill myself", "q"])
        self.assertIn("14416", out)
        self.assertIn("988", out)
        self.assertEqual(out.count("Do you know what you need to do?"), 2)


class SafetyTests(unittest.TestCase):
    def test_mentions_crisis(self):
        for text in ["i want to die", "thinking about SUICIDE", "I keep hurting myself", "self-harm"]:
            self.assertTrue(mentions_crisis(text), text)
        for text in ["1", "I'm dying to finish this", "kill this task", ""]:
            self.assertFalse(mentions_crisis(text), text)


class MainTests(unittest.TestCase):
    def test_validate_command(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["validate"]), 0)
        self.assertIn("OK", out.getvalue())

    def test_list_command(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["list"]), 0)
        self.assertIn("hell_yeah", out.getvalue())


if __name__ == "__main__":
    unittest.main()
