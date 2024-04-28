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
# Méthode d'addition de matrices
    def addition(self, other):
        """
        Additionne deux matrices.

        Args:
            other (Matrice): La matrice à ajouter.

        Returns:
            Matrice: La matrice résultante de l'addition.
        """
        if len(self.dictionnaire) != len(other.dictionnaire) or len(list(self.dictionnaire.values())[0]) != len(list(other.dictionnaire.values())[0]):
            raise ValueError("Les matrices doivent avoir la même taille pour effectuer une addition.")
        result = Matrice()
        for key in self.dictionnaire.keys():
            result.dictionnaire[key] = [self.dictionnaire[key][i] + other.dictionnaire[key][i] for i in range(len(self.dictionnaire[key]))]
        return result

    # Méthode de soustraction de matrices
    def soustraction(self, other):
        """
        Soustrait une matrice d'une autre.

        Args:
            other (Matrice): La matrice à soustraire.

        Returns:
            Matrice: La matrice résultante de la soustraction.
        """
        if len(self.dictionnaire) != len(other.dictionnaire) or len(list(self.dictionnaire.values())[0]) != len(list(other.dictionnaire.values())[0]):
            raise ValueError("Les matrices doivent avoir la même taille pour effectuer une soustraction.")
        result = Matrice()
        for key in self.dictionnaire.keys():
            result.dictionnaire[key] = [self.dictionnaire[key][i] - other.dictionnaire[key][i] for i in range(len(self.dictionnaire[key]))]
        return result

    # Méthode de multiplication de matrices
    def multiplication(self, other):
        """
        Multiplie deux matrices.

        Args:
            other (Matrice): La matrice à multiplier.

        Returns:
            Matrice: La matrice résultante de la multiplication.
        """
        if len(list(self.dictionnaire.values())[0]) != len(other.dictionnaire):
            raise ValueError("Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice pour effectuer une multiplication.")
        result = Matrice()
        for key in self.dictionnaire.keys():
            result.dictionnaire[key] = [sum(self.dictionnaire[key][j] * other.dictionnaire[list(other.dictionnaire.keys())[j]][i] for j in range(len(self.dictionnaire[key]))) for i in range(len(list(other.dictionnaire.values())[0]))]
        return result
    
    # Méthode de puissance de matrice
    def puissance(self, n):
        """
        Élève une matrice à la puissance n.

        Args:
            n (int): L'exposant auquel élever la matrice.

        Returns:
            Matrice: La matrice résultante de l'élévation à la puissance n.
        """
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("La matrice doit être carrée pour effectuer une élévation à la puissance.")
        if n == 0:
            # Si n est 0, la matrice résultante est la matrice identité
            result = Matrice()
            for key in self.dictionnaire.keys():
                result.dictionnaire[key] = [1 if i == j else 0 for i in range(len(self.dictionnaire[key])) for j in range(len(self.dictionnaire[key]))]
            return result
        elif n > 0:
            # Si n est positif, élever la matrice à la puissance n
            result = self
            for _ in range(1, n):
                result = result.multiplication(self)
            return result
        else:
            raise ValueError("La puissance doit être un entier positif ou nul.")