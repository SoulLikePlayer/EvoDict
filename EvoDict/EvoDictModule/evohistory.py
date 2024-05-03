import random
import string

class EvoHistory:
  '''
  Classe représentant l'historique des dictionnaire évolué
  '''
  def __init__(self, object) :
    self.dictionnaire_base = object.dictionnaire
    self.liste_dictionnaire = [self.dictionnaire_base]
    self.id = self.generer_id_random(4)
    self.liste_commit = {f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}" : f"Création du {type(object).__name}"}
    
  def generer_id_random(self, n):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=n))  
  
  def commit(self, message, dictionnaire):
    self.liste_dictionnaire.append(dictionnaire)
    self.liste_commit[f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}"] = message