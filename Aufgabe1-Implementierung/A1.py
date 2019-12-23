import IO
import graph as g
import generate as gen
import sys

print("Erzeuge Graphen")
size = 10
graph = g.make_graph(size)
difficulty = 1000
batteries_max = 4
print("Generiere Level")
start, energy, batteries = gen.generate_level(size, graph, difficulty, batteries_max=batteries_max)
if not batteries:
    print("Konnte kein ausreichend schweres Level erzeugen")
    sys.exit(1)
print("Löse Level")
solution = g.solve_backtracking(graph, start, energy, batteries)

print("Level", start, energy, batteries)
print("Schwierigkeitsstufe", gen.difficulty(graph, start, energy, batteries))
print("Lösung", solution)

win = IO.display_level(size, batteries, start, energy)
win = IO.display_solution(win, solution)

input("Enter drücken zum Beenden")

# size, start, energy, batteries = IO.load_file("stromrallye0.txt")
# graph = g.make_graph(size)
#
# solution = g.solve_backtracking(graph, start, energy, batteries)
#
# if solution:
#     print("Lösung gefunden", *solution)
# else:
#     print("Keine Lösung gefunden")