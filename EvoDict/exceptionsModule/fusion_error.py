#Exception de EvoDict en cas d'erreur de fusions

class FusionError(Exception):
    """Exception levée lorsqu'il y a une incompatibilité lors de la fusion de deux EvoDict."""
    def __init__(self, message="Erreur de fusion : Les clés ou les valeurs ne correspondent pas."):
        self.message = message
        super().__init__(self.message)