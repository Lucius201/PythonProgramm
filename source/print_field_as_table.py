"""Printet das Spielfeld"""

from typing import List


def print_field_as_table(field: List[List[int]]) -> None:
    """Nimmt Spielffeld als Liste als Parameter und printet Spielfeld"""
    print("   A B C D E\n")

    for i, row in enumerate(field):
        if isinstance(row[0], int):
            print_row = map(str, row)
        else:
            print_row = row
        print(str(i + 1) + "  " + " ".join(print_row))
    print("")


field = [
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
]

if __name__ == "__main__":
    print_field_as_table(field)
