"""Funktion, die das Gewinnen vom Spiel bestimmt"""

# shown_field_1 = [
#     ["x", "x", "x", "x", "x"],
#     ["x", "x", "x", "x", "x"],
#     ["x", "x", "x", "x", "x"],
#     ["x", "x", "x", "x", "x"],
#     ["x", "x", "x", "x", "x"],
# ]
# shown_field_2 = [
#     ["x", "x", "x", "x", "x"],
#     ["b", "b", "b", "b", "b"],
#     ["b", "b", "b", "b", "b"],
#     ["b", "b", "b", "b", "b"],
#     ["b", "b", "b", "b", "b"],
# ]


def win_condition(shown_field) -> bool:
    """Wenn nur noch 5 unaufdeckte Felder -> Spiel gewonnen"""
    x_count = 0
    for row in shown_field:
        for cell in row:
            if cell == "x":
                x_count = x_count + 1

    if x_count <= 5:
        return True
    else:
        return False


# if __name__ == "__main__":
#     print(win_condition(shown_field_2))
