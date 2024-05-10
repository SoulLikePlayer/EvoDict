from EvoDict import *

arbre = Arbre({
    "A": ["C", "F"],
    "C": ["B", "D"],
    "F": ["E", "G"]
})

arbre.parcours_prefixe()  # Affiche : A C B D F E G
arbre.parcours_infixe()   # Affiche : B C D A E F G
arbre.parcours_postfixe() # Affiche : B D C E G F A
