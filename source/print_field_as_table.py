"""Printet das Spielfeld"""

# field = [
#     [1, 1, 1, 0, 1],
#     [0, 1, 0, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1],
# ]


def print_field_as_table(field):
    """Nimmt Spielffeld als Liste als Input und printet Spielfeld"""
    print("   A B C D E\n")

    for i, row in enumerate(field):
        str_row = map(str, row)
        print(str(i + 1) + "  " + " ".join(str_row))


# if __name__ == "__main__":
#     print_field_as_table(field)
