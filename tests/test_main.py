# pylint: disable=C
import unittest
from unittest.mock import patch
from source.main import main


class TestMainFunction(unittest.TestCase):

    @patch("builtins.input", side_effect=["q", "q"])
    @patch("builtins.print")
    def test_main_quit_early(self, mock_print, mock_input):
        """Testet ein Exit Vorgang"""
        try:
            main()
        except SystemExit:
            self.fail("main() exited unexpectedly")

    @patch(
        "source.get_playing_field.get_playing_field",
        return_value=[
            [0, 1, 9, 2, 1],
            [0, 1, 1, 3, 9],
            [0, 0, 0, 3, 9],
            [0, 1, 1, 3, 9],
            [0, 1, 9, 2, 1],
        ],
    )
    @patch(
        "builtins.input",
        side_effect=[
            "a1",
            "a2",
            "a3",
            "a4",
            "a5",
            "b1",
            "b2",
            "b3",
            "b4",
            "b5",
            "c2",
            "c3",
            "c4",
            "d1",
            "d2",
            "d3",
            "d4",
            "d5",
            "e1",
            "e5",
            "n",
        ],
    )
    @patch("builtins.print")
    def test_main_win_condition(self, mock_print, mock_input, mock_field):
        """Testet ein Gewinnen Durchlauf (print von "Gewonnen")"""
        try:
            main()
        except SystemExit:
            self.fail("main() exited unexpectedly")

        printed_output = "".join(str(call) for call in mock_print.call_args_list)
        self.assertIn("Gewonnen", printed_output)

    @patch(
        "source.get_playing_field.get_playing_field",
        return_value=[
            [0, 1, 9, 2, 1],
            [0, 1, 1, 3, 9],
            [0, 0, 0, 3, 9],
            [0, 1, 1, 3, 9],
            [0, 1, 9, 2, 1],
        ],
    )
    @patch("builtins.input", side_effect=["c1", "n"])
    @patch("builtins.print")
    def test_main_lose_condition(self, mock_print, mock_input, mock_field):
        """Test, dass das Game "Verloren" printet wenn die Bombe gescannt wird"""
        try:
            main()
        except SystemExit:
            self.fail("main() exited unexpectedly")

        printed_output = "".join(str(call) for call in mock_print.call_args_list)
        self.assertIn("Verloren", printed_output)


if __name__ == "__main__":
    unittest.main()
