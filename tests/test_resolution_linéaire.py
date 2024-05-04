from EvoDict import *

# Création d'une matrice
matrice = Matrice({
    'ligne1': [2, 1, -1],
    'ligne2': [-3, -1, 2],
    'ligne3': [-2, 1, 2]
})

# Vecteur b
vecteur_b = [8, -11, -3]

# Création d'une instance de la classe Resolution
resol = Resolution(matrice)

# Résolution du système d'équations linéaires
solution = resol.resoudre_systeme_lineaire(vecteur_b)

# Affichage de la solution
print("La solution du système d'équations linéaires Ax = b est :", solution)
