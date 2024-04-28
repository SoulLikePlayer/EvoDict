from tabulate import tabulate
from EvoDict.graphsModule import Graphe

class Matrice(Graphe):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)

    def __str__(self):
        """
        Retourne la représentation de la matrice sous forme de tableau à l'aide de la bibliothèque tabulate.
        """
        headers = ["ligne n°"] + list(self.dictionnaire.keys())
        data = []
        for i, (key, value) in enumerate(self.dictionnaire.items()):
            row = ["ligne {}".format(i + 1)] + value
            data.append(row)
        return tabulate(data, headers=headers, tablefmt="grid")
