from EvoDict import *

class ArbreBinaire(Arbre):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)

    def __setitem__(self, cle, valeur):
        # Vérifier si la valeur est déjà dans le dictionnaire
        if valeur in self.dictionnaire:
            raise ValueError("La valeur existe déjà dans l'arbre binaire.")

        # Vérifier si le nombre d'enfants de la nouvelle valeur est supérieur à 2
        enfants = self.dictionnaire.get(cle, [])
        if isinstance(enfants, list) and len(enfants) >= 2:
            raise ValueError("Impossible d'ajouter plus de deux enfants à un nœud dans un arbre binaire.")

        # Appeler la méthode de la classe parente pour ajouter la valeur
        super().__setitem__(cle, valeur)

    def __str__(self):
        return super().__str__()
