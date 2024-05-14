import unittest
from EvoDict import Evodict

def fibonacci(n):
    """Retourne les n premiers nombres de la suite de Fibonacci."""
    fibo_values = [0, 1]
    for i in range(2, n):
        fibo_values.append(fibo_values[-1] + fibo_values[-2])
    return fibo_values[:n]

class TestEvoDictSetItem(unittest.TestCase):
    def test_setitem_fibonacci(self):
        # Création d'une instance de EvoDict
        evodict = Evodict(None, "Index", "Valeur")

        # Obtention des 10 premiers nombres de la suite de Fibonacci
        fibo_values = fibonacci(10)

        # Ajout des nombres de Fibonacci dans l'EvoDict
        for i, value in enumerate(fibo_values):
            evodict["index n°{}".format(i)] = value

        # Vérification que les clés et valeurs ont été correctement ajoutées
        for i, value in enumerate(fibo_values):
            self.assertEqual(evodict["index n°{}".format(i)], value)
        
        print(evodict)    

if __name__ == "__main__":
    unittest.main()
