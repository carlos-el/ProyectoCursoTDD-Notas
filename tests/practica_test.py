import sys, os, pytest

sys.path.append(os.path.abspath('./src'))

from practica.definition import Practica
from calificacion.definition import Calificacion
from excepciones.exceptions import *

def test_calificar():
    # setup
    p = Practica(1, "p1", "test p1")
    nota = 10
    alumno = "pepe test"
    comentario = "genial test"

    # exercise
    p.calificar(alumno, nota, comentario)

    # verify
    c = p.get_calificacion(alumno)
    assert c.get_alumno() == alumno,"Error con alumno en calificar"
    assert c.get_nota() == nota,"Error con nota en calificar"
    assert c.get_comentario() == comentario,"Error con comentario en calificar"

def test_re_calificar():
    # setup
    p = Practica(1, "p1", "test p1")
    nota = 10
    alumno = "pepe test"
    comentario = "genial test"

    # exercise
    p.calificar("test", 1, "test")
    p.calificar(alumno, nota, comentario)

    # verify
    c = p.get_calificacion(alumno)
    assert c.get_alumno() == alumno,"Error con alumno en calificar"
    assert c.get_nota() == nota,"Error con nota en calificar"
    assert c.get_comentario() == comentario,"Error con comentario en calificar" 

def test_add_anotacion():
    # setup
    p = Practica(1, "p1", "test p1")
    alumno = "pepe test"
    nota = 10
    comentario = "genial test"
    anotacion1 = "uno test"
    anotacion2 = "dos test"

    # exercise
    p.calificar(alumno, nota, comentario)
    p.add_anotacion(alumno, anotacion1)
    p.add_anotacion(alumno, anotacion2)

    # verify 
    c = p.get_calificacion(alumno)
    assert anotacion1 in c.get_anotaciones(),"Error al anadir anotacion1"
    assert anotacion2 in c.get_anotaciones(),"Error al anadir anotacion2"

def test_alumno_not_found():
    # setup
    p = Practica(1, "p1", "test p1")
    alumno = "pepe test"
    nota = 10
    comentario = "genial test"
    anotacion1 = "uno test"

    # verify 
    with pytest.raises(ItemNotFound):
        p.add_anotacion(alumno, anotacion1)

    with pytest.raises(ItemNotFound):
        p.get_calificacion(alumno)