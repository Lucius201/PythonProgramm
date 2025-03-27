"""Dieses Modul bestimmt die Nummern der einzelnen Felder"""
from source.playing_field import get_playing_field

get_playing_field()

def get_field_numbers() -> list:
    """Diese Funktion bildet das Feld mit Nummern"""
    field = get_playing_field()
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    result = []
    for direction in directions:
        continue
    print(field)
    return result



if __name__ == "__main__":
    get_field_numbers()
