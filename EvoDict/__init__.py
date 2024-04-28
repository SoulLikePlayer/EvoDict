# Contenu de __init__.py dans le sous-dossier EvoDict

# Exposer les classes principales du package
from .EvoDict import EvoDict
from .exceptions import FusionError, ExportError, ImportationError
from .graphs import Graphe, Arbre, Matrice

# Déclarer les éléments à exposer lors de l'importation avec "*"
__all__ = ["EvoDict", "Graphe", "FusionError", "ExportError", "ImportationError", "Arbre", "Matrice"]
