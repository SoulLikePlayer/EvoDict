class EvoDict:
    """
    Classe représentant un dictionnaire évolué.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données.
        nom_cle (str): Le nom utilisé pour désigner les clés.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs.
        not_a_key_counter (int): Compteur utilisé pour générer des clés uniques pour les éléments supprimés.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
        Initialise un nouvel EvoDict.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs. Par défaut, "value".
        """
        if dictionnaire is None:
            self.dictionnaire = dict()
        else:
            self.dictionnaire = dictionnaire
        self.nom_cle = cle
        self.nom_valeur = valeur
        self.not_a_key_counter = 0




#Exception de EvoDict

class FusionError(Exception):
    """Exception levée lorsqu'il y a une incompatibilité lors de la fusion de deux EvoDict."""
    def __init__(self, message="Erreur de fusion : Les clés ou les valeurs ne correspondent pas."):
        self.message = message
        super().__init__(self.message)        