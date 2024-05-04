from EvoDict import *

dictionnaire = Evodict()

dictionnaire["A"] = 2
dictionnaire["B"] = 2
del dictionnaire["A"]
dictionnaire["A"] = 1

print(dictionnaire.historique)
print(dictionnaire.historique.liste_dictionnaire)

dictionnaire.historique()