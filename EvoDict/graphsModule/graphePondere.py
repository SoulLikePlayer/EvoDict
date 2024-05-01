from EvoDict.graphsModule import Graphe
import networkx as nx
import matplotlib.pyplot as plt

class GraphePondere(Graphe):
    """
    Classe représentant un graphe pondéré.
    
    Attributes:
        dictionnaire (dict): Le dictionnaire contenant les données du graphe.
        nom_cle (str): Le nom utilisé pour désigner les clés dans le dictionnaire.
        nom_valeur (str): Le nom utilisé pour désigner les valeurs dans le dictionnaire.
    """
    
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        """
        Initialise un nouvel objet de la classe GraphePondere.

        Args:
            dictionnaire (dict, optional): Le dictionnaire initial contenant les données du graphe. Par défaut, None.
            cle (str, optional): Le nom de la clé. Par défaut, "key".
            valeur (str, optional): Le nom de la valeur. Par défaut, "value".
        """
        super().__init__(dictionnaire, cle, valeur)
    
    def __setitem__(self, cle, valeur):
        """
        Ajoute une arête pondérée au graphe en utilisant la syntaxe dictionnaire[cle] = [sommet, poids].

        Args:
            cle: Le nœud de départ de l'arête.
            valeur: Une liste contenant le nœud d'arrivée de l'arête et le poids.
        """
        if not isinstance(valeur, list):
            raise ValueError("La valeur doit être une liste.")
        if len(valeur) < 2:
            raise ValueError("La liste doit avoir au moins deux éléments.")
        if not isinstance(valeur[-1], int):
            raise ValueError("Le dernier élément de la liste doit être un entier (poids).")
        arrivee, poids = valeur[:-1], valeur[-1]
        if cle not in self.dictionnaire:
            self.dictionnaire[cle] = {}
        self.dictionnaire[cle][arrivee[0]] = poids

    
    def __str__(self):
        """
        Dessine le graphe pondéré avec les poids des arêtes inclus.
        """
        # Créer un graphe dirigé à l'aide de networkx
        G = nx.DiGraph()

        # Ajouter les nœuds au graphe
        for depart, voisins in self.dictionnaire.items():
            for arrivee, poids in voisins.items():
                G.add_edge(depart, arrivee, weight=poids)

        # Dessiner le graphe
        pos = nx.spring_layout(G)  # Positionnement des nœuds
        nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=12, arrows=True)

        # Ajouter les poids des arêtes
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Afficher le graphe
        plt.show()
        return ""
