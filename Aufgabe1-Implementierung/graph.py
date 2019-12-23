def make_graph(size):
    """Erzeugt einen Graphen eines quadratischen Spielbrettes"""
    graph = {(i, j): [] for i in range(0, size) for j in range(0, size)}  # Graphen erstellen
    for i, j in graph.keys():  # Verbindungen erstellen
        if i > 0:
            graph[(i, j)].append((i-1, j))
        if i < size - 1:
            graph[(i, j)].append((i+1, j))
        if j > 0:
            graph[(i, j)].append((i, j-1))
        if j < size - 1:
            graph[(i, j)].append((i, j+1))
    return graph


def solve_backtracking(graph, node, energy, batteries, path=[]):
    if sum([val for val in batteries.values() if val >= 0]) == energy == 0:  # branch gelöst
        return path+[node]
    elif sum([val for val in batteries.values() if val >= 0]) > 0 and energy == 0:  # branch fehlgeschlagen
        return []

    for next_node in graph[node]:
        if next_node in batteries and batteries[next_node] > 0:  # tauscht Batterien, wenn die liegende nicht leer ist
            new_batteries = batteries.copy()
            new_batteries[next_node] = energy - 1
            new_energy = batteries[next_node]
            final_path = solve_backtracking(graph, next_node, new_energy, new_batteries, path=(path+[node]))
        else:
            final_path = solve_backtracking(graph, next_node, energy-1, batteries, path=(path+[node]))
        if final_path:
            return final_path
    return []


def count_paths_dfs(graph, node, energy, batteries, path=[]):
    if sum([val for val in batteries.values() if val >= 0]) == energy == 0:  # branch gelöst
        return 1, 0
    elif sum([val for val in batteries.values() if val >= 0]) > 0 and energy == 0:  # branch fehlgeschlagen
        return 0, 1

    solved = 0
    failed = 0
    for next_node in graph[node]:
        if next_node in batteries and batteries[next_node] > 0:  # tauscht Batterien, wenn die liegende nicht leer ist
            new_batteries = batteries.copy()
            new_batteries[next_node] = energy - 1
            new_energy = batteries[next_node]
            s, f = count_paths_dfs(graph, next_node, new_energy, new_batteries, path=(path+[node]))
        else:
            s, f = count_paths_dfs(graph, next_node, energy-1, batteries, path=(path+[node]))
        solved += s
        failed += f

    return solved, failed
