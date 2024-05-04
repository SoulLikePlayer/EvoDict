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
        super().__init__(dictionnaire, "key", "value")

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée dans le dictionnaire de l'arbre binaire.

        Si la clé existe déjà, vérifie si le nœud a déjà 2 fils.
        Si la valeur est une liste et qu'elle contient plus de 2 éléments, lève une ValueError.
        Si le nœud a déjà 2 fils et que la valeur est une liste, lève une ValueError.
        Sinon, ajoute la valeur au nœud.

        Args:
            cle (str): La clé à définir.
            valeur (list ou str): La valeur ou la liste de valeurs associée(s) à la clé.

        Raises:
            ValueError: Si le nœud a déjà 2 fils, ou si la valeur est une liste contenant plus de 2 éléments.
        """
        # Vérifie si la clé existe déjà dans le dictionnaire
        if cle in self.dictionnaire.keys():
            # Si la clé existe déjà, vérifie si le nœud a déjà 2 fils
            if isinstance(self.dictionnaire[cle], list) and len(self.dictionnaire[cle]) == 2:
                raise ValueError("Le nœud ne peut avoir plus de 2 fils")
            # Si la valeur est une liste et qu'elle contient plus de 2 éléments, lève une ValueError
            if isinstance(valeur, list) and len(valeur) > 2:
                raise ValueError("Le nœud ne peut contenir plus de 2 fils")
            # Si le nœud a déjà 2 fils et que la valeur est une liste, lève une ValueError
            if isinstance(self.dictionnaire[cle], list) and isinstance(valeur, list) and len(self.dictionnaire[cle]) == 2 :
                raise ValueError("Le nœud ne peut avoir plus de 2 fils")
            # Ajoute la valeur au nœud
            self.dictionnaire[cle].append(valeur)
        else:
            # Si la clé n'existe pas, crée une nouvelle entrée dans le dictionnaire avec la clé spécifiée et la valeur associée
            super().__setitem__(cle, valeur)

        # Vérifie si le nœud a maintenant plus de 2 fils et lève une ValueError le cas échéant
        if isinstance(self.dictionnaire[cle], list) and len(self.dictionnaire[cle]) > 2:
            raise ValueError("Le nœud ne peut contenir plus de 2 fils")
