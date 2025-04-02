"""Kreaiert das fertige Feld mit "x" als Bomben"""

from typing import List


def get_end_screen_field(numbers_field: List[List[int]]) -> List[List[str]]:
    """Macht das Nummer Feld schön für die Losing Page"""
    end_screen_field = []
    for row in numbers_field:
        result_row = []
        for c in row:
            if c == 9:
                result_row.append("x")
            else:
                result_row.append(str(c))
        end_screen_field.append(result_row)
    return end_screen_field
