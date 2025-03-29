"""Main Module Des Spiels"""

from get_playing_field import get_playing_field
from get_field_numbers import get_field_numbers
from print_field_as_table import print_field_as_table


def main():
    """main funktion des Spiels"""
    playing_field = get_playing_field()
    numbers_field = get_field_numbers(playing_field)
    shown_field = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print_field_as_table(shown_field)

    return


if __name__ == "__main__":
    main()
