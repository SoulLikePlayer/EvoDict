from EvoDict import *

graphe = {"A" : ["B"],
          "B" : ["C"],
          "C" : ["D"],
          "D" : ["A"]}

EvoGraphe = Graphe(graphe)
print(EvoGraphe)
