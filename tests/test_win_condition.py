import unittest
from source.win_condition import win_condition


class TestWinCondition(unittest.TestCase):
    def test_win_condition_with_five_unrevealed(self):
        shown_field = [
            ["x", "x", "x", "x", "x"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
        ]
        self.assertTrue(win_condition(shown_field))

    def test_win_condition_with_more_than_five_unrevealed(self):
        shown_field = [
            ["x", "x", "x", "x", "x"],
            ["x", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
        ]
        self.assertFalse(win_condition(shown_field))

    def test_win_condition_with_no_unrevealed(self):
        shown_field = [
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
        ]
        self.assertTrue(win_condition(shown_field))

    def test_win_condition_with_exactly_five_unrevealed(self):
        shown_field = [
            ["x", "x", "x", "x", "x"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
        ]
        self.assertTrue(win_condition(shown_field))


if __name__ == "__main__":
    unittest.main()
