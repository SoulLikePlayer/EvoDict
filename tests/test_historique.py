from EvoDict import *

dictionnaire = Evodict()

dictionnaire["A"] = 2
dictionnaire["B"] = 2
del dictionnaire["A"]
dictionnaire["A"] = 1

dictionnaire.historique.branch("test", True)

print(dictionnaire.historique)
dictionnaire.historique.reset(hard=True)
print(dictionnaire)
print(dictionnaire.historique.liste_dictionnaire)