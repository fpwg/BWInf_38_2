import graph as g
from math import inf, floor
import random as r


def inverse_difficulty(graph, node, energy, batteries):
    solved, failed = g.count_paths_dfs(graph, node, energy, batteries)
    return solved - failed
    # return inf if not failed else (solved/failed)


def difficulty(graph, node, energy, batteries):
    solved, failed = g.count_paths_dfs(graph, node, energy, batteries)
    return failed - solved
    # return inf if not solved else (failed/solved)


def random_start_vec(size, n_batteries, seed=None):
    """Erzeugt zufälligen Startvektor für das Generieren der Level"""
    if seed:
        r.seed(seed)
    r_range = (0, size - 1)
    vec = []
    for i in range(0, 3 * (n_batteries + 1)):
        vec.append(float(r.randint(*r_range)))
    graph = g.make_graph(size)
    return graph, vec


def to_params(vec, size):
    """Konvertiert den Vektor in die Levelparameter, die Werte werden dabei abgerundet"""
    n_batteries = int(len(vec) / 3) - 1

    energy = cf(vec[0], 0, size)
    node = tuple(map(lambda x: cf(x, 0, size), vec[1:3]))

    batteries = {}
    for i in range(0, n_batteries):
        pos = tuple(map(lambda x: cf(x, 0, size), vec[i*3+3:i*3+5]))
        charge = cf(vec[i*3+5], 0, size)
        batteries[pos] = charge

    return node, energy, batteries


def cf(val, max, min):
    if val > max:
        return max
    elif val < min:
        return min
    else:
        return floor(val)


def gradient_descent(graph, vec, size, iterations, gamma):
    next = vec
    for i in range(iterations):
        current = next
        dvec = vec_mul(gradient(graph, vec, size), -gamma)
        next = vec_add(current, dvec)
        print("nudged by", *dvec)
    return vec


def gradient(graph, vec, size):
    DX = 1
    grad = []
    f_0 = inverse_difficulty(graph, *to_params(vec, size))
    print("Current f", f_0, "at", *vec)
    for n in range(0, len(vec)-1):
        vec_ = vec.copy()
        vec_[n] += DX
        f_1 = inverse_difficulty(graph, *to_params(vec_, size))
        DF = f_1 - f_0
        grad.append(DF/DX)
    return grad


def vec_add(vec_a, vec_b):
    return map(lambda a, b: a + b, zip(vec_a, vec_b))


def vec_mul(vec, k):
    return [k * x_n for x_n in vec]