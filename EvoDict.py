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