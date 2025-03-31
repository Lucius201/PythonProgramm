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
        if type(row[0]) is int:
            print_row = map(str, row)
        else:
            print_row = row
        print(str(i + 1) + "  " + " ".join(print_row))
    print("")


# if __name__ == "__main__":
#     print_field_as_table(field)
