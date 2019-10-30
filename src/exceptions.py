class Error(Exception):
    pass

class NotaError(Error):
    """Excepcion para una nota mayor que 10 o menor que 0.

    Atributos:
        nota -- nota de entrada que ha producido el error.
        message -- explicacion del error

    """
    def __init__(self, nota, message):
        self.nota = nota
        self.message = message
