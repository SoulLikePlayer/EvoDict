from EvoDict import *

dictionnaire = Evodict()

dictionnaire["A"] = 2
dictionnaire["B"] = 2
del dictionnaire["A"]
dictionnaire["A"] = 1

dictionnaire.historique.branch("test", True)

dictionnaire.historique.reset(hard=True)

dictionnaire.historique.checkout("test")

dictionnaire.historique()