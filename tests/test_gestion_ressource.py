from EvoDict import *

dic_ressource = {}

Gestion = GestionRessource("Pioche de fer", dic_ressource)

Gestion["baton"] = 2
Gestion["fer"] = 3

Gestion2 = GestionRessource("Pioche de bois", {"baton" : 2,
                                               "bois" : 3})

Gestion.fusions(Gestion2)
print(Gestion)