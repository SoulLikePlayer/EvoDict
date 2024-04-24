        
class ExportError(Exception):
    '''Exception levée lorsqu'il y a une erreur dans l'export'''
    def __init__(self, message="Erreur de l'export"):
        self.message = message
        super().__init__(self.message)