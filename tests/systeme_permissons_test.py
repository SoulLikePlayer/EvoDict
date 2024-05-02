from EvoDict import *

# Création d'une liste des différentes permissions autorisées
liste_permissions_autorisees = ["lecture", "écriture", "suppression", "exécution"]

# Création d'un système de permissions avec un dictionnaire vide et la liste des permissions autorisées
systeme_permissions = SystemePermission({}, liste_permissions_autorisees)

# Test d'ajout de permissions valides pour un utilisateur
try:
    systeme_permissions["utilisateur1"] = {"lecture", "écriture"}
    print("Permissions ajoutées avec succès pour l'utilisateur1.")
except ValueError as e:
    print("Erreur lors de l'ajout des permissions :", e)

# Test d'ajout de permissions avec une permission non autorisée pour un utilisateur
try:
    systeme_permissions["utilisateur2"] = {"lecture", "exécution"}
    print("Permissions ajoutées avec succès pour l'utilisateur2.")
except ValueError as e:
    print("Erreur lors de l'ajout des permissions :", e)

# Affichage du système de permissions après les modifications
print("Système de permissions mis à jour :\n",systeme_permissions)