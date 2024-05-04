from EvoDict import *

# Création d'un graphe pondéré
graph_pondere = GraphePondere()

# Ajout des arêtes avec des poids en utilisant la syntaxe dictionnaire[cle] = [sommet, poids]
graph_pondere['A'] = ['B', 5]
graph_pondere['A'] = ['C', 3]
graph_pondere['B'] = ['C', 2]
graph_pondere['B'] = ['D', 4]
graph_pondere['C'] = ['D', 6]

# Affichage du graphe pondéré
print("Graphe pondéré :")
print(graph_pondere)
print(graph_pondere.historique)