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


def parse_street(string):
    """Liest eine Zeile mit einer Straße und die Koordinaten zurück"""
    start, rest = parse_tuple(string)
    end, rest = parse_tuple(rest)
    assert len(rest) == 0

    return start, end


def load_file(filename=""):
    """Lädt eine Kartendatei und gibt Straßen, Start- und Endpunkt zurück.
    Wenn kein Dateiname gegben wurde, wird er über stdin abgefragt"""
    # Dateinamen einlesen
    while not os.path.exists(filename):
        filename = input("Dateinamen der Straßenkarte eingeben:")

    print(f"Öffne {filename}")
    # Daten einlesen
    with open(filename) as file:
        n_streets = int(file.readline().strip())
        home, _ = parse_tuple(file.readline())
        dest, _ = parse_tuple(file.readline())
        streets = []
        for i in range(0, n_streets):
            streets.append(parse_street(file.readline()))

    print("Karte fertig eingelesen")
    return home, dest, streets


def display_graph(graph, start, dest, filename=""):
    x_size = y_size = 0
    for x, y in graph.keys():
        x_size = max(DISPLAY_SCALE + x * DISPLAY_SCALE, x_size)
        y_size = max(DISPLAY_SCALE + y * DISPLAY_SCALE, y_size)

    win = GraphWin("Abbiegen" + " - " + filename, x_size + DISPLAY_SCALE, y_size + DISPLAY_SCALE, autoflush=False)
    win.setBackground(color_rgb(138, 250, 107))
    print("Anzeigefenster mit Dimensionen", x_size, "x", y_size, "wird geöffnet.")

    lines = set()
    points = set()
    for from_x, from_y in graph.keys():
        points.add(Point(from_x * DISPLAY_SCALE + DISPLAY_SCALE, y_size - from_y * DISPLAY_SCALE))
        for to_x, to_y in graph[(from_x, from_y)]:
            lines.add(Line(Point(from_x * DISPLAY_SCALE + DISPLAY_SCALE, y_size - from_y * DISPLAY_SCALE), Point(to_x * DISPLAY_SCALE + DISPLAY_SCALE, y_size - to_y * DISPLAY_SCALE)))
    for line in lines:
        line.draw(win)
    for point in points:
        pt = Circle(point, DISPLAY_SCALE/10)
        pt.setFill("blue")
        pt.draw(win)

    pt_start = Circle(Point(start[0] * DISPLAY_SCALE + DISPLAY_SCALE, y_size - start[1] * DISPLAY_SCALE), DISPLAY_SCALE/10)
    pt_dest = Circle(Point(dest[0] * DISPLAY_SCALE + DISPLAY_SCALE, y_size - dest[1] * DISPLAY_SCALE), DISPLAY_SCALE/10)

    pt_start.setFill("red")
    pt_dest.setFill("green")

    pt_start.draw(win)
    pt_dest.draw(win)

    win.flush()
    return win


def display_path(win, path, color="red"):
    pts = [Point(DISPLAY_SCALE * x + DISPLAY_SCALE, win.getHeight() - DISPLAY_SCALE - DISPLAY_SCALE * y) for x, y in path]
    for i in range(1, len(pts)):
        ln = Line(pts[i-1], pts[i])
        ln.setOutline(color)
        ln.setWidth(3)
        ln.draw(win)
    win.flush()
    return win
