import IO
import graph as g


def main(file):
    start, dest, edges = IO.load_file(file)
    graph = g.graph_from_edges(edges)

    g.connect_streets(graph)

    dist_turns, path_turns = g.dijkstra_least_turns(graph, start, dest)
    dist_actual, path_actual = g.dijkstra_least_distance(graph, start, dest)

    print("Start", start, "Ziel", dest)
    print("Strecke (wenigste Wendungen, rot)", dist_turns, "Pfad", *path_turns)
    print("Strecke (wenigste Strecke, orange)", dist_actual, "Pfad", *path_actual)

    win = IO.display_graph(graph, start, dest, filename=file)
    win = IO.display_path(win, path_turns, color="red")
    win = IO.display_path(win, path_actual, color="orange")


for file in ["abbiegen0.txt", "abbiegen1.txt", "abbiegen2.txt", "abbiegen3.txt", "abbiegen4.txt"]:
    main(file)

input("Enter drücken zum Beenden")
