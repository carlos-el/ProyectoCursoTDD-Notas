from calificacion.definition import Calificacion
from excepciones.exceptions import *

class Practica:
    def __init__(self, id, nombre, descripcion):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__calificaciones = []

    def get_calificaciones(self):
        return self.__calificaciones

    def get_calificacion(self, alumno):
        if not isinstance(alumno, str):
            raise AttributeError("No es un string")

        for c in self.__calificaciones:
            if c.get_alumno() == alumno:
                return c
        
        raise ItemNotFound("No hay una calificación para el alumno")

    def calificar(self, alumno, nota, comentario):
        if not isinstance(alumno, str):
            raise AttributeError("No es un string")

        for c in self.__calificaciones:
            if c.get_alumno == alumno:
                c.calificar(nota, comentario)
                return

        c = Calificacion(alumno, nota, comentario)
        self.__calificaciones.append(c)

    def add_anotacion(self, alumno, anotacion):
        if not isinstance(alumno, str):
            raise AttributeError("No es un string")

        for c in self.__calificaciones:
            if c.get_alumno() == alumno:
                c.add_anotacion(anotacion)
                return

        raise ItemNotFound("No hay una calificación para el alumno")