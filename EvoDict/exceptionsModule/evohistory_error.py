class EvoHistoryError(Exception):
  def __init__(message = "Une erreur c'est produit"):
    super().__init__(message)