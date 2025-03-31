"""Main Module Des Spiels"""

from get_playing_field import get_playing_field
from get_field_numbers import get_field_numbers
from print_field_as_table import print_field_as_table


def main():
    """main funktion des Spiels"""
    playing_field = get_playing_field()
    numbers_field = get_field_numbers(playing_field)
    # print_field_as_table(playing_field)
    # print_field_as_table(numbers_field)
    allowed_characters = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
    }
    allowed_numbers = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    shown_field = [
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
    ]
    print("Willkommen in SweeperMine. Deine Aufgabe ist es Felder aufzudecken.")
    print("Decke Felder auf indem du die Koordinaten angibst: (A1, C5, ...)\n")

    while True:
        print_field_as_table(shown_field)

        chosen_cell = input().lower()
        row_numbers = [int(c) for c in list(chosen_cell) if c.isdigit()]
        column_chars = [c for c in list(chosen_cell) if not c.isdigit()]
        # print(column_chars, row_numbers)
        try:
            chosen_row = allowed_numbers[row_numbers[0]]
            chosen_column = allowed_characters[column_chars[0]]
            # print(chosen_column, chosen_row)
            # print_field_as_table(numbers_field)
            # print(numbers_field[chosen_row][chosen_column])
            if numbers_field[chosen_row][chosen_column] == 9:
                print("Verloren!")
                print_field_as_table(playing_field)
                playing_field = get_playing_field()
                numbers_field = get_field_numbers(playing_field)
                shown_field = [
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                ]
            else:
                shown_field[chosen_row][chosen_column] = str(
                    numbers_field[chosen_row][chosen_column]
                )

        except:
            print("Ungültige Eingabe")


if __name__ == "__main__":
    main()
