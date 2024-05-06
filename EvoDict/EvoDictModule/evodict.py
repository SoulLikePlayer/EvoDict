from tabulate import tabulate
from pickle import *
from EvoDict import *
from EvoDict.EvoDictModule.evohistory import EvoHistory
from EvoDict.exceptionsModule import *


class Evodict:
    """
    Classe représentant un dictionnaire évolué.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données.
        nom_cle (str): Le nom utilisé pour désigner les clés.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs.
        not_a_key_counter (int): Compteur utilisé pour générer des clés uniques pour les éléments supprimés.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value", estPaire=False, estImpaire=False,
                 limMaxPaire=None, limMaxVal=None, estPositive=False, estNegative=False, estMutable=True):
        """
        Initialise un nouvel EvoDict.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs. Par défaut, "value".
        """
        if dictionnaire is None:
            self.dictionnaire = dict()
        else:
            self.dictionnaire = dictionnaire
        self.nom_cle = cle
        self.nom_valeur = valeur
        self.not_a_key_counter = 0

        # Méthodes de manipulation du dictionnaire
        self.historique = EvoHistory(self)

        # association des contraintes de clé valeur
        self.limClé = 0
        # contraite de mutation
        self.estMutable = estMutable
        # contrainte de valeur pair
        self.estPaire = estPaire
        if self.estPaire:
            for value in self.dictionnaire.values():
                if value % 2 != 0 and isinstance(value, int):
                    raise ConditionError("La condition estPaire n'est pas respectée initialement")
        # contrainte de valeur impair
        self.estImpaire = estImpaire
        if self.estImpaire:
            for value in self.dictionnaire.values():
                if value % 2 != 0 and isinstance(value, int):
                    raise ConditionError("La condition estImpaire n'est pas respectée initialement")
        # contrainte de limite de paire clé-valeur
        self.limMaxPaire = limMaxPaire
        if self.limMaxPaire is not None:
            if len(list(self.dictionnaire.keys())) > self.limMaxPaire:
                raise ConditionError(
                    f"La taille maximum est initalement dépassée de {len(list(self.dictionnaire.keys())) - self.limMaxPaire}")
            else :
                self.limClé = len(list(self.dictionnaire.keys()))

    def __getitem__(self, cle):
        """Renvoie la valeur associée à la clé spécifiée."""
        if isinstance(self.dictionnaire[cle], list):
            for i in range(len(self.dictionnaire[cle])):
                print(self.dictionnaire[cle][i], " ", end="")
        else:
            return self.dictionnaire[cle]

    def __setitem__(self, cle, valeur):
        """Définit la valeur associée à la clé spécifiée."""
        if ((self.estPaire and valeur % 2 == 0) or (self.estImpaire and valeur % 2 != 0) or self.estMutable or (self.limMaxPaire != None and (len(list(self.dictionnaire.keys())) + self.limClé <= self.limMaxPaire))):
            if valeur in self.dictionnaire.values():
                for k, v in self.dictionnaire.items():
                    if v == valeur and "NotAkey" in k:
                        valeur = self.dictionnaire.pop(k)
                        self.not_a_key_counter -= 1
                        break
            if cle in self.dictionnaire.keys():
                valeur2 = valeur
                valeur1 = self.dictionnaire[cle]
                if isinstance(valeur1, list):
                    valeur1.append(valeur2)
                    self.dictionnaire[cle] = valeur1
                else:
                    self.dictionnaire[cle] = [valeur1, valeur2]
            else:
                self.dictionnaire[cle] = valeur
            # Ajoute le commit
            message = f"Ajout de la valeur {valeur} à la clé {cle}"
            self.historique.commit(message)
        else:
            raise ConditionError()

    def __delitem__(self, cle):
        """
        Supprime une clé et la remplace par une clé unique de type "NotAkey".
        La valeur associée reste dans le dictionnaire.
        """
        if self.estMutable:
            if cle in self.dictionnaire:
                self.not_a_key_counter += 1
                not_a_key = "NotAkey" + str(self.not_a_key_counter)
                while not_a_key in self.dictionnaire:
                    self.not_a_key_counter += 1
                    not_a_key = "NotAkey" + str(self.not_a_key_counter)
                self.dictionnaire[not_a_key] = self.dictionnaire.pop(cle)
            # Ajoute le commit
            message = f"Suppression de la clé {cle}"
            self.historique.commit(message)
        else:
            raise ConditionError()

    # Méthode de copie
    def __copy__(self):
        """Renvoie une copie superficielle du dictionnaire."""
        return Evodict(self.dictionnaire.copy(), self.nom_cle, self.nom_valeur)

    def __deepcopy__(self, memo):
        """Renvoie une copie en profondeur du dictionnaire."""
        from copy import deepcopy
        return Evodict(deepcopy(self.dictionnaire, memo), self.nom_cle, self.nom_valeur)

    # Méthodes de consultation du dictionnaire

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

    # Autres méthodes de manipulation du dictionnaire

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
        if self.estMutable:
            self.dictionnaire.update(*args, **kwargs)
            # Ajoute le commit
            message = "Mise à jour du dictionnaire"
            self.historique.commit(message)
        else:
            raise ConditionError("Impossible de mettre à jour le dictionnaire, car estMutable est False.")

    def pop(self, cle, *args):
        """Supprime et renvoie la valeur associée à la clé spécifiée."""
        if self.estMutable:
            # Ajoute le commit
            message = f"Suppression de la clé {cle}"
            self.historique.commit(message)

            return self.dictionnaire.pop(cle, *args)
        else:
            raise ConditionError("Impossible de supprimer une clé, car estMutable est False.")

    def popitem(self):
        """Supprime et renvoie une paire (clé, valeur) arbitraire du dictionnaire."""
        if self.estMutable:
            # Ajoute le commit
            message = "Suppression d'une paire (clé, valeur) arbitraire"
            self.historique.commit(message)
            return self.dictionnaire.popitem()
        else:
            raise ConditionError("Impossible de supprimer une paire, car estMutable est False.")

    def clear(self):
        """Supprime tous les éléments du dictionnaire."""
        if self.estMutable:
            self.dictionnaire.clear()
            # Ajoute le commit
            message = "Suppression de tous les éléments du dictionnaire"
            self.historique.commit(message)
        else:
            raise ConditionError("Impossible de vider le dictionnaire, car estMutable est False.")

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
            if (key in self.dictionnaire):
                # Si la clé existe déjà dans le dictionnaire actuel, nous devons fusionner les valeurs.
                if (value != self.dictionnaire[key]) :
                    current_value = self.dictionnaire[key]
                    if (isinstance(current_value, list)):
                        # Si la valeur actuelle est une liste, nous étendons cette liste avec les nouvelles valeurs.
                        current_value.append(value)
                        self.dictionnaire[key] = sorted(current_value)
                    else:
                        # Si la valeur actuelle n'est pas une liste, nous transformons les deux valeurs en liste et les fusionnons.
                        self.dictionnaire[key] = [current_value, value]
            else:
                # Si la clé n'existe pas dans le dictionnaire actuel, nous l'ajoutons simplement avec sa valeur.
                self.dictionnaire[key] = value
        # Ajoute le commit
        message = "Fusion des informations avec un autre EvoDict"
        self.historique.commit(message)

    def supprimeParIndex(self, index):
        """
        Supprime une clé en fonction de son index dans le dictionnaire.

        Args:
            index (int): L'index de la clé à supprimer.
        """
        if (self.estMutable) :
            keys = list(self.dictionnaire.keys())
            if 0 <= index < len(keys):
                key_to_delete = keys[index]
                del self.dictionnaire[key_to_delete]
            else:
                print("L'indice spécifié est hors de la plage du dictionnaire.")
            # Ajoute le commit
            message = f"Suppression de la clé à l'index {index}"
            self.historique.commit(message)
        else:
            raise ConditionError("Impossible de supprimer la valeur car le dictionnaire n'est pas mutable")    

    # Méthode d'Export
    def export(self, File) :
        try :
            with open(File+".txt", "wb") as f:
                dump(self.dictionnaire, f)
        except:
            if (File == ""):
                raise ExportError("Le nom du fichier ne doit pas être vide")    
        # Ajoute le commit
        message = "Export du dictionnaire vers un fichier"
        self.historique.commit(message)

    # Méthode d'Import
    def Import(self, File):
        try:
            with open(File + ".txt", "rb") as f:
                self.dictionnaire=load(f)
        except:
            raise ImportationError()
        # Ajoute le commit
        message = "Import du dictionnaire depuis un fichier"
        self.historique.commit(message)
        
    def put(self, key, values, index):
        """
        Insère une paire clé-valeur à un index spécifique dans le dictionnaire.

        Args:
            key: La clé à insérer.
            values: La valeur associée à la clé.
            index: L'index où insérer la paire clé-valeur.
        """
        if (self.estMutable):
            if index > len(self.dictionnaire):
                for i in range(len(self.dictionnaire), index):
                    self.dictionnaire["NotAkey"+str(i)] = None
            self.dictionnaire[key] = values
            message = f"Insertion de la paire clé-valeur à l'index {index}"
            self.historique.commit(message)
        else:
            raise ConditionError("Impossible d'insérer une nouvelle valeur ou clé a partir d'un index car le dictionnaire n'est pas mutable")    