import math


def point_distance(point_a, point_b):
    """Berechnet die Distanz zweier Punkte"""
    return math.sqrt(math.pow(point_a[0] - point_b[0], 2) + math.pow(point_a[1] - point_b[1], 2))


def on_line(a, b, c, tolerance=0):
    """Überprüft, ob A, B und C auf einer Linie liegen"""
    x = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])
    return x == 0


def path_length(path):
    length = 0
    for i in range(1, len(path)):
        length += point_distance(path[i-1], path[i])
    return length
