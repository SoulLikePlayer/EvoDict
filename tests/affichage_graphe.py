import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from EvoDict import *

graphe = {"A" : ["B"],
          "B" : ["C"],
          "C" : ["D"],
          "D" : ["A"]}

EvoGraphe = Graphe(graphe)
print(EvoGraphe)
