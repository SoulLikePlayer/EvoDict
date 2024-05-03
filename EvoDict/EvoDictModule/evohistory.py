class EvoHistory:
  def __init__(self, EvoDict):
    self.dictionnaire_historique_main = [EvoDict.dictionnaire]
    self.commit_main = ["Système inial"]
    
  def commit(self, message, EvoDict):
    self.dictionnaire_historique_main.append(EvoDict.dictionnaire)
    self.commit_main.append(message)
  
  def __str__(self):
    return self.commit_main[0]  