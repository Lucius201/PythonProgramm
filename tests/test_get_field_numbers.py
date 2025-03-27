import unittest
from source.get_field_numbers import get_field_numbers


class TestGetFieldNumbers5x5(unittest.TestCase):
    def test_all_ones_5x5(self):
        field = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(get_field_numbers(field), expected)

    def test_all_zeros_5x5(self):
        field = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        self.assertEqual(get_field_numbers(field), expected)

    def test_checkerboard_pattern(self):
        field = [
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
        ]
        expected = [
            [2, 9, 3, 9, 2],
            [9, 4, 9, 4, 9],
            [3, 9, 4, 9, 3],
            [9, 4, 9, 4, 9],
            [2, 9, 3, 9, 2],
        ]
        self.assertEqual(get_field_numbers(field), expected)

    def test_single_bomb_center(self):
        field = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 9, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(get_field_numbers(field), expected)

    def test_bombs_on_edges(self):
        field = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [
            [9, 9, 9, 9, 9],
            [9, 5, 3, 5, 9],
            [9, 3, 0, 3, 9],
            [9, 5, 3, 5, 9],
            [9, 9, 9, 9, 9],
        ]
        self.assertEqual(get_field_numbers(field), expected)


if __name__ == "__main__":
    unittest.main()
