from EvoDict import Evodict

class GestionRessource(Evodict):
  '''
    Classe représentant un dictionnaire de gestions de ressource
    
    Attributes :
        Dictionnaire (dict) : Le dictionnaire contenant les données.
  '''
  def __init__(self, dictionnaire = None):
    super().__init__(dictionnaire, "Objet", "Quantité")
    
  def __setitem__(self, cle, valeur):
    if (cle in self.dictionnaire.keys()):
      if (isinstance(valeur, int) or isinstance(valeur, float)):
        self.dictionnaire[cle] += round(valeur, 2)  
      else:
        raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))
    else:  
      if (isinstance(valeur, int) or isinstance(valeur, float)):
        self.dictionnaire[cle] = round(valeur, 2)  
      else:
        raise TypeError("Le type de valeurs ne peut pas être '{}', elle ne peut être que int et float".format(type(valeur).__name__))