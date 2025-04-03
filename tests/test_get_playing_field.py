# pylint: disable=C
import unittest
from source.get_playing_field import (
    get_playing_field,
)


class TestPlayingField(unittest.TestCase):
    def test_field_size(self):
        """Testet ob das Spielfeld 5x5 groß ist"""
        field = get_playing_field(6)
        self.assertEqual(len(field), 5)
        for row in field:
            self.assertEqual(len(row), 5)

    def test_bomb_representation(self):
        """Test ob 5 mal die 9 im Feld steht. die 9er sind die Bomben"""
        field = get_playing_field(6)
        bomb_count = sum(row.count(9) for row in field)
        self.assertEqual(bomb_count, 6)

    def test_numbers_within_range(self):
        """Testet ob nur Nummer in den Feldern stehen und zwar von 0 bis 9"""
        field = get_playing_field(6)
        for row in field:
            for cell in row:
                self.assertIn(cell, range(10))


if __name__ == "__main__":
    unittest.main()
