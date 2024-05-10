from EvoDict.graphsModule.treeModule import Arbre

class ArbreBinaire(Arbre):
    """
    Classe représentant un arbre binaire, un type spécifique d'arbre.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données de l'arbre binaire.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
    """

    def __init__(self, dictionnaire=None):
        """
        Initialise un nouvel objet de la classe ArbreBinaire.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données de l'arbre binaire. Par défaut, None.
        """
        # Appel du constructeur de la classe parente avec les noms de clé et de valeur appropriés
        super().__init__(2, dictionnaire, "key", "value")

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée dans le dictionnaire de l'arbre binaire.

        Args:
            cle (str): La clé à définir.
            valeur (list ou str): La valeur ou la liste de valeurs associée(s) à la clé.

        Raises:
            ValueError: Si le nœud a déjà 2 fils, ou si la valeur est une liste contenant plus de 2 éléments.
        """
        super().__setitem__(cle, valeur)
