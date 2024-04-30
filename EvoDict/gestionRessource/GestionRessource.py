from EvoDict import EvoDict

class GestionRessource(EvoDict):
  def __init__(self, dictionnaire = None):
    super().__init__(dictionnaire, "Objet", "Quantité")