from EvoDict.graphsModule.treeModule import Arbre

class ArbreBinaire(Arbre):
  def __init__(self, dictionnaire=None):
    super().__init__(dictionnaire, "key", "value")
    
  def __setitem__(self, cle, valeur):
      if (cle in self.dictionnaire.keys()):
        if ((isinstance(self.dictionnaire[cle], list)) and (len(self.dictionnaire[cle]) == 2)):
          raise ValueError("Le noeud ne peut avoir plus de 2 fils")
        test = self.dictionnaire[cle]
      else:
        test= []
      
      if (isinstance(valeur, list)):
        if (len(valeur) > 2):
          raise ValueError("Le noeud ne peut contenir plus de 2 fils")
        else :
          for value in valeur:
            test.append(value)
      else:
          test.append(valeur)
      
      if(len(test) > 2):
        raise ValueError("Le noeud ne peut contenir plus de 2 fils")
      return super().__setitem__(cle, valeur)
    