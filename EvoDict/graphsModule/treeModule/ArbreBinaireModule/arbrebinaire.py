from EvoDict.graphsModule.treeModule import Arbre

class ArbreBinaire(Arbre):
  def __init__(sel, dictionnaire):
    super().__init__(dictionnaire, "key", "value")
    
  def __setitem__(self, cle, valeur):
    if (cle in list(self.dictionnaire.keys())):
      if (isinstance(self.dictionnaire[cle]) and len(self.dictionnaire[cle]) == 2):
        raise ValueError("Impossible de mettre plus de 2 clé sur chaque noeud")