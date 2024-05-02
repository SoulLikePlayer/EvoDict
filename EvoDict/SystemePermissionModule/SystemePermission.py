from EvoDict import Evodict

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
