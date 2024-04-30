from EvoDict import *

dic_ressource = {"pierre" : 2,
                    "bois" : 15}

Gestion = GestionRessource(dic_ressource)

print(Gestion)

Gestion["pierre"] = "5"

print(Gestion)