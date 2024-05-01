from EvoDict.graphsModule.matriceModule.matrice import Matrice

class MatriceTriangulaire(Matrice):
    """
    Représentation d'une matrice triangulaire.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données de la matrice.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
        type (str): Détermine si le triangle est inférieur ou supérieur.
                    - "inf" pour inférieur.
                    - "sup" pour supérieur.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value", type="inf"):
        """
        Initialise un nouvel objet de la classe MatriceTriangulaire.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données de la matrice. Par défaut, None.
            cle (str, optional): Le nom de la clé. Par défaut, "key".
            valeur (str, optional): Le nom de la valeur. Par défaut, "value".
            type (str, optional): Détermine si le triangle est inférieur ou supérieur. Par défaut, "inf".
        """
        # Appeler le constructeur de la classe parente avec les noms de clé et de valeur appropriés
        super().__init__(dictionnaire, cle, valeur)
        # Appeler la méthode rendre_triangulaire seulement si la matrice est initialisée
        if self.dictionnaire is not None:
            if type == "inf":
                self.rendre_triangulaire(True)
            elif type == "sup":
                self.rendre_triangulaire(False)    

    def rendre_triangulaire(self, inferieure):
        """
        Transforme la matrice en une matrice triangulaire inférieure ou supérieure en fonction de l'argument passé.

        Args:
            inferieure (bool): Indique si la matrice doit être rendue triangulaire inférieure (par défaut) ou supérieure.
        """
        for key, values in self.dictionnaire.items():
            if inferieure:
                # Remplacer les éléments au-dessus de la diagonale principale par des zéros
                for i in range(len(values)):
                    if i > list(self.dictionnaire.keys()).index(key):
                        self.dictionnaire[key][i] = 0
            else:
                # Remplacer les éléments en dessous de la diagonale principale par des zéros
                for i in range(len(values)):
                    if i < list(self.dictionnaire.keys()).index(key):
                        self.dictionnaire[key][i] = 0
