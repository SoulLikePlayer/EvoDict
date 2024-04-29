from EvoDict import *

class MatriceBinaire(Matrice):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
        Initialise une matrice binaire à partir d'une matrice classique ou échelonnée réduite.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs. Par défaut, "value".
        """
        # Appel du constructeur de la classe parente
        super().__init__(dictionnaire, cle, valeur)
        
        # Transformation de la matrice en matrice binaire
        if dictionnaire is not None:
            self.transformer_matrice_binaire()

    def transformer_matrice_binaire(self):
        """
        Transforme la matrice en matrice binaire.
        """
        for cle, valeur in self.dictionnaire.items():
            if isinstance(valeur, list):
                self.dictionnaire[cle] = [1 if x != 0 else 0 for x in valeur]
            else:
                self.dictionnaire[cle] = 1 if valeur != 0 else 0
