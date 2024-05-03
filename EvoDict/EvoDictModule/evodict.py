from tabulate import tabulate
from pickle import *
from EvoDict.exceptionsModule import *
import git
import os

class EvoHistory:
    def __init__(self):
        self.repo = self.init_repo()
        self.commit_main = ["Système initial"]

    def init_repo(self):
        # Obtient le chemin absolu du dossier contenant le fichier evodict.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Crée un dossier pour le dépôt Git s'il n'existe pas déjà
        repo_path = os.path.join(current_dir, '.evodict_repo')
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        # Initialise un dépôt Git dans le dossier contenant evodict.py
        return git.Repo.init(current_dir)

    def commit(self, message):
        # Obtient le chemin absolu du fichier evodict.py
        evodict_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evodict.py')
        # Ajoute le fichier evodict.py à la zone de préparation
        self.repo.index.add([evodict_path])
        # Effectue un commit avec le message spécifié
        self.repo.index.commit(message)
        # Met à jour l'historique des commits
        self.commit_main.append(message)

class Evodict:
    """
    Classe représentant un dictionnaire évolué.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
        Initialise un nouvel EvoDict.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs. Par défaut, "value".
        """
        # Initialise le dictionnaire avec un dictionnaire vide ou un dictionnaire fourni en argument
        if dictionnaire is None:
            self.dictionnaire = dict()
        else:
            self.dictionnaire = dictionnaire
        # Attributs pour définir les noms de clés et de valeurs
        self.nom_cle = cle
        self.nom_valeur = valeur
        # Compteur pour générer des clés uniques lors de la suppression de clés existantes
        self.not_a_key_counter = 0
        # Historique du dictionnaire
        self.historique = EvoHistory()

    # Méthodes spéciales pour la manipulation du dictionnaire

    def __setitem__(self, cle, valeur):
        """Définit la valeur associée à la clé spécifiée."""
        # Vérifie si la valeur existe déjà dans le dictionnaire
        if valeur in self.dictionnaire.values():
            for k, v in self.dictionnaire.items():
                if v == valeur and "NotAkey" in k:
                    # Si la valeur existe déjà et est associée à une clé "NotAkey", la supprime
                    valeur = self.dictionnaire.pop(k)
                    self.not_a_key_counter -= 1
                    break
        # Vérifie si la clé existe déjà dans le dictionnaire
        if cle in self.dictionnaire.keys():
            valeur2 = valeur
            valeur1 = self.dictionnaire[cle]
            # Si la clé existe déjà, vérifie si sa valeur est une liste
            if isinstance(valeur1, list):
                # Si oui, ajoute la nouvelle valeur à la liste
                valeur1.append(valeur2)
                self.dictionnaire[cle] = valeur1
            else:
                # Sinon, transforme les deux valeurs en liste et les fusionne
                self.dictionnaire[cle] = [valeur1, valeur2]
        else:
            # Si la clé n'existe pas, ajoute simplement la nouvelle clé-valeur
            self.dictionnaire[cle] = valeur
        # Effectue un commit avec le message correspondant
        self.historique.commit(f"Ajout de la clé '{cle}' avec la valeur '{valeur}'")

    def __delitem__(self, cle):
        """
        Supprime une clé et la remplace par une clé unique de type "NotAkey".
        La valeur associée reste dans le dictionnaire.
        """
        if cle in self.dictionnaire:
            self.not_a_key_counter += 1
            not_a_key = "NotAkey" + str(self.not_a_key_counter)
            # Trouve une clé unique de type "NotAkey"
            while not_a_key in self.dictionnaire:
                self.not_a_key_counter += 1
                not_a_key = "NotAkey" + str(self.not_a_key_counter)
            # Remplace la clé spécifiée par la nouvelle clé "NotAkey"
            self.dictionnaire[not_a_key] = self.dictionnaire.pop(cle)
            # Effectue un commit avec le message correspondant
            self.historique.commit(f"Suppression de la clé '{cle}'")

    def __repr__(self):
        """Renvoie une représentation du dictionnaire."""
        return repr(self.dictionnaire)

    def __str__(self):
        """Renvoie une représentation du dictionnaire sous forme de tableau."""
        headers = [self.nom_cle, self.nom_valeur]
        data = [(cle, valeur) for cle, valeur in self.dictionnaire.items()]
        return tabulate(data, headers=headers, tablefmt="grid")
