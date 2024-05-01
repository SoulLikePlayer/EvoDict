from EvoDict import *

dic_ressource = {"pierre" : 2,
                    "bois" : 15}

Gestion = GestionRessource(dic_ressource)

Gestion["pierre"] = 5

print(Gestion)