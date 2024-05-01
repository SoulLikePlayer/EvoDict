# Contenu de __init__.py dans le sous-dossier EvoDict

# Exposer les classes principales du package
from .EvoDictModule import Evodict
from .exceptionsModule import FusionError, ExportError, ImportationError
from .graphsModule import Graphe, Arbre, Matrice, Resolution, MatriceEchelonneeReduite, MatriceBinaire, MatriceTriangulaire

# Déclarer les éléments à exposer lors de l'importation avec "*"
__all__ = ["Evodict", "Graphe", "FusionError", "ExportError", "ImportationError", "Arbre", "Matrice", "Resolution", "MatriceEchelonneeReduite", "MatriceBinaire", "MatriceTriangulaire"]
