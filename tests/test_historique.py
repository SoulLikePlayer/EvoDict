from EvoDict import *


dictionnaire = Evodict({"A" : 2})
dictionnaire['B'] = 23

print(dictionnaire.historique)

dictionnaire['B'] = 32

print(dictionnaire.historique)

#dictionnaire.historique.reset(1)