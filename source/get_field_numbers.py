"""Dieses Modul bestimmt die Nummern der einzelnen Felder"""

from playing_field import get_playing_field


def get_field_numbers(field) -> list:
    """Diese Funktion bildet das Feld mit Nummern"""
    # field = get_playing_field()
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    result = []
    current_row = 0
    current_column = 0

    for row in field:
        result_row = []
        for cell in row:
            bomb_count = 0
            for direction in directions:
                # print(direction)
                search_column = current_column + direction[0]
                search_row = current_row + direction[1]
                if search_row >= 5 or search_row < 0:
                    continue
                if search_column >= 5 or search_column < 0:
                    continue
                if field[search_row][search_column] == 0:
                    bomb_count += 1
                    # print("bomb found")

                # print(search_column, search_row)
            print("BOMB COUNT: " + str(bomb_count))
            if cell == 0:
                result_row.append(9)
            else:
                result_row.append(bomb_count)

            current_column += 1
        # print(result_row)
        result.append(result_row)
        current_row += 1
        current_column = 0

    print(" ")
    print(field[0])
    print(field[1])
    print(field[2])
    print(field[3])
    print(field[4])
    print(" ")
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    print(result[4])
    return result


if __name__ == "__main__":
    get_field_numbers(get_playing_field())
