from EvoDict import *

dictionnaire = Evodict()

dictionnaire["A"] = 2
dictionnaire["B"] = 2
del dictionnaire["A"]
dictionnaire["A"] = 1

print(dictionnaire.historique)
dictionnaire.historique.reset(nb=2)
print(dictionnaire)
print(dictionnaire.historique.liste_dictionnaire)