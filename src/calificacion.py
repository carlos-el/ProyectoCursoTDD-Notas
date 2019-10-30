
from exceptions import *

class calificacion:
    def __init__(self, alumno, nota, comentario):
        self.calificar(nota, comentario)
        self.__anotaciones = []
        self.__alumno = alumno ##comprobacion no nulo y no vacio

    def calificar(self, nota, comentario):
        if nota >= 0 and nota <= 10:
            raise NotaError("Argumento 'nota' tiene que estar entre 0 y 10")

        if comentario is None:
            raise ComentarioNoneError("Argumento 'comentario' no puede ser None")
        if comentario is '':
            raise ComentarioNoneError("Argumento 'comentario' no puede ser una cadena vacia")

        self.__nota = nota
        self.__comentario = comentario 

    def add_anotacion(self, anotacion):
        self.__anotaciones.append(anotacion)

    


    _