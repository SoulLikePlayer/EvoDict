import networkx as nx
import matplotlib.pyplot as plt
from EvoDict.graphsModule import Graphe

class Arbre(Graphe):
    """
    Classe représentant un arbre, un type spécifique de graphe.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données de l'arbre.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value", limMaxPaire=None):
        """
        Initialise un nouvel objet de la classe Arbre.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données de l'arbre. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés dans le dictionnaire. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs dans le dictionnaire. Par défaut, "value".
        """
        # Appel du constructeur de la classe parente avec les noms de clé et de valeur appropriés
        super().__init__(dictionnaire, cle, valeur, limMaxPaire)

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée dans le dictionnaire de l'arbre.

        Si la valeur est déjà une clé existante dans le dictionnaire, lève une ValueError.

        Args:
            cle (str): La clé à définir.
            valeur (list): La liste des valeurs associées à la clé.

        Raises:
            ValueError: Si la valeur est déjà une clé existante dans le dictionnaire.
        """
        # Vérifie si la valeur est déjà une clé existante dans le dictionnaire
        if valeur in list(self.dictionnaire.keys()):
            raise ValueError("La valeur '{}' est déjà une clé existante dans le dictionnaire de l'arbre.".format(valeur))
        # Appel de la méthode de la classe parente pour définir la valeur associée à la clé spécifiée
        return super().__setitem__(cle, valeur)

    def __str__(self):
        """
        Affiche le dictionnaire de l'arbre sous forme de graphe dirigé à l'aide du parcours en profondeur.

        Returns:
            str: Une chaîne vide, car l'affichage du graphe est géré par matplotlib.
        """
        # Appel de la méthode de la classe parente pour afficher le dictionnaire sous forme de graphe dirigé
        return super().__str__()
