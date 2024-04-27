# Contenu de __init__.py dans le sous-dossier graphs


# Importer la classe Graphe pour l'exposer dans ce sous-module
from .graph import Graphe

# Déclarer les éléments à exposer lors de l'importation avec "*"
__all__ = ["Graphe"]
