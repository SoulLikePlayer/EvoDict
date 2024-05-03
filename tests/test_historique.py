from EvoDict import *

dictionnaire = Evodict()
dictionnaire2 = Evodict()

dictionnaire["A"] = 2
dictionnaire2["B"] = 50

print(dictionnaire.historique)
print("----------------------")
print(dictionnaire2.historique)