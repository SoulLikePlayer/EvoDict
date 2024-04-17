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

    def fusions(self, other):
        """
        Fusionne les informations d'un autre EvoDict dans le dictionnaire actuel.

        Args:
            other (EvoDict): L'autre EvoDict dont les informations doivent être fusionnées.
        """
        if self.nom_cle != other.nom_cle:
            raise FusionError("Les noms de clés ne correspondent pas : '{}' et '{}'.".format(self.nom_cle, other.nom_cle))
        if self.nom_valeur != other.nom_valeur:
            raise FusionError("Les noms de valeurs ne correspondent pas : '{}' et '{}'.".format(self.nom_valeur, other.nom_valeur))

        for key, value in other.dictionnaire.items():
            if (key in self.dictionnaire):
                # Si la clé existe déjà dans le dictionnaire actuel, nous devons fusionner les valeurs.
                if (value != self.dictionnaire[key]) :
                    current_value = self.dictionnaire[key]
                    if (isinstance(current_value, list)):
                    # Si la valeur actuelle est une liste, nous étendons cette liste avec les nouvelles valeurs.
                        current_value.append(value)
                        self.dictionnaire[key] = sorted(current_value)
                    else:
                        # Si la valeur actuelle n'est pas une liste, nous transformons les deux valeurs en liste et les fusionnons.
                        self.dictionnaire[key] = [current_value, value]
            else:
                # Si la clé n'existe pas dans le dictionnaire actuel, nous l'ajoutons simplement avec sa valeur.
                self.dictionnaire[key] = value

    def supprimeParIndex(self, index):
        """
        Supprime une clé en fonction de son index dans le dictionnaire.

        Args:
            index (int): L'index de la clé à supprimer.
        """
        keys = list(self.dictionnaire.keys())
        if 0 <= index < len(keys):
            key_to_delete = keys[index]
            del self.dictionnaire[key_to_delete]
        else:
            print("L'indice spécifié est hors de la plage du dictionnaire.")

#Exception de EvoDict

class FusionError(Exception):
    """Exception levée lorsqu'il y a une incompatibilité lors de la fusion de deux EvoDict."""
    def __init__(self, message="Erreur de fusion : Les clés ou les valeurs ne correspondent pas."):
        self.message = message
        super().__init__(self.message)        