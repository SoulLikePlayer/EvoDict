from EvoDict.graphsModule import Graphe

class BellmanFord(Graphe):
    def __init__(self, graphe, depart, fin):
        if (isinstance(graphe, Graphe) != True):
          raise TypeError("vous devez mettre un graphe en paramètre, pas un {}".format(type(graphe).__name__))
        super().__init__(graphe.dictionnaire)
        self.depart = depart
        self.fin = fin
        self.distance, self.predecesseurs = self.bellman_ford()

    def bellman_ford(self):
        # Initialisation des distances à l'infini pour tous les nœuds sauf le départ
        distances = {noeud: float('inf') for noeud in self.dictionnaire}
        distances[self.depart] = 0
        predecesseurs = {}

        # Parcours des arêtes |V| - 1 fois
        for _ in range(len(self.dictionnaire) - 1):
            for source in self.dictionnaire:
                for cible, poids in self.dictionnaire[source].items():
                    # Mise à jour de la distance si un chemin plus court est trouvé
                    if distances[source] != float('inf') and distances[source] + poids < distances[cible]:
                        distances[cible] = distances[source] + poids
                        predecesseurs[cible] = source

        # Vérification des cycles de poids négatifs
        for source in self.dictionnaire:
            for cible, poids in self.dictionnaire[source].items():
                if distances[source] != float('inf') and distances[source] + poids < distances[cible]:
                    raise ValueError("Le graphe contient un cycle de poids négatifs")

        return distances, predecesseurs

    def chemin_plus_court(self):
        chemin = []
        noeud_actuel = self.fin
        while noeud_actuel != self.depart:
            chemin.append(noeud_actuel)
            noeud_actuel = self.predecesseurs[noeud_actuel]
        chemin.append(self.depart)
        chemin.reverse()

        return chemin, self.distance[self.fin]
