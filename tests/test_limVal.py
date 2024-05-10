from EvoDict import *

evodict_avec_limie = Evodict({'A' : 'BEC'}, limMaxVal=2)
evodict_avec_limie['A'] = 'C'
evodict_avec_limie['A'] = 'D'
print(evodict_avec_limie)