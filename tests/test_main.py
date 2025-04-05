# pylint: disable=C
import unittest
from unittest.mock import patch
from source.main import main


def win_condition_side_effect(shown_field, bomb_count):
    # Check if every cell in shown_field is "x"
    if all(cell == "x" for row in shown_field for cell in row):
        return True
    return False


class TestMainFunction(unittest.TestCase):
    """Test class"""

    def test_game_quit(self):
        with patch("builtins.input", side_effect=["n", "q", "q"]):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)

    @patch("source.main.get_playing_field")
    @patch("source.main.win_condition", return_value=True)
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("source.main.print_field_as_table")
    def test_game_win(
        self, mock_print, mock_input, mock_win_condition, mock_get_playing_field
    ):
        dummy_field = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        mock_get_playing_field.return_value = dummy_field

        with self.assertRaises(SystemExit) as exit_context:
            main()
        self.assertEqual(exit_context.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
