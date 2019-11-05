import sys, os, pytest

sys.path.append(os.path.abspath('./src'))

from calificacion.definition import Calificacion

def test_alumno_none():
    with pytest.raises(AttributeError):
        _ = Calificacion(None, 6, "Comentario de prueba")

def test_alumno_empty():
    with pytest.raises(ValueError):
        _ = Calificacion("", 6, "Comentario de prueba")

def test_nota_correcta():
    _ = Calificacion("Alumno", 6, "Comentario de prueba")

def test_nota_negativa():
    with pytest.raises(ValueError):
        _ = Calificacion("Alumno", -3, "Comentario de prueba")

def test_comentario_none():
    with pytest.raises(AttributeError):
        _ = Calificacion("Alumno", 6, None)

def test_comentario_empty():
    with pytest.raises(ValueError):
        _ = Calificacion("Alumno", 6, "")

def test_anotacion_none():
    with pytest.raises(AttributeError):
        _ = Calificacion("Alumno", 6, "Comentario de prueba").add_anotacion(None)

def test_anotacion_empty():
    with pytest.raises(ValueError):
        _ = Calificacion("Alumno", 6, "Comentario de prueba").add_anotacion('')
