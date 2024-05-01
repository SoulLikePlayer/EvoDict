from EvoDict import *

# Création de la matrice A
matrice_a = Matrice({
    'row1': [2, 1, -1],
    'row2': [-3, -1, 2],
    'row3': [-2, 1, 2]
})

# Vecteur b
vecteur_b = [8, -11, -3]

# Résolution du système d'équations linéaires Ax = b
solution = Resolution(matrice_a).resoudre_systeme_lineaire(vecteur_b)

# Affichage de la solution
print("La solution du système d'équations linéaires est :", solution)
