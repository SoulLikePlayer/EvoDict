from EvoDict import Evodict
import matplotlib.pyplot as plt

class GestionRessource(Evodict):
    """
    Classe représentant un dictionnaire de gestion de ressources.

    Attributes:
        Dictionnaire (dict): Le dictionnaire contenant les données.
    """
    
    def __init__(self, titre, dictionnaire=None):
        """
        Initialise un nouvel objet de la classe GestionRessource.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données de gestion de ressources. Par défaut, None.
        """
        # Appel du constructeur de la classe parente avec les noms de clé et de valeur appropriés
        super().__init__(dictionnaire, "Objet", "Quantité")
        self.titre = titre

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée dans le dictionnaire.

        Si la clé existe déjà, ajoute la nouvelle valeur à la valeur existante.
        Sinon, crée une nouvelle entrée dans le dictionnaire avec la clé spécifiée et la valeur associée.

        Args:
            cle (str): La clé à définir.
            valeur (int ou float): La valeur à associer à la clé.
        
        Raises:
            TypeError: Si le type de valeur n'est ni int ni float.
        """
        print(type(self.dictionnaire).__name__)
        if cle in list(self.dictionnaire.keys()):
            # Si la clé existe déjà, ajoute la nouvelle valeur à la valeur existante
            if isinstance(valeur, int) or isinstance(valeur, float):
                self.dictionnaire[cle] += round(valeur, 2)  
                self.historique.commit(f"Adition de la valeur {round(valeur, 2)} a la clé {cle}")
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
        else:  
            if (isinstance(valeur, int) or isinstance(valeur, float)):
                super().__setitem__(cle, round(valeur, 2))  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))

    def __str__(self):
        """
        Affiche le dictionnaire sous forme de graphique à barres.

        Returns:
            str: Une chaîne vide, car l'affichage du graphique est géré par matplotlib.
        """
        # Récupère les clés et les valeurs du dictionnaire
        clefs = list(self.dictionnaire.keys())
        valeurs = list(self.dictionnaire.values())

        # Crée un graphique à barres avec les données du dictionnaire
        plt.figure(figsize=(10, 6))
        plt.bar(clefs, valeurs, color='blue')
        plt.xlabel(self.nom_cle)
        plt.ylabel(self.nom_valeur)
        plt.title(f"Graphique de Gestion de Ressources : {self.titre}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # Renvoie une chaîne vide car l'affichage du graphique est géré par matplotlib
        return ""
    
    def fusions(self, other):
        self.titre = "Fusions de " +self.titre + " et de " +other.titre
        return super().fusions(other)