import random
from EvoDict import *

matrice_non_binaire = {}
for i in range(1, 11):
    ligne = [random.randint(0, 9) for _ in range(10)]
    matrice_non_binaire[f"ligne{i}"] = ligne

matrice_normal = Matrice(matrice_non_binaire)
print("Matrice classique :")
print(matrice_normal)

matrice_binaire = MatriceBinaire(matrice_non_binaire)
print("Matrice binaire :")
print(matrice_binaire)
