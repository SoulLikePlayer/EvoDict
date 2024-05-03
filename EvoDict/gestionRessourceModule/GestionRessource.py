from EvoDict import Evodict
import matplotlib.pyplot as plt

class GestionRessource(Evodict):
<<<<<<< HEAD
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
=======
    """
    Classe représentant un dictionnaire de gestion de ressources.

    Attributes:
        Dictionnaire (dict): Le dictionnaire contenant les données.
    """
    
    def __init__(self, dictionnaire=None):
        """
        Initialise un nouvel objet de la classe GestionRessource.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données de gestion de ressources. Par défaut, None.
        """
        # Appel du constructeur de la classe parente avec les noms de clé et de valeur appropriés
        super().__init__(dictionnaire, "Objet", "Quantité")

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
        if cle in self.dictionnaire.keys():
            # Si la clé existe déjà, ajoute la nouvelle valeur à la valeur existante
            if isinstance(valeur, int) or isinstance(valeur, float):
                self.dictionnaire[cle] += round(valeur, 2)  
            else:
                raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
        else:
            # Si la clé n'existe pas, crée une nouvelle entrée dans le dictionnaire avec la clé spécifiée et la valeur associée
            if isinstance(valeur, int) or isinstance(valeur, float):
                self.dictionnaire[cle] = round(valeur, 2)  
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
        plt.title("Graphique de Gestion de Ressources")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # Renvoie une chaîne vide car l'affichage du graphique est géré par matplotlib
        return ""
>>>>>>> Graphe
