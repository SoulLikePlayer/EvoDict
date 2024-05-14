from EvoDict.graphsModule import Graphe

class BellmanFord(Graphe):
    def __init__(self, graphe, depart=None, arrivee=None):
        """
        Initialise un objet BellmanFord.

        Args:
            graphe (Graphe): L'objet Graphe représentant le graphe sur lequel appliquer l'algorithme.
            depart (str, optional): Le nœud de départ. Par défaut, le premier nœud du graphe.
            arrivee (str, optional): Le nœud d'arrivée. Par défaut, le dernier nœud du graphe.
        """
        if depart is None:
            depart = next(iter(graphe.dictionnaire))
        if arrivee is None:
            arrivee = next(iter(reversed(graphe.dictionnaire)))
        self.depart = depart
        self.arrivee = arrivee
        self.dictionnaire = graphe.dictionnaire
    
    def __call__(self):
        """
        Trouve le chemin le plus court entre le nœud de départ et le nœud d'arrivée en utilisant l'algorithme de Bellman-Ford.

        Returns:
            dict: Le dictionnaire représentant le plus court chemin avec les nœuds comme clés et leurs successeurs comme valeurs.
        """
        # Utiliser l'algorithme de Bellman-Ford pour trouver le chemin le plus court
        distances = {noeud: float('inf') for noeud in self.dictionnaire}
        predecesseurs = {}
        distances[self.depart] = 0
        
        for _ in range(len(self.dictionnaire) - 1):
            for u in self.dictionnaire:
                for v in self.dictionnaire[u]:
                    poids = 1  # Nous supposons que tous les poids sont égaux à 1
                    if distances[u] + poids < distances[v]:
                        distances[v] = distances[u] + poids
                        predecesseurs[v] = u
        
        # Reconstruire le chemin le plus court à partir des prédecesseurs
        chemin = [self.arrivee]
        while self.arrivee != self.depart:
            self.arrivee = predecesseurs[self.arrivee]
            chemin.append(self.arrivee)
        chemin.reverse()
        
        # Créer un nouveau dictionnaire représentant le plus court chemin
        plus_court_chemin = Graphe()
        for i in range(len(chemin) - 1):
            plus_court_chemin[chemin[i]] = [chemin[i + 1]]

        print(plus_court_chemin)
        return plus_court_chemin
