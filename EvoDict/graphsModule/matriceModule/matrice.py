from tabulate import tabulate
from EvoDict.graphsModule import Graphe
import numpy as np

class Matrice(Graphe):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)

    def __str__(self):
        """
        Retourne la représentation de la matrice sous forme de tableau à l'aide de la bibliothèque tabulate.
        """
        headers = ["colonne n°"] + list(self.dictionnaire.keys())
        data = []
        for i, (key, value) in enumerate(self.dictionnaire.items()):
            row = ["ligne {}".format(i + 1)] + value
            data.append(row)
        return tabulate(data, headers=headers, tablefmt="grid")
    
    def __setitem__(self, cle, valeur):
        if cle not in self.dictionnaire:
            # Si la clé n'existe pas, cela signifie que nous ajoutons une nouvelle ligne
            new_row = [0] * len(list(self.dictionnaire.values())[0])  # Crée une nouvelle ligne remplie de zéros
            self.dictionnaire[cle] = new_row
        elif isinstance(valeur, list):
            # Si la valeur est une liste, cela signifie que nous mettons à jour une ligne existante
            if len(valeur) != len(list(self.dictionnaire.values())[0]):
                raise ValueError("La longueur de la valeur ne correspond pas au nombre de colonnes de la matrice.")
            self.dictionnaire[cle] = valeur
        else:
            # Si la valeur est un scalaire, cela signifie que nous mettons à jour une seule cellule de la matrice
            if len(self.dictionnaire[cle]) == 0:
                # Si la ligne est vide, remplissez-la de zéros avant d'ajouter la valeur
                self.dictionnaire[cle] = [0] * len(list(self.dictionnaire.values())[0])
            self.dictionnaire[cle].append(valeur)  # Ajoutez la valeur à la ligne existante
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

# Méthode de transposition de la matrice
    def transposition(self):
        """
        Transpose la matrice en échangeant lignes et colonnes.
        """
        transposed_dict = {key: [] for key in range(len(list(self.dictionnaire.values())[0]))}
        for key, values in self.dictionnaire.items():
            for i, value in enumerate(values):
                transposed_dict[i].append(value)
        self.dictionnaire = transposed_dict

    # Méthode de calcul du déterminant de la matrice (uniquement pour les matrices carrées)
    def determinant(self):
        """
        Calcule le déterminant de la matrice (uniquement pour les matrices carrées).

        Returns:
            float: Le déterminant de la matrice.
        """
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("Le déterminant n'est défini que pour les matrices carrées.")
        return np.linalg.det(list(self.dictionnaire.values()))

    # Méthode de calcul de l'inverse de la matrice (uniquement pour les matrices carrées inversibles)
    def inverse(self):
        """
        Calcule l'inverse de la matrice (uniquement pour les matrices carrées inversibles).

        Returns:
            Matrice: La matrice inverse.
        """
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("L'inverse n'est défini que pour les matrices carrées.")
        inverse_array = np.linalg.inv(list(self.dictionnaire.values()))
        inverse_dict = {i: inverse_array[i].tolist() for i in range(len(inverse_array))}
        return Matrice(inverse_dict)

    # Méthode de calcul de la trace de la matrice (uniquement pour les matrices carrées)
    def trace(self):
        """
        Calcule la trace de la matrice (uniquement pour les matrices carrées).

        Returns:
            float: La trace de la matrice.
        """
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("La trace n'est définie que pour les matrices carrées.")
        return np.trace(list(self.dictionnaire.values()))

    # Méthode de calcul des valeurs propres et des vecteurs propres (uniquement pour les matrices carrées)
    def valeurs_vecteurs_propres(self):
        """
        Calcule les valeurs propres et les vecteurs propres de la matrice (uniquement pour les matrices carrées).

        Returns:
            tuple: Un tuple contenant les valeurs propres et les vecteurs propres.
        """
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("Les valeurs propres et les vecteurs propres ne sont définis que pour les matrices carrées.")
        eigenvalues, eigenvectors = np.linalg.eig(list(self.dictionnaire.values()))
        return eigenvalues, eigenvectors        
    
    def __call__(self):
        """
        Affiche toutes les informations disponibles sur la matrice, y compris ses propriétés mathématiques et son type.
        """
        print("Informations sur la matrice :")
        print("Contenu de la matrice :")
        print(self.__str__())
        print("Propriétés mathématiques :")
        print("Nombre de lignes :", len(self.dictionnaire))
        print("Nombre de colonnes :", len(list(self.dictionnaire.values())[0]))
        print("Type de la matrice :", type(self).__name__)
        print("\nInformations mathématiques:")
        if len(self.dictionnaire) == len(list(self.dictionnaire.values())[0]):
            print("Transposée:")
            self.transposition()
            print(str(self))
            print("Déterminant:", self.determinant())
            print("Inverse:")
            try :
                inverse_matrix = self.inverse()
                print(str(inverse_matrix))
            except :
                print("Matrice non inversible")    
            print("Trace:", self.trace())
            eigenvalues, eigenvectors = self.valeurs_vecteurs_propres()
            print("Valeurs propres:", eigenvalues)
            print("Vecteurs propres:")
            for i in range(len(eigenvectors)):
                print("Vecteur propre", i+1, ":", eigenvectors[i])
        else:
            print("La transposée, le déterminant, l'inverse, la trace, les valeurs propres et les vecteurs propres ne sont définis que pour les matrices carrées.")