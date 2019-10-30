class NotaError(Exception):
    """Excepcion para una nota mayor que 10 o menor que 0."""
    pass

class ComentarioNoneError(Error):
    """Excepcion para un comentario de valor None."""
    pass

class ComentarioEmptyError(Error):
    """Excepcion para un comentario vacio."""
    pass

class AlumnoNoneError(Error):
    """Excepcion para un Alumno de valor None."""
    pass

class AlumnoEmptyError(Error):
    """Excepcion para un Alumno vacio."""
    pass


