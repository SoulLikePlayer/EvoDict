class ConditionError(Exception):
  def __init__(self, message = "Une erreur de condition est survenue"):
    super().__init__(message)