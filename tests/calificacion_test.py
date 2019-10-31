import sys, os, pytest

sys.path.append(os.path.abspath('./src'))

from calificacion.definition import Calificacion
from calificacion.exceptions import *

def test_alumno_none():
    with pytest.raises(AlumnoNoneException):
        _ = Calificacion(None, 6, "Comentario de prueba")

def test_alumno_empty():
    with pytest.raises(AlumnoEmptyException):
        _ = Calificacion("", 6, "Comentario de prueba")

def test_nota_correcta():
    _ = Calificacion("Alumno", 6, "Comentario de prueba")

def test_nota_negativa():
    with pytest.raises(NotaException):
        _ = Calificacion("Alumno", -3, "Comentario de prueba")

def test_comentario_none():
    with pytest.raises(ComentarioNoneException):
        _ = Calificacion("Alumno", 6, None)

def test_comentario_empty():
    with pytest.raises(ComentarioEmptyException):
        _ = Calificacion("Alumno", 6, "")
