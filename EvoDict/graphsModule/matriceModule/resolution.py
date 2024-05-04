class Resolution:      
    def __init__(self, matrice) :
        self.dictionnaire = matrice.dictionnaire        
    def resoudre_systeme_lineaire(self, vecteur_b):
        """
        Résout un système d'équations linéaires Ax = b, où A est la matrice actuelle
        et b est un vecteur donné.

        Args:
            vecteur_b (list): Le vecteur b dans le système d'équations.

        Returns:
            list: La solution x du système d'équations.
        """
        # Assurez-vous que la matrice est carrée
        if len(self.dictionnaire) != len(list(self.dictionnaire.values())[0]):
            raise ValueError("La matrice doit être carrée pour résoudre un système d'équations linéaires.")

        # Vérifiez que le vecteur b a la même longueur que le nombre de lignes de la matrice
        if len(vecteur_b) != len(self.dictionnaire):
            raise ValueError("La longueur du vecteur b ne correspond pas au nombre de lignes de la matrice.")

        # Créez une copie de la matrice pour ne pas modifier l'originale
        matrice_augmentee = [row[:] + [vecteur_b[i]] for i, row in enumerate(self.dictionnaire.values())]

        # Élimination de Gauss
        n = len(matrice_augmentee)
        for i in range(n):
            # Trouvez le pivot pour cette colonne
            pivot_row = max(range(i, n), key=lambda k: abs(matrice_augmentee[k][i]))
            matrice_augmentee[i], matrice_augmentee[pivot_row] = matrice_augmentee[pivot_row], matrice_augmentee[i]

            # Faites en sorte que le pivot soit égal à 1
            pivot = matrice_augmentee[i][i]
            if pivot != 0:
                matrice_augmentee[i] = [x / pivot for x in matrice_augmentee[i]]

            # Soustrayez cette ligne des lignes ci-dessous pour éliminer les coefficients
            for j in range(i + 1, n):
                factor = matrice_augmentee[j][i]
                matrice_augmentee[j] = [x - factor * y for x, y in zip(matrice_augmentee[j], matrice_augmentee[i])]

        # Rétro-subsitution
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            solution[i] = matrice_augmentee[i][-1] - sum(matrice_augmentee[i][j] * solution[j] for j in range(i + 1, n))

        return solution            