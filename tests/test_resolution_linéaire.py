from EvoDict import *

# Création de la matrice A
matrice_a = Matrice({
    'row1': [2, 1, -1],
    'row2': [4, -1, 3],
    'row3': [1, -1, 2]
})

# Vecteur b
vecteur_b = [4, 2, -1]

# Résolution du système d'équations linéaires Ax = b
solution = Resolution(matrice_a).resoudre_systeme_lineaire(vecteur_b)

# Affichage de la solution
print("La solution du système d'équations linéaires est :", solution)
