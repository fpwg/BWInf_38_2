import IO
import graph as g
import generate as gen

print(gen.gradient_descent(*gen.random_start_vec(3, 1), 3, 100, 0.1))

# size, start, energy, batteries = IO.load_file("stromrallye0.txt")
# graph = g.make_graph(size)
#
# solution = g.solve_backtracking(graph, start, energy, batteries)
#
# if solution:
#     print("Lösung gefunden", *solution)
# else:
#     print("Keine Lösung gefunden")