from tabulate import tabulate
from pickle import *
from EvoDict import *
from EvoDict.exceptionsModule import *
from evohistory import *

class Evodict:
    """
    Classe représentant un dictionnaire évolué.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données.
        nom_cle (str): Le nom utilisé pour désigner les clés.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs.
        not_a_key_counter (int): Compteur utilisé pour générer des clés uniques pour les éléments supprimés.
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
        self.historique = EvoHistory(self)

    # Méthodes spéciales pour la manipulation du dictionnaire

    def __getitem__(self, cle):
        """Renvoie la valeur associée à la clé spécifiée."""
        if isinstance(self.dictionnaire[cle], list):
            # Si la valeur est une liste, affiche chaque élément séparément
            for item in self.dictionnaire[cle]:
                print(item, end=" ")
        else:
            # Sinon, renvoie simplement la valeur
            return self.dictionnaire[cle]

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

    # Méthodes spéciales pour la consultation du dictionnaire

    def __contains__(self, cle):
        """Vérifie si une clé est présente dans le dictionnaire."""
        return cle in self.dictionnaire

    def __iter__(self):
        """Renvoie un itérateur sur les clés du dictionnaire."""
        return iter(self.dictionnaire)

    def __len__(self):
        """Renvoie le nombre de paires clé-valeur dans le dictionnaire."""
        return len(self.dictionnaire)

    def __repr__(self):
        """Renvoie une représentation du dictionnaire."""
        return repr(self.dictionnaire)

    def __str__(self):
        """Renvoie une représentation du dictionnaire sous forme de tableau."""
        headers = [self.nom_cle, self.nom_valeur]
        data = [(cle, valeur) for cle, valeur in self.dictionnaire.items()]
        return tabulate(data, headers=headers, tablefmt="grid")

    # Autres méthodes pour la manipulation du dictionnaire

    def keys(self):
        """Renvoie les clés du dictionnaire."""
        return self.dictionnaire.keys()

    def values(self):
        """Renvoie les valeurs du dictionnaire."""
        return self.dictionnaire.values()

    def items(self):
        """Renvoie les paires (clé, valeur) du dictionnaire."""
        return self.dictionnaire.items()

    def update(self, *args, **kwargs):
        """Met à jour le dictionnaire avec les éléments spécifiés."""
        self.dictionnaire.update(*args, **kwargs)

    def pop(self, cle, *args):
        """Supprime et renvoie la valeur associée à la clé spécifiée."""
        return self.dictionnaire.pop(cle, *args)

    def popitem(self):
        """Supprime et renvoie une paire (clé, valeur) arbitraire du dictionnaire."""
        return self.dictionnaire.popitem()

    def clear(self):
        """Supprime tous les éléments du dictionnaire."""
        self.dictionnaire.clear()

    def copy(self):
        """Renvoie une copie superficielle du dictionnaire."""
        return self.__copy__()

    def deepcopy(self):
        """Renvoie une copie en profondeur du dictionnaire."""
        return self.__deepcopy__()

    def get(self, cle, default=None):
        """Renvoie la valeur associée à la clé spécifiée ou une valeur par défaut si la clé n'existe pas."""
        return self.dictionnaire.get(cle, default)

    def setdefault(self, cle, default=None):
        """Renvoie la valeur associée à la clé spécifiée, en l'ajoutant au besoin avec une valeur par défaut."""
        return self.dictionnaire.setdefault(cle, default)

    def __call__(self):
        """
        Méthode appelée lorsque l'objet est utilisé comme une fonction.
        Permet une interaction utilisateur pour effectuer des opérations sur le dictionnaire.
        """
        print("Bienvenue dans EvoDict ! Que souhaitez-vous faire ?")
        while True:
            print("\nMenu :")
            print("1. Ajouter une nouvelle paire clé-valeur")
            print("2. Supprimer une paire clé-valeur")
            print("3. Afficher le dictionnaire")
            print("4. Quitter")
            choix = input("Votre choix : ")

            if choix == "1":
                cle = input("Entrez la nouvelle clé : ")
                valeur = input("Entrez la nouvelle valeur : ")
                # Convertir la valeur au type approprié si possible
                try:
                    # Essayez de convertir la valeur en entier
                    valeur = int(valeur)
                except ValueError:
                    # Si la conversion en entier échoue, essayez de convertir en float
                    try:
                        valeur = float(valeur)
                    except ValueError:
                        # Si la conversion en float échoue, conservez la valeur en tant que chaîne de caractères
                        pass
                self[cle] = valeur
                print("Nouvelle paire clé-valeur ajoutée avec succès !")

            elif choix == "2":
                cle = input("Entrez la clé à supprimer : ")
                if cle in self:
                    del self[cle]
                    print("Clé supprimée avec succès !")
                else:
                    print("La clé spécifiée n'existe pas dans le dictionnaire.")

            elif choix == "3":
                print("Affichage du dictionnaire :")
                print(self)

            elif choix == "4":
                print("Au revoir !")
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")

    def fusions(self, other):
        """
        Fusionne les informations d'un autre EvoDict dans le dictionnaire actuel.

        Args:
            other (EvoDict): L'autre EvoDict dont les informations doivent être fusionnées.
        """
        if self.nom_cle != other.nom_cle:
            raise FusionError("Les noms de clés ne correspondent pas : '{}' et '{}'.".format(self.nom_cle, other.nom_cle))
        if self.nom_valeur != other.nom_valeur:
            raise FusionError("Les noms de valeurs ne correspondent pas : '{}' et '{}'.".format(self.nom_valeur, other.nom_valeur))

        for key, value in other.dictionnaire.items():
            if key in self.dictionnaire:
                # Si la clé existe déjà dans le dictionnaire actuel, nous devons fusionner les valeurs.
                if value != self.dictionnaire[key]:
                    current_value = self.dictionnaire[key]
                    if isinstance(current_value, list):
                        # Si la valeur actuelle est une liste, nous étendons cette liste avec les nouvelles valeurs.
                        current_value.append(value)
                        self.dictionnaire[key] = sorted(current_value)
                    else:
                        # Si la valeur actuelle n'est pas une liste, nous transformons les deux valeurs en liste et les fusionnons.
                        self.dictionnaire[key] = [current_value, value]
            else:
                # Si la clé n'existe pas dans le dictionnaire actuel, nous l'ajoutons simplement avec sa valeur.
                self.dictionnaire[key] = value

    def supprimeParIndex(self, index):
        """
        Supprime une clé en fonction de son index dans le dictionnaire.

        Args:
            index (int): L'index de la clé à supprimer.
        """
        keys = list(self.dictionnaire.keys())
        if 0 <= index < len(keys):
            key_to_delete = keys[index]
            del self.dictionnaire[key_to_delete]
        else:
            print("L'indice spécifié est hors de la plage du dictionnaire.")

    def rechercheParIndex(self, i):
        """
        Recherche une paire clé-valeur par son index dans le dictionnaire.

        Args:
            i (int): L'index de la paire clé-valeur à rechercher.
        """
        if i in self.dictionnaire:
            key = list(self.dictionnaire.keys())[i]
            value = list(self.dictionnaire.values())[i]
            headers = [self.nom_cle, self.nom_valeur, "index"]
            data = [(key, value, i)]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("L'indice n'est pas dans le dictionnaire")

    # Méthodes d'exportation et d'importation

    def export(self, File):
        """
        Exporte le dictionnaire vers un fichier.

        Args:
            File (str): Le nom du fichier de destination.
        """
        try:
            # Exporte le dictionnaire en utilisant pickle
            with open(File + ".txt", "wb") as f:
                dump(self.dictionnaire, f)
        except:
            if File == "":
                raise ExportError("Le nom du fichier ne doit pas être vide")

    def Import(self, File):
        """
        Importe le dictionnaire à partir d'un fichier.

        Args:
            File (str): Le nom du fichier source.
        """
        try:
            # Importe le dictionnaire à partir du fichier en utilisant pickle
            with open(File + ".txt", "rb") as f:
                self.dictionnaire = load(f)
        except:
            raise ImportationError()

    def put(self, key, values, index):
        """
        Insère une paire clé-valeur à un index spécifique dans le dictionnaire.

        Args:
            key: La clé à insérer.
            values: La valeur associée à la clé.
            index: L'index où insérer la paire clé-valeur.
        """
        if index > len(self.dictionnaire):
            # Si l'index est en dehors de la plage actuelle du dictionnaire, ajoute des clés "NotAkey" jusqu'à l'index spécifié
            for i in range(len(self.dictionnaire), index):
                self.dictionnaire["NotAkey" + str(i)] = None
        # Insère la paire clé-valeur à l'index spécifié
        self.dictionnaire[key] = values
