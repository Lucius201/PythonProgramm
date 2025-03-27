"""Dieses Modul bestimmt die Nummern der einzelnen Felder"""

field = [
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
]


def get_field_numbers(field) -> list:
    """Diese Funktion bildet das Feld mit Nummern"""
    print(field)
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    result = []
    current_row = 0
    current_column = 0

    for row in field:
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
                if field[search_row][search_column] == 0:
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
    print(get_field_numbers(field))
