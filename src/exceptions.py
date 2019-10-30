class NotaException(Exception):
    """Excepcion para una nota mayor que 10 o menor que 0."""
    pass

class ComentarioNoneException(Exception):
    """Excepcion para un comentario de valor None."""
    pass

class ComentarioEmptyException(Exception):
    """Excepcion para un comentario vacio."""
    pass

class AlumnoNoneException(Exception):
    """Excepcion para un Alumno de valor None."""
    pass

class AlumnoEmptyException(Exception):
    """Excepcion para un Alumno vacio."""
    pass
