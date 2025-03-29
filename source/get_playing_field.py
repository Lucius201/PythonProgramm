"""Das Modul erstellt das 5x5 Spielfeld."""

import random


def get_playing_field() -> list:
    """Generiert ein 5x5 Spielfeld."""
    playing_field = []
    result = []

    for i in range(5):
        playing_field.append(0)
    for i in range(20):
        playing_field.append(1)

    random.shuffle(playing_field)
    for i in range(5):
        result.append(playing_field[i * 5 : i * 5 + 5])
    return result


if __name__ == "__main__":
    print(get_playing_field())
