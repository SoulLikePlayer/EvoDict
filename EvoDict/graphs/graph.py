import networkx as nx
import matplotlib.pyplot as plt
from EvoDict import *

#Classe de graphe
class Graphe(EvoDict):
     def __init__(self, dictionnaire=None, cle="key", valeur="value"):
         super().__init__(dictionnaire, cle, valeur)
         
     def __setitem__(self, cle, valeur):
         super().__setitem__(cle, valeur) 
         value_in_key = False
         for key in self.dictionnaire:
             if (key == valeur):
                 value_in_key = True
         if (value_in_key == False):
             self.dictionnaire[valeur] = []  
     
     def __str__(self):
        """Affiche le dictionnaire sous forme de graphe grâce au parcours en profondeurs."""
        # Créer un graphe dirigé pour représenter l'arbre
        G = nx.DiGraph()

        # Fonction auxiliaire pour parcourir l'arbre en profondeur et ajouter des nœuds et des arêtes au graphe
        def dfs(node, parent=None):
            G.add_node(node)
            if parent is not None:
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