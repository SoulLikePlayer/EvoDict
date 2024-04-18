from tabulate import tabulate

class EvoDict:
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
        if dictionnaire is None:
            self.dictionnaire = dict()
        else:
            self.dictionnaire = dictionnaire
        self.nom_cle = cle
        self.nom_valeur = valeur
        self.not_a_key_counter = 0
        
        # Méthodes de manipulation du dictionnaire

    def __getitem__(self, cle):
        """Renvoie la valeur associée à la clé spécifiée."""
        if (isinstance(self.dictionnaire[cle], list)):
            for i in range(len(self.dictionnaire[cle])) : 
                print(self.dictionnaire[cle][i]," ", end="")
        else:   
            return self.dictionnaire[cle]
        
    def __setitem__(self, cle, valeur):
        """Définit la valeur associée à la clé spécifiée."""
        if (valeur in self.dictionnaire.values()):
            for k, v in self.dictionnaire.items():
                if ((v == valeur) and ("NotAkey" in k)):
                    valeur = self.dictionnaire.pop(k)
                    self.not_a_key_counter -= 1
                    break
        if (cle in self.dictionnaire.keys()) :
          valeur2 = valeur
          valeur1 = self.dictionnaire[cle]
          if (isinstance(valeur1, list)):
            valeur1.append(valeur2)
            self.dictionnaire[cle] = valeur1
          else:
            self.dictionnaire[cle] = [valeur1, valeur2]
        else:
          self.dictionnaire[cle] = valeur
    
    def __delitem__(self, cle):
        """
        Supprime une clé et la remplace par une clé unique de type "NotAkey".
        La valeur associée reste dans le dictionnaire.
        """
        if cle in self.dictionnaire:
            self.not_a_key_counter += 1
            not_a_key = "NotAkey" + str(self.not_a_key_counter)
            while not_a_key in self.dictionnaire:
                self.not_a_key_counter += 1
                not_a_key = "NotAkey" + str(self.not_a_key_counter)
            self.dictionnaire[not_a_key] = self.dictionnaire.pop(cle)              
     
    #Methode de copie         
    def __copy__(self):
        """Renvoie une copie superficielle du dictionnaire."""
        return EvoDict(self.dictionnaire.copy(), self.nom_cle, self.nom_valeur)     
    
    def __deepcopy__(self, memo):
        """Renvoie une copie en profondeur du dictionnaire."""
        from copy import deepcopy
        return EvoDict(deepcopy(self.dictionnaire, memo), self.nom_cle, self.nom_valeur)  
    
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
