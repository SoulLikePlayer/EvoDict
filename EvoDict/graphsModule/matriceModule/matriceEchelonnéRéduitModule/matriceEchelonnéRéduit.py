from EvoDict.graphsModule.matriceModule import Matrice

class MatriceEchelonneeReduite(Matrice):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
        Initialise une matrice échelonnée réduite.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs. Par défaut, "value".
        """
        # Appel du constructeur de la classe parente
        super().__init__(dictionnaire, cle, valeur)
        
        # Vérification et échelonnement réduction de la matrice
        if dictionnaire is not None:
            self.echelonner_reduire_matrice()

    def echelonner_reduire_matrice(self):
        """
        Réduit la matrice à sa forme échelonnée réduite.
        """
        # Obtenez les dimensions de la matrice
        nb_lignes = len(self.dictionnaire)
        if nb_lignes == 0:
            return
        
        nb_colonnes = len(next(iter(self.dictionnaire.values())))
        
        # Définir les indices pour le pivot
        i_pivot = 0
        j_pivot = 0
        
        # Algorithme de Gauss-Jordan pour échelonner réduire la matrice
        while i_pivot < nb_lignes and j_pivot < nb_colonnes:
            # Trouver le pivot dans la colonne actuelle
            max_val = 0
            i_max = i_pivot
            for i in range(i_pivot, nb_lignes):
                if abs(self.dictionnaire[list(self.dictionnaire.keys())[i]][j_pivot]) > max_val:
                    max_val = abs(self.dictionnaire[list(self.dictionnaire.keys())[i]][j_pivot])
                    i_max = i
            
            # Permuter les lignes si nécessaire pour mettre le pivot sur la diagonale
            if i_max != i_pivot:
                self.dictionnaire[list(self.dictionnaire.keys())[i_pivot]], self.dictionnaire[list(self.dictionnaire.keys())[i_max]] = self.dictionnaire[list(self.dictionnaire.keys())[i_max]], self.dictionnaire[list(self.dictionnaire.keys())[i_pivot]]
            
            # Échelonner la ligne actuelle
            pivot = self.dictionnaire[list(self.dictionnaire.keys())[i_pivot]][j_pivot]
            if pivot != 0:
                for i in range(i_pivot + 1, nb_lignes):
                    coef = self.dictionnaire[list(self.dictionnaire.keys())[i]][j_pivot] / pivot
                    for j in range(j_pivot, nb_colonnes):
                        self.dictionnaire[list(self.dictionnaire.keys())[i]][j] -= coef * self.dictionnaire[list(self.dictionnaire.keys())[i_pivot]][j]
            
            # Passer à la ligne et à la colonne suivante
            i_pivot += 1
            j_pivot += 1
