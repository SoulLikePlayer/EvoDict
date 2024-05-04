from EvoDict import *

dic_ressource = {}

Gestion = GestionRessource(dic_ressource)

Gestion["pierre"] = 2
Gestion["bois"] = 15
Gestion["pierre"] = 5

print(Gestion)