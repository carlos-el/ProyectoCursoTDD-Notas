
from exceptions import NotaError

class calificacion:
    def __init__(self, alumno, nota, comentario):
        self.calificar(nota, comentario)
        self.__anotaciones = []
        self.__alumno = alumno ##comprobacion no nulo y no vacio

    def calificar(self, nota, comentario):
        if nota not in [0, 10]:
            raise NotaError(nota, "Nota no esta entre 0 y 10")

        self.__nota = nota
        self.__comentario = comentario ##comprobacion no nulo y no vacio

    def add_anotacion(self, anotacion):
        self.__anotaciones.append(anotacion)

    


    _