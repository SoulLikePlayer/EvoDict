from EvoDict.graphsModule import Graphe

class BellmanFord(Graphe):
    """
    Classe représentant l'algorithme de Bellman-Ford pour trouver le chemin le plus court dans un graphe non pondéré.

    Attributes:
        graphe (Graphe): Le graphe non pondéré.
        debut (str): Le sommet de départ du chemin.
        fin (str): Le sommet d'arrivée du chemin.
    """
    def __init__(self, graphe, debut=None, fin=None):
        """
        Initialise un nouvel objet de la classe BellmanFord.

        Args:
            graphe (Graphe): Le graphe non pondéré.
            debut (str, optional): Le sommet de départ du chemin. Par défaut, None.
            fin (str, optional): Le sommet d'arrivée du chemin. Par défaut, None.
        """
        self.graphe = graphe
        self.debut = debut if debut else next(iter(self.graphe.dictionnaire.keys()), None)
        self.fin = fin if fin else list(self.graphe.dictionnaire.keys())[-1]

    def __call__(self):
        """
        Trouve le chemin le plus court dans le graphe non pondéré à l'aide de l'algorithme de Bellman-Ford.
        Crée un nouveau graphe pondéré représentant le chemin le plus court.

        Returns:
            GraphePondere: Le graphe pondéré représentant le chemin le plus court.
        """
        if self.debut not in self.graphe.dictionnaire or self.fin not in self.graphe.dictionnaire:
            raise ValueError("Les sommets de départ et d'arrivée doivent être présents dans le graphe.")

        # Initialisation
        distance = {sommet: float("inf") for sommet in self.graphe.dictionnaire}
        distance[self.debut] = 0
        predecesseur = {}

        # Algorithme de Bellman-Ford
        for _ in range(len(self.graphe.dictionnaire) - 1):
            for sommet, voisins in self.graphe.dictionnaire.items():
                for voisin in voisins:
                    if distance[sommet] + 1 < distance[voisin]:
                        distance[voisin] = distance[sommet] + 1
                        predecesseur[voisin] = sommet

        # Création du graphe pondéré représentant le chemin le plus court
        chemin_courant = self.fin
        chemin_plus_court = []
        while chemin_courant != self.debut:
            chemin_plus_court.insert(0, (predecesseur[chemin_courant], chemin_courant))
            chemin_courant = predecesseur[chemin_courant]

        # Créer le nouveau graphe représentant le chemin le plus court
        nouveau_graphe = Graphe()
        for depart, arrivee in chemin_plus_court:
            nouveau_graphe[depart] = [arrivee]

        print(nouveau_graphe)
        return nouveau_graphe