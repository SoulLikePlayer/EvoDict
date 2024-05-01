from EvoDict import *

graphe = Graphe({
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
})

chemin = BellmanFord(graphe, 'A', 'E')

chemin()