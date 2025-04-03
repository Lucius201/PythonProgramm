"""Main Module Des Spiels"""


def main() -> None:
    """main funktion des Spiels"""
    from get_playing_field import get_playing_field
    from print_field_as_table import print_field_as_table
    from win_condition import win_condition
    from get_end_screen_field import get_end_screen_field

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
                print("Schwierigkeit: einfach\n")
                bomb_count = 4
            case "n":
                print("Schwierigkeit: normal\n")
                bomb_count = 6
            case "s":
                print("Schwierigkeit: schwer\n")
                bomb_count = 10
            case _:
                print("Ungültige Angabe. Schwierigkeit auf 'normal' gesetzt.\n")

        playing_field = get_playing_field(bomb_count)
        playing_field = [
            [0, 1, 9, 2, 1],
            [0, 1, 1, 3, 9],
            [0, 0, 0, 3, 9],
            [0, 1, 1, 4, 9],
            [0, 1, 9, 3, 9],
        ]

        while not win_condition(shown_field, bomb_count):
            print("\n" * 15)

            if error_message:
                print(error_message + "\n")
                error_message = ""

            print_field_as_table(shown_field)

            chosen_cell = input().lower()
            row_numbers = [int(c) for c in list(chosen_cell) if c.isdigit()]
            column_chars = [c for c in list(chosen_cell) if not c.isdigit()]

            if not chosen_cell:
                error_message = "Bitte eine Koordinate eingeben. z.B: (a1, c2, e4, d1)"
                continue

            if column_chars[0] == "q":
                break

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
            break


if __name__ == "__main__":
    main()
