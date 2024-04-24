from EvoDict import *
evo_dict = Graphe({
        "A": ["B", "C", "E", "I"],
        "B": "D",
        "C": "F",
        "D": [],
        "E": ["G"],
        "F": "H",
        "G": [],
        "H": "I",
        "I": []
    })

    # Visualiser l'arbre
evo_dict["I"] = "Z"  
print(evo_dict)

evo_2 = EvoDict(evo_dict, "clé", "valeur")
print(evo_2)