import networkx as nx
import matplotlib.pyplot as plt
from EvoDict import Evodict

class Graphe(Evodict):
    """
    Classe représentant un graphe basé sur un dictionnaire.

    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données du graphe.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
    """

    def __init__(self, dictionnaire=None, cle="key", valeur="value", limMaxVal = None):
        """
        Initialise un nouvel objet de la classe Graphe.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données du graphe. Par défaut, None.
            cle (str, optional): Le nom à utiliser pour les clés dans le dictionnaire. Par défaut, "key".
            valeur (str, optional): Le nom à utiliser pour les valeurs dans le dictionnaire. Par défaut, "value".
        """
        # Appel du constructeur de la classe parente avec les noms de clé et de valeur appropriés
        print(type(limMaxVal).__name__)
        super().__init__(dictionnaire, cle, valeur, limMaxVal=limMaxVal)

    def __setitem__(self, cle, valeur):
        """
        Définit la valeur associée à la clé spécifiée dans le dictionnaire.

        Si la clé existe déjà, ajoute la nouvelle valeur à la valeur existante.
        Sinon, crée une nouvelle entrée dans le dictionnaire avec la clé spécifiée et la valeur associée.

        Args:
            cle (str): La clé à définir.
            valeur (list): La liste des valeurs associées à la clé.

        Raises:
            TypeError: Si la valeur n'est pas une liste.
        """
        # Appel de la méthode de la classe parente pour définir la valeur associée à la clé spécifiée
        super().__setitem__(cle, valeur)
        # Ajout des valeurs comme des clés avec des listes vides comme valeurs associées
        for value in valeur:
            if value not in list(self.dictionnaire.keys()):
                super().__setitem__(cle, [])

    def __str__(self):
        """
        Affiche le dictionnaire sous forme de graphe dirigé à l'aide du parcours en profondeur.

        Returns:
            str: Une chaîne vide, car l'affichage du graphe est géré par matplotlib.
        """
        # Création d'un graphe dirigé pour représenter le graphe
        G = nx.DiGraph()

        # Fonction auxiliaire pour parcourir le graphe en profondeur et ajouter des nœuds et des arêtes au graphe
        visited = set()  # Ensemble pour suivre les nœuds déjà visités
        def dfs(node, parent=None):
            if node in visited:
                if parent is not None and self.dictionnaire[parent] is not None:
                    G.add_edge(parent, node)  # Si le nœud a déjà été visité, on arrête la récursion
                return
            visited.add(node)
            G.add_node(node)
            if parent is not None and self.dictionnaire[parent] is not None:
                G.add_edge(parent, node)
            children = self.dictionnaire.get(node, [])
            if isinstance(children, list):
                for child in children:
                    dfs(child, node)
            else:
                dfs(children, node)

        # Commencer le parcours en profondeur à partir de la racine du graphe
        root = next(iter(self.dictionnaire.keys()), None)
        if root is not None:
            dfs(root)

        # Dessiner le graphe
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

        # Renvoyer une chaîne vide car l'affichage du graphe est géré par matplotlib
        return ""
