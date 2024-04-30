import networkx as nx
import matplotlib.pyplot as plt
from EvoDict import Evodict

class Graphe(Evodict):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
    représente un graphe
    
    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données.
        nom_cle (str): Le nom utilisé pour désigner les clés.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs.
       
    """
        super().__init__(dictionnaire, cle, valeur)

    def __setitem__(self, cle, valeur):
        super().__setitem__(cle, valeur)
        for value in valeur :
            if value not in list(self.dictionnaire.keys()):
                self.dictionnaire[value] = []  

    def __str__(self):
        """Affiche le dictionnaire sous forme de graphe grâce au parcours en profondeurs."""
        # Créer un graphe dirigé pour représenter l'arbre
        G = nx.DiGraph()

        # Fonction auxiliaire pour parcourir l'arbre en profondeur et ajouter des nœuds et des arêtes au graphe
        visited = set()  # Ensemble pour suivre les nœuds déjà visités
        def dfs(node, parent=None):
            if node in visited:
                if parent is not None and self.dictionnaire[parent] is not None:
                    G.add_edge(parent, node)  # Si le nœud a déjà été visité, on arrête la récursion
                return
            visited.add(node)
            G.add_node(node)
            if parent is not None and self.dictionnaire[parent] is not None:
                G.add_edge(parent, node)
            children = self.dictionnaire.get(node, [])
            if isinstance(children, list):
                for child in children:
                    dfs(child, node)
            else:
                dfs(children, node)

        # Commencer le parcours en profondeur à partir de la racine de l'arbre
        root = next(iter(self.dictionnaire.keys()), None)
        if root is not None:
            dfs(root)

        # Dessiner le graphe
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()
        return ""
