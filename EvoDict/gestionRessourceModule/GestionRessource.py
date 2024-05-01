from EvoDict import Evodict
import matplotlib.pyplot as plt

class GestionRessource(Evodict):
    '''
    Classe représentant un dictionnaire de gestions de ressource
    
    Attributes :
        Dictionnaire (dict) : Le dictionnaire contenant les données.
    '''
    def __init__(self, dictionnaire=None):
        super().__init__(dictionnaire, "Objet", "Quantité")
    
    def __setitem__(self, cle, valeur):
        if cle in self.dictionnaire.keys():
            if isinstance(valeur, int) or isinstance(valeur, float):
                self.dictionnaire[cle] += round(valeur, 2)  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
        else:  
            if isinstance(valeur, int) or isinstance(valeur, float):
                self.dictionnaire[cle] = round(valeur, 2)  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))

    def __str__(self):
        """
        Affiche le dictionnaire sous forme de graphique à barres.
        """
        clefs = list(self.dictionnaire.keys())
        valeurs = list(self.dictionnaire.values())

        plt.figure(figsize=(10, 6))
        plt.bar(clefs, valeurs, color='blue')
        plt.xlabel(self.nom_cle)
        plt.ylabel(self.nom_valeur)
        plt.title("Graphique de Gestion de Ressources")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        return ""