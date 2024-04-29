from EvoDict import *

# Création d'une matrice qui n'est pas échelonnée réduite
matrice_non_echelonnee_reduite = MatriceEchelonneeReduite({
    "ligne1": [1, 2, 3],
    "ligne2": [1, 3, 4],
    "ligne3": [0, 0, 1]
})

# Affichage de la matrice avant réduction
print("Matrice non échelonnée réduite :")
print(matrice_non_echelonnee_reduite)

# Création d'une matrice qui est déjà échelonnée réduite
matrice_echelonnee_reduite = MatriceEchelonneeReduite({
    "ligne1": [1, 0, 0],
    "ligne2": [0, 1, 0],
    "ligne3": [0, 0, 1]
})

# Affichage de la matrice déjà échelonnée réduite
print("\nMatrice déjà échelonnée réduite :")
print(matrice_echelonnee_reduite)