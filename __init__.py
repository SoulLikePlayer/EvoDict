# Contenu de __init__.py à la racine du package

# Importer les classes principales des sous-modules
from .EvoDict import *

# Déclarer les éléments à exposer lors de l'importation avec "*"
__all__ = EvoDict.__all__
