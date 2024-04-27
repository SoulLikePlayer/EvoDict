from EvoDict.graphs import Graphe

class Graphe(Graphe):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)