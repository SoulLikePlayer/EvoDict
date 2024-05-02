# Contenu de __init__.py dans le sous-dossier EvoDict

# Exposer les classes principales du package
from .EvoDictModule import Evodict
from .exceptionsModule import FusionError, ExportError, ImportationError
from .graphsModule import Graphe, Arbre, Matrice, MatriceEchelonneeReduite, MatriceBinaire, MatriceTriangulaire, ArbreBinaire, BellmanFord, GraphePondere, Dijkstra
from .gestionRessourceModule import GestionRessource
from .SystemePermissionModule import SystemePermission

# Déclarer les éléments à exposer lors de l'importation avec "*"

__all__ = ["Evodict", "Graphe", "FusionError", "ExportError", "ImportationError", "Arbre", "Matrice", "MatriceEchelonneeReduite", "MatriceBinaire", "MatriceTriangulaire", "ArbreBinaire", "GestionRessource", "BellmanFord", "Resolution", "Dijkstra", "GraphePondere", "SystemePermission"]
