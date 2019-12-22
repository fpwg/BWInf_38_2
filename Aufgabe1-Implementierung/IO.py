import os.path
from graphics import Line, Point, GraphWin, Circle, color_rgb

DISPLAY_SCALE = 50


def parse_tuple(string):
    """Liest einen 2-Tupel von Ints aus einem String und gibt den Tupel sowie den Rest zurück"""
    string = string.strip()

    assert string[0] == "("
    string = string[1:]

    zahl1 = ""
    while string[0].isdigit():
        zahl1 += string[0]
        string = string[1:]
    zahl1 = int(zahl1)

    assert string[0] == ","
    string = string[1:]

    zahl2 = ""
    while string[0].isdigit():
        zahl2 += string[0]
        string = string[1:]
    zahl2 = int(zahl2)

    assert string[0] == ")"
    string = string[1:]

    return (zahl1, zahl2), string


def parse_battery(string):
    """Liest eine Zeile mit einer Batterie und gibt der Ladung und Koordinaten zurück"""
    pos, rest = parse_tuple(string)
    charge = int(rest.strip())

    return pos, charge


def load_file(filename=""):
    """Lädt eine Leveldatei und gibt Größe, Start, Bordbatterie und Batterien
    zurück. Wenn kein Dateiname gegben wurde, wird er über stdin abgefragt"""
    # Dateinamen einlesen
    while not os.path.exists(filename):
        filename = input("Dateinamen des Levels eingeben:")

    print(f"Öffne {filename}")
    # Daten einlesen
    with open(filename) as file:
        n_batteries = int(file.readline().strip())
        size = int(file.readline().strip())
        energy = int(file.readline().strip())
        start, _ = parse_tuple(file.readline())
        dest, _ = parse_tuple(file.readline())
        batteries = {}
        for i in range(0, n_batteries-1):
            pos, charge = parse_battery(file.readline())
            batteries[pos] = charge

    print("Level fertig eingelesen")
    return size, start, energy, batteries
