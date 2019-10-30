import pytest

from src.calificacion.definition import Calificacion
from src.calificacion.exceptions import *

class TestCalificacion:
    
    def nota_correcta(self):
        _ = Calificacion("Alumno", 6, "Comentario de prueba")

    def nota_negativa(self):
        with pytest.raises(NotaException):
            _ = Calificacion("Alumno", -3, "Comentario de prueba")

    def alumno_none(self):
        with pytest.raises(AlumnoNoneException):
            _ = Calificacion(None, 6, "Comentario de prueba")

    def alumno_empty(self):
        with pytest.raises(AlumnoEmptyException):
            _ = Calificacion("", 6, "Comentario de prueba")

    def comentario_none(self):
        with pytest.raises(ComentarioNoneException):
            _ = Calificacion("Alumno", 6, None)

    def comentario_empty(self):
        with pytest.raises(ComentarioEmptyException):
            _ = Calificacion("Alumno", 6, "")