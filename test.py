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
evo_dict["I"] = "J"    
print(evo_dict)