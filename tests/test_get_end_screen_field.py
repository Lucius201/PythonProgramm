# pylint: disable=C
import unittest
from get_end_screen_field import get_end_screen_field


class TestEndScreenField(unittest.TestCase):
    def test_bomb_conversion(self):
        """Testet, dass 9er zu "x" verwandelt werden"""
        input_field = [[9, 1, 0], [2, 9, 3], [4, 5, 9]]
        expected_output = [["x", "1", "0"], ["2", "x", "3"], ["4", "5", "x"]]
        self.assertEqual(get_end_screen_field(input_field), expected_output)

    def test_number_conversion(self):
        """Testet, dass aus Integer Strings gemacht werden"""
        input_field = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expected_output = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
        self.assertEqual(get_end_screen_field(input_field), expected_output)


if __name__ == "__main__":
    unittest.main()
