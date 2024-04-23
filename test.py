from EvoDict import *
evo_dict = EvoDict({
        "A": ["B", "C"],
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
evo_dict.Graphe()