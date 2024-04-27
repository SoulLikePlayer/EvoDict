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
        if valeur in self.dictionnaire.keys():
            raise ValueError("Un nœud ne peut avoir qu'un seul parent dans un arbre.")
        super().__setitem__(cle, valeur)

    def __str__(self):
        return super().__str__()