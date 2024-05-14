import random
import string
import tkinter as tk
from tkinter import ttk
import copy

class EvoHistory:
  '''
  Classe représentant l'historique des dictionnaire évolué
  '''
  def __init__(self, object) :
    self.object = object
    self.dictionnaire_base = copy.deepcopy(object.dictionnaire)
    self.id = self.generer_id_random(4)
    self.liste_commit = {f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}" : f"Création du {type(object).__name__}"}
    self.liste_dictionnaire = []
    self.liste_dictionnaire.append(self.dictionnaire_base)
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
        self.liste_commit[f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}"] = message
        self.dictionnaire = copy.deepcopy(self.object.dictionnaire)
        self.liste_dictionnaire.append(self.dictionnaire)
        self.refresh_treeview()
    
  def __call__(self):
    self.root.mainloop()
  
  def __str__(self):
    for cle, value in reversed(list(self.liste_commit.items())):
      print(cle, "-->", value)
    return ""