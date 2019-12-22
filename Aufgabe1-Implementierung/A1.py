import IO
import graph as g


size, start, energy, batteries = IO.load_file("stromrallye0.txt")
graph = g.make_graph(size)

solution = g.solve_backtracking(graph, start, energy, batteries)

if solution:
    print("Lösung gefunden", *solution)
else:
    print("Keine Lösung gefunden")