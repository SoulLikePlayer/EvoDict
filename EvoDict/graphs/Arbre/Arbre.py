import networkx as nx
import matplotlib.pyplot as plt
from EvoDict import *

class Arbre(Graphe):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée.
        Empêche la création de plusieurs fils pour un même parent.
        """
        # Vérifie si le nœud fils a déjà un parent
        if valeur in self.dictionnaire.values():
            raise ValueError("Un nœud ne peut avoir qu'un seul parent dans un arbre.")
        super().__setitem__(cle, valeur)

    def __str__(self):
        """Affiche l'arbre sous forme de graphe en évitant les cycles."""
        G = nx.DiGraph()
        visited = set()

        def dfs(node, parent=None):
            if node in visited:
                return
            visited.add(node)
            G.add_node(node)
            if parent is not None:
                G.add_edge(parent, node)
            children = self.dictionnaire.get(node, [])
            if isinstance(children, list):
                for child in children:
                    dfs(child, node)
            else:
                dfs(children, node)

        root = next(iter(self.dictionnaire.keys()), None)
        if root is not None:
            dfs(root)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()
        return ""
