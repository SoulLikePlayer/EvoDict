from EvoDict import *

# Création d'une matrice carrée 4x4 non triangulaire
matrice = {
    'ligne 1': [1, 2, 3, 4],
    'ligne 2': [5, 6, 7, 8],
    'ligne 3': [9, 10, 11, 12],
    'ligne 4': [13, 14, 15, 16]
}

matrice_non_triangulaire = Matrice(matrice)

# Affichage de la matrice initiale
print("Matrice non triangulaire :")
print(matrice_non_triangulaire)
print()

# Transformation de la matrice en matrice triangulaire
matrice_triangulaire = MatriceTriangulaire(matrice, type="sup")

# Affichage de la matrice triangulaire
print("Matrice triangulaire :")
print(matrice_triangulaire)
