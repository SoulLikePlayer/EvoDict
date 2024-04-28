import networkx as nx
import matplotlib.pyplot as plt
from EvoDict.graphsModule import Graphe

class Arbre(Graphe):
    def __init__(self, dictionnaire=None, cle="key", valeur="value"):
        super().__init__(dictionnaire, cle, valeur)
    
    def __setitem__(self, cle, valeur):
      if (valeur in list(self.dictionnaire.keys())):
        raise ValueError()
      return super().__setitem__(cle, valeur)
     
    def __str__(self):
      return super().__str__()      