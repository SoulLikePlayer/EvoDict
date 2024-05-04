from EvoDict import *

# Création d'un graphe pondéré
graph_pondere = GraphePondere()

# Ajout des arêtes avec des poids en utilisant la syntaxe dictionnaire[cle] = [sommet, poids]
graph_pondere['A'] = ['B', 1]
graph_pondere['A'] = ['C', 3]
graph_pondere['B'] = ['C', 1]
graph_pondere['B'] = ['D', 4]
graph_pondere['C'] = ['D', 6]


#chemin le plus court
chemin = Dijkstra(graph_pondere, 'A', 'C')

# Affichage du graphe pondéré
print("Graphe pondéré :")
print(graph_pondere)

print("Chemin du graphe ponndéré")
chemin()

