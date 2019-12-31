import geom


def graph_from_edges(edges, both_ways=True):
    """Generiert einen Graphen (dict) aus den Kanten"""
    graph = {}
    for edge in edges:
        from_pt, to_pt = edge
        add_graph_edge(graph, from_pt, to_pt)
        if both_ways:  # verbinde in beide Richtungen
            add_graph_edge(graph, to_pt, from_pt)
    return graph


def add_graph_edge(graph, from_val, to_val):
    """Fügt zu einem Graphen eine weitere Kante hinzu"""
    if from_val in graph and to_val in graph[from_val]:
        return
    if from_val in graph and type(graph[from_val]) is list:
        graph[from_val].append(to_val)
    elif from_val in graph and type(graph[from_val]) is not list:
        graph[from_val] = [graph[from_val], to_val]
    else:
        graph[from_val] = [to_val]


def connect_streets(graph):  # verbindet nur über dreierdistanz
    for node in graph.keys():
        for neighbour in graph.keys():
            for third in graph.keys():
                if (third != node != neighbour) and (node not in graph[third]) and (neighbour in graph[node]) and (third in graph[neighbour]) and geom.on_line(node, neighbour, third):
                    add_graph_edge(graph, third, node)
                    add_graph_edge(graph, node, third)


def dijkstra_least_turns(graph, start, dest):
    """Ermittle mit dem Dijkstra-Algorithmus die Strecke mit den wenigsten Abbiegungen.
    Bei gleichwertigen Wegen wird der kürzere bevorzugt"""
    from math import inf
    unvisited = {key for key in graph.keys()}
    turns = {key: inf for key in graph.keys()}
    distance = {key: inf for key in graph.keys()}
    previous = {}

    current = start
    turns[current] = 0
    distance[current] = 0
    while len(unvisited) > 0:
        # aktuellen Knoten besuchen
        ts = turns[current]
        ds = distance[current]
        for neighbour in graph[current]:
            new_turns = ts + (not geom.on_line(previous[current], current, neighbour)) if current != start else ts
            new_dist = ds + geom.point_distance(current, neighbour)
            if neighbour in unvisited and (new_turns < turns[neighbour]) or (new_turns == turns[neighbour] and new_dist < distance[neighbour]):
                turns[neighbour] = new_turns
                distance[neighbour] = new_dist
                previous[neighbour] = current
        # Abbruchbedingungen
        if current == dest:
            break
        else:
            unvisited.remove(current)
            current = min(unvisited, key=turns.get)

    path = [dest]
    current = dest
    while current != start:
        prev = previous[current]
        path.append(prev)
        current = prev

    return turns[dest], path[::-1]


def dijkstra_least_distance(graph, start, dest):
    """Ermittle mit dem Dijkstra-Algorithmus die Strecke mit den wenigsten Kanten"""
    from math import inf
    unvisited = {key for key in graph.keys()}
    distance = {key: inf for key in graph.keys()}
    previous = {}

    current = start
    distance[current] = 0
    while len(unvisited) > 0:
        # aktuellen Knoten besuchen
        dist = distance[current]
        for neighbour in graph[current]:
            new_dist = (dist + geom.point_distance(current, neighbour))
            if neighbour in unvisited and new_dist < distance[neighbour]:
                distance[neighbour] = new_dist
                previous[neighbour] = current
        # Abbruchbedingungen
        if current == dest:
            break
        else:
            unvisited.remove(current)
            current = min(unvisited, key=distance.get)

    path = [dest]
    current = dest
    while current != start:
        prev = previous[current]
        path.append(prev)
        current = prev

    return distance[dest], path[::-1]
