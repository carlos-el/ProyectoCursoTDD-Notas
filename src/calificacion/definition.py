class Calificacion:
    def __init__(self, alumno, nota, comentario):
        self.calificar(nota, comentario)
        self.__anotaciones = []

        if alumno is None:
            raise AttributeError("Argumento 'alumno' no puede ser None")
        if not alumno:
            raise ValueError("Argumento 'alumno' no puede ser una cadena vacía")

        self.__alumno = alumno

    def calificar(self, nota, comentario):
        if nota < 0 or nota > 10:
            raise ValueError("Argumento 'nota' tiene que estar entre 0 y 10")

        if comentario is None:
            raise AttributeError("Argumento 'comentario' no puede ser None")
        if not comentario:
            raise ValueError("Argumento 'comentario' no puede ser una cadena vacia")

        self.__nota = nota
        self.__comentario = comentario

    def add_anotacion(self, anotacion):
        if anotacion is None:
            raise AttributeError("Argumento 'anotacion' no puede ser None")
        if anotacion is '':
            raise ValueError("Argumento 'anotacion' no puede ser una cadena vacia")

        self.__anotaciones.append(anotacion)

    def get_alumno(self):
        return self.__alumno

    def get_nota(self):
        return self.__nota

    def get_comentario(self):
        return self.__comentario

    def get_anotaciones(self):
        return self.__anotaciones
