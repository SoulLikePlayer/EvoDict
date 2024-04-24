class ImportationError(Exception):
    '''Exception levée lorsqu'il y a une erreur dans l'import'''
    def __init__(self, message="Erreur de l'import"):
        self.message = message
        super().__init__(self.message)                        

    
