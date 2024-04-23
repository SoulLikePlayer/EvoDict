from EvoDict import *

def fibonacci(n):
    """
    Fonction pour calculer les n premiers termes de la suite de Fibonacci.
    """
    fib_dict = EvoDict({"0": 0, "1": 1})  # Initialisation du dictionnaire avec les deux premiers termes
    for i in range(2, n):
        fib_dict[str(i)] = fib_dict[str(i-1)] + fib_dict[str(i-2)]  # Calcul des termes suivants
    return fib_dict

# Test avec les 10 premiers termes de Fibonacci
n = 10
fibonacci_dict = fibonacci(n)
print("Suite de Fibonacci jusqu'au", n, "ème terme")
fibonacci_dict.Graphe()

