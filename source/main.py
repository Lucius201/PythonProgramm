"""Main Module Des Spiels"""

from get_playing_field import get_playing_field
from get_field_numbers import get_field_numbers
from print_field_as_table import print_field_as_table
from win_condition import win_condition


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
    error_message = ""
    print("Willkommen in SweeperMine. Deine Aufgabe ist es Felder aufzudecken.")
    print("Decke Felder auf indem du die Koordinaten angibst: (A1, C5, ...)\n")
    while True:
        while not win_condition(shown_field):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if error_message:
                print(error_message + "\n")
                error_message = ""
            print_field_as_table(shown_field)

            chosen_cell = input().lower()
            row_numbers = [int(c) for c in list(chosen_cell) if c.isdigit()]
            column_chars = [c for c in list(chosen_cell) if not c.isdigit()]

            if column_chars[0] == "q":
                break

            try:
                chosen_row = allowed_numbers[row_numbers[0]]
                chosen_column = allowed_characters[column_chars[0]]

                if numbers_field[chosen_row][chosen_column] == 9:

                    print("Verloren!")
                    # print_field_as_table(playing_field)

                    playing_field = get_playing_field()
                    numbers_field = get_field_numbers(playing_field)
                    shown_field = [
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                    ]
                    break

                else:
                    shown_field[chosen_row][chosen_column] = str(
                        numbers_field[chosen_row][chosen_column]
                    )

            except:
                error_message = "Ungültige Eingabe"

        if win_condition(shown_field):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print_field_as_table(shown_field)
            print("Gewonnen!\n")
        end_screen_input = input("Nochmal spielen? (y/n)\n").lower()
        if end_screen_input == "n" or end_screen_input == "q":
            break
        else:
            continue


if __name__ == "__main__":
    main()
