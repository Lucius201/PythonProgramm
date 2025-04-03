"""Das Modul erstellt das 5x5 Spielfeld."""

import random
from typing import List


def get_playing_field(bomb_count: int) -> List[List[int]]:
    """Generiert ein 5x5 Spielfeld mit eingetragenen Nummern"""
    playing_field_list = []
    binary_playing_field = []

    for i in range(bomb_count):
        playing_field_list.append(0)
    for i in range(25 - bomb_count):
        playing_field_list.append(1)

    random.shuffle(playing_field_list)
    for i in range(5):
        binary_playing_field.append(playing_field_list[i * 5 : i * 5 + 5])

    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    result = []
    current_row = 0
    current_column = 0

    for row in binary_playing_field:
        result_row = []
        for cell in row:
            bomb_count = 0
            for direction in directions:
                search_column = current_column + direction[0]
                search_row = current_row + direction[1]
                if search_row >= 5 or search_row < 0:
                    continue
                if search_column >= 5 or search_column < 0:
                    continue
                if binary_playing_field[search_row][search_column] == 0:
                    bomb_count += 1

            if cell == 0:
                result_row.append(9)
            else:
                result_row.append(bomb_count)

            current_column += 1
        result.append(result_row)
        current_row += 1
        current_column = 0
    return result


if __name__ == "__main__":
    print(get_playing_field(6))
