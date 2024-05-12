from EvoDict import *

dictionnaire_avec_nb_parents = Evodict({"A" : ["B", "C"],
                                        "C" : "B"}, limMaxParent=2)

dictionnaire_avec_nb_parents["D"] = "C"
dictionnaire_avec_nb_parents["E"] = "C"
print(dictionnaire_avec_nb_parents)