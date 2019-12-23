import os.path
from graphics import Rectangle, Point, GraphWin, Circle, color_rgb, Text, Line

DISPLAY_SCALE = 70


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


def display_level(size, batteries, start, energy):
    win = GraphWin("Stromrallye", size * DISPLAY_SCALE, size * DISPLAY_SCALE, autoflush=False)
    for x in range(0, size):
        for y in range(0, size):
            rect = Rectangle(Point(x*DISPLAY_SCALE, y*DISPLAY_SCALE), Point(x*DISPLAY_SCALE+DISPLAY_SCALE, y*DISPLAY_SCALE+DISPLAY_SCALE))
            rect.setFill("white")
            rect.setOutline("black")
            rect.draw(win)
            if (x, y) == start:
                circle = Circle(Point((x+0.5)*DISPLAY_SCALE, (y+0.5)*DISPLAY_SCALE), DISPLAY_SCALE/3)
                circle.setFill("green")
                circle.setOutline("green")
                circle.draw(win)
                text = Text(Point((x+0.5)*DISPLAY_SCALE, (y+0.5)*DISPLAY_SCALE), str(energy))
                text.setSize(20)
                text.draw(win)
            elif (x, y) in batteries:
                text = Text(Point((x+0.5)*DISPLAY_SCALE, (y+0.5)*DISPLAY_SCALE), str(batteries[(x,y)]))
                text.setSize(20)
                text.draw(win)
    win.flush()
    return win


def display_solution(win, solution):
    for i in range(1, len(solution)):
        point_a = Point((solution[i-1][0] + 0.5) * DISPLAY_SCALE, (solution[i-1][1] + 0.5) * DISPLAY_SCALE)
        point_b = Point((solution[i][0] + 0.5) * DISPLAY_SCALE, (solution[i][1] + 0.5) * DISPLAY_SCALE)
        line = Line(point_a, point_b)
        line.setFill("red")
        line.setArrow("last")
        line.setWidth(3)
        line.draw(win)
    win.flush()
    return win