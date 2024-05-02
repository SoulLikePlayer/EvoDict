from EvoDict import Evodict

class GestionRessource(Evodict):
    '''
        Classe représentant un dictionnaire de gestions de ressource
        
        Attributes :
            Dictionnaire (dict) : Le dictionnaire contenant les données.
    '''
    def __init__(self, dictionnaire = None):
        super().__init__(dictionnaire, "Objet", "Quantité")
        
    def __setitem__(self, cle, valeur):
        if (cle in self.dictionnaire.keys()):
            if (isinstance(valeur, int) or isinstance(valeur, float)):
                self.dictionnaire[cle] += round(valeur, 2)  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
        else:  
            if (isinstance(valeur, int) or isinstance(valeur, float)):
                self.dictionnaire[cle] = round(valeur, 2)  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
        
    def mettre_a_jour_ressource(self, cle, quantite):
        """
        Met à jour la quantité de ressource à une clé donnée.

        Args:
            cle (str): La clé de la ressource à mettre à jour.
            quantite (float): La nouvelle quantité de ressource.

        Raises:
            ValueError: Si la quantité spécifiée est négative.
        """
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative.")
        else:
            self[cle] = quantite

    def verifier_disponibilite_ressource(self, cle, quantite):
        """
        Vérifie si une quantité spécifiée de ressource est disponible à une clé donnée.

        Args:
            cle (str): La clé de la ressource à vérifier.
            quantite (float): La quantité de ressource à vérifier.

        Returns:
            bool: True si la quantité de ressource est disponible, False sinon.
        """
        return self.get(cle, 0) >= quantite

    def get_ressource(self, cle = None):
        if (cle == None) :
            return self.dictionnaire
        return self.dictionnaire[cle]