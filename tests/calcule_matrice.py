from EvoDict import *

# Création de deux matrices
matrice1 = Matrice({"ligne1": [1, 2], "ligne2": [4, 5]})
matrice2 = Matrice({"ligne1": [7, 8], "ligne2": [9, 10]})

# Addition de matrices
resultat_addition = matrice1.addition(matrice2)
print("Addition de matrices :")
print(resultat_addition)

# Soustraction de matrices
resultat_soustraction = matrice1.soustraction(matrice2)
print("Soustraction de matrices :")
print(resultat_soustraction)

# Multiplication de matrices
resultat_multiplication = matrice1.multiplication(matrice2)
print("Multiplication de matrices :")
print(resultat_multiplication)
