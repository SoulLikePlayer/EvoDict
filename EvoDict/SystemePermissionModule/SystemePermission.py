from EvoDict import Evodict
from tabulate import tabulate

class SystemePermission(Evodict):
    """
    Classe représentant un système de permissions basé sur un dictionnaire.
  
    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données du système de permissions.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
        liste_permissions (list): Une liste des différentes permissions autorisées.
    """

    def __init__(self, dictionnaire, liste_permissions):
        super().__init__(dictionnaire, "Personne ou Groupe", "Permissions")
        self.liste_permissions = liste_permissions

    def __setitem__(self, personne_ou_groupe, permissions):
        """
        Associe à une personne ou groupe les permissions spécifiées, si les permissions sont valides.

        Args:
            personne_ou_groupe (str): La personne ou le groupe à associer aux permissions.
            permissions (set): L'ensemble des permissions à associer.
        """
        # Vérifier si toutes les permissions sont valides
        if all(permission in self.liste_permissions for permission in permissions):
            super().__setitem__(personne_ou_groupe, permissions)
        else:
            raise ValueError("Une ou plusieurs permissions spécifiées ne sont pas valides.")

    def __str__(self):
        """
        Renvoie une représentation du système de permissions sous forme de tableau.
        """
        # Création de l'en-tête du tableau avec les permissions
        headers = ["Personne ou Groupe"] + self.liste_permissions

        # Création des données du tableau avec un "X" pour chaque permission associée à une personne ou groupe
        data = []
        for personne_ou_groupe, permissions in self.items():
            row = [personne_ou_groupe] + ["X" if permission in permissions else "" for permission in self.liste_permissions]
            data.append(row)

        return tabulate(data, headers=headers, tablefmt="fancy_grid")