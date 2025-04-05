"""Funktion, die das Gewinnen vom Spiel bestimmt"""

from typing import List


def win_condition(shown_field: List[List[str]], bomb_count: int) -> bool:
    """Wenn nur noch 5 unaufdeckte Felder -> Spiel gewonnen"""
    x_count = 0
    for row in shown_field:
        for cell in row:
            if cell == "x":
                x_count = x_count + 1
    return x_count <= bomb_count
