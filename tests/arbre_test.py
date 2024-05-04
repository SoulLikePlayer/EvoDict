import unittest
from EvoDict import *

class TestVisualisationArbre(unittest.TestCase):
    def test_visualiser_arbre_vide(self):
        """Test de visualisation d'un arbre vide."""
        arbre = Arbre()
        print("Visualisation de l'arbre vide :")
        print(arbre)

    def test_visualiser_arbre_un_seul_noeud(self):
        """Test de visualisation d'un arbre avec un seul nœud."""
        arbre = Arbre({"A": []})
        print("Visualisation de l'arbre avec un seul nœud :")
        print(arbre)

    def test_visualiser_arbre_equilibre(self):
        """Test de visualisation d'un arbre équilibré."""
        arbre = Arbre({"B": ["D", "E"], "C": ["F", "G"]})
        arbre["A"] = ["B", "C"]
        print("Visualisation de l'arbre équilibré :")
        print(arbre)

    def test_visualiser_arbre_desequilibre(self):
        """Test de visualisation d'un arbre déséquilibré."""
        arbre = Arbre({"A": ["B"], "B": ["C"], "C": ["D", "E"]})
        print("Visualisation de l'arbre déséquilibré :")
        print(arbre)

if __name__ == "__main__":
    unittest.main()
