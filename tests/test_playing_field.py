# pylint: disable=C
import unittest
from collections import Counter
from source.playing_field import get_playing_field

class TestGeneratePlayingField(unittest.TestCase):
    def test_field_size(self):
        field = get_playing_field()
        self.assertEqual(len(field), 5)  # Check rows
        for row in field:
            self.assertEqual(len(row), 5)  # Check columns

    def test_field_content(self):
        field = get_playing_field()
        flat_list = [cell for row in field for cell in row]
        count = Counter(flat_list)
        self.assertEqual(count[1], 5)
        self.assertEqual(count[0], 20)

    def test_randomness(self):
        fields = [tuple(map(tuple, get_playing_field())) for _ in range(10)]
        unique_fields = set(fields)
        self.assertGreater(len(unique_fields), 1)  # Erwartet, dass nicht alle Felder gleich sind


if __name__ == "__main__":
    unittest.main()
