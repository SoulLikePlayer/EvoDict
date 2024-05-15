import random
import string
import tkinter as tk
from tkinter import ttk
import copy
from EvoDict.exceptionsModule import EvoHistoryError

class EvoHistory:
  '''
  Classe représentant l'historique des dictionnaire évolué
  '''
  def __init__(self, object) :
    self.object = object
    self.dictionnaire_base = copy.deepcopy(object.dictionnaire)
    self.id = self.generer_id_random(4)
    self.liste_commit = {"main": {f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}" : f"Création du {type(object).__name__}"}}
    self.liste_dictionnaire = {"main" : []}
    self.liste_dictionnaire["main"].append(self.dictionnaire_base)
    
    self.branche_actuelle = "main"
    # Création de l'interface graphique
    self.root = tk.Tk()
    self.root.title(f"EvoHistory {self.id}")
    self.tree = ttk.Treeview(self.root)
    self.tree.pack(expand=True, fill=tk.BOTH)
    self.refresh_treeview()
       
  def generer_id_random(self, n):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=n))  
  
  def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for commit, message in reversed(list(self.liste_commit.items())):
          self.tree.insert("", "end", text=commit[:16]+" : "+message)
        self.root.update()

  def commit(self, message):
        self.liste_commit[self.branche_actuelle][f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}"] = message
        self.dictionnaire = copy.deepcopy(self.object.dictionnaire)
        self.liste_dictionnaire[self.branche_actuelle].append(self.dictionnaire)
        self.refresh_treeview()
        
  def reset(self, nb = 1, hard = False):
     if (hard):
       self.object.dictionnaire = self.liste_dictionnaire[self.branche_actuelle][0]     
     else:
       self.object.dictionnaire = self.liste_dictionnaire[self.branche_actuelle][len(self.liste_dictionnaire) - nb]
     taille = len(self.liste_dictionnaire[self.branche_actuelle])-1
     suppr = True
     while (taille >= 0):
       if(self.liste_dictionnaire[self.branche_actuelle][taille] != self.object.dictionnaire and suppr == True):
         del self.liste_dictionnaire[self.branche_actuelle][taille]
       elif(self.liste_dictionnaire[self.branche_actuelle][taille] == self.object.dictionnaire):
         suppr = False  
       taille -= 1
  
  def branch(self, nom_de_branche, copy_dict = False):
    self.liste_dictionnaire[nom_de_branche] = []
    self.liste_commit[nom_de_branche] = []
    if (copy_dict):
      for element in self.liste_dictionnaire[self.branche_actuelle]:
        self.liste_dictionnaire[nom_de_branche].append(copy.deepcopy(element))  
  
  def checkout(self, nom_de_branche):
    if (nom_de_branche not in list(self.liste_dictionnaire.keys())):
      raise EvoHistoryError("Vous ne pouvez qu'accédez au branche que vous avez crée avant avec la commande branch")
    self.branche_actuelle = nom_de_branche
    self.object.dictionnaire = self.liste_dictionnaire[self.branche_actuelle][-1]
    print(f"switch a la branche {self.branche_actuelle}")
          
  def __call__(self):
    self.root.mainloop()
  
  def __str__(self):
    for cle, value in reversed(list(self.liste_commit.items())):
      print(cle, "-->", value)
    return ""