"""Main Module Des Spiels"""

import sys
from get_playing_field import get_playing_field
from print_field_as_table import print_field_as_table
from win_condition import win_condition
from get_end_screen_field import get_end_screen_field


def main() -> None:
    """main funktion des Spiels"""

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
        bomb_count = 6
        difficulty = input(
            "Welche Schwierigkeit wählen Sie? (e: einfach, n: normal, s: schwer)\n"
        ).lower()

        match difficulty:
            case "e":
                bomb_count = 4
                difficulty = "Einfach"
            case "n":
                bomb_count = 6
                difficulty = "Normal"
            case "s":
                bomb_count = 10
                difficulty = "Schwer"
            case _:
                difficulty = "Normal"

        playing_field = get_playing_field(bomb_count)

        while not win_condition(shown_field, bomb_count):
            print("\n" * 15)

            if difficulty:
                print("Schwierigkeit: " + difficulty + "\n")
                difficulty = ""

            if error_message:
                print(error_message + "\n")
                error_message = ""

            print_field_as_table(shown_field)

            chosen_cell = input().lower()
            row_numbers = [int(c) for c in list(chosen_cell) if c.isdigit()]
            column_chars = [c for c in list(chosen_cell) if not c.isdigit()]

            if column_chars:
                if "q" in column_chars:
                    shown_field = [
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                    ]
                    break

            if not row_numbers or not column_chars:
                error_message = "Bitte eine Koordinate eingeben. z.B: (a1, c2, e4, d1)"
                continue

            try:
                chosen_row = allowed_numbers[row_numbers[0]]
                chosen_column = allowed_characters[column_chars[0]]

                if playing_field[chosen_row][chosen_column] == 9:
                    print("\n" * 15)
                    print("Verloren!\n")
                    print_field_as_table(get_end_screen_field(playing_field))

                    shown_field = [
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x"],
                    ]
                    break

                shown_field[chosen_row][chosen_column] = str(
                    playing_field[chosen_row][chosen_column]
                )

            except:
                error_message = "Ungültige Eingabe"

        if win_condition(shown_field, bomb_count):
            print("\n" * 15)
            print_field_as_table(shown_field)
            print("Gewonnen!\n")
            shown_field = [
                ["x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x"],
            ]

        end_screen_input = input("Nochmal spielen? (y/n)\n").lower()

        if end_screen_input == "y":
            continue

        if end_screen_input in ("n", "q"):
            sys.exit(1)


if __name__ == "__main__":
    main()
