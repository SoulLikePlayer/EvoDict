from EvoDict import Evodict

class Geodict(Evodict):
  def __init__(self):
    self.dictionnaire = {"attitude" : 0,
                         "longitude" : 0}
    super().__init__(self.dictionnaire, cle="Type de Coordonnée", valeur="Coordonnée", limMaxVal=1)
  
  def __str__(self):
    StringBuilder = "Coordonnée : ("+str(self.dictionnaire["attitude"])+","+str(self.dictionnaire["longitude"])+")"
    return StringBuilder
    