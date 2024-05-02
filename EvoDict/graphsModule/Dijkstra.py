from EvoDict.graphsModule import GraphePondere

class Dijkstra(GraphePondere):
    """
    Classe représentant l'algorithme de Dijkstra pour trouver le chemin le plus court dans un graphe pondéré.

    Attributes:
        graphe (GraphePondere): Le graphe pondéré.
        debut (str): Le sommet de départ du chemin.
        fin (str): Le sommet d'arrivée du chemin.
    """
    def __init__(self, graphe, debut=None, fin=None):
        """
        Initialise un nouvel objet de la classe Dijkstra.

        Args:
            graphe (GraphePondere): Le graphe pondéré.
            debut (str, optional): Le sommet de départ du chemin. Par défaut, None.
            fin (str, optional): Le sommet d'arrivée du chemin. Par défaut, None.
        """
        self.dictionnaire = graphe.dictionnaire
        self.debut = debut if debut else next(iter(self.dictionnaire.keys()), None)
        self.fin = fin if fin else list(self.dictionnaire.keys())[-1]
        print(self.dictionnaire)

    def __call__(self):
        """
        Trouve le chemin le plus court dans le graphe pondéré à l'aide de l'algorithme de Dijkstra.
        Crée un nouveau graphe pondéré représentant le chemin le plus court.

        Returns:
            GraphePondere: Le graphe pondéré représentant le chemin le plus court.
        """
        if self.debut not in self.dictionnaire or self.fin not in self.dictionnaire:
            raise ValueError("Les sommets de départ et d'arrivée doivent être présents dans le graphe.")

        # Initialisation
        distance = {sommet: float("inf") for sommet in self.dictionnaire}
        distance[self.debut] = 0
        predecesseur = {}
        non_visites = set(self.dictionnaire.keys())

        # Algorithme de Dijkstra
        while non_visites:
            sommet_courant = min(non_visites, key=lambda sommet: distance[sommet])
            non_visites.remove(sommet_courant)
            if distance[sommet_courant] == float("inf"):
                break
            for voisin, poids in self.dictionnaire[sommet_courant].items():
                nouvelle_distance = distance[sommet_courant] + poids
                if nouvelle_distance < distance[voisin]:
                    distance[voisin] = nouvelle_distance
                    predecesseur[voisin] = sommet_courant

        # Création du graphe pondéré représentant le chemin le plus court
        chemin_courant = self.fin
        chemin_plus_court = []
        while chemin_courant != self.debut:
            chemin_plus_court.insert(0, (predecesseur[chemin_courant], chemin_courant, distance[chemin_courant]))
            chemin_courant = predecesseur[chemin_courant]

        # Créer le nouveau graphe pondéré représentant le chemin le plus court
        nouveau_graphe = GraphePondere()
        for depart, arrivee, poids in chemin_plus_court:
            nouveau_graphe[depart] = [arrivee, poids]
        
        print(nouveau_graphe)
        return nouveau_graphe