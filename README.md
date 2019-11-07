# Gestor de notas

[![Build Status](https://travis-ci.com/carlos-el/ProyectoCursoTDD-Notas.svg?branch=master)](https://travis-ci.com/carlos-el/ProyectoCursoTDD-Notas)
[![Code coverage](https://codecov.io/gh/carlos-el/ProyectoCursoTDD-Notas/branch/master/graphs/badge.svg)](https://codecov.io/gh/carlos-el/ProyectoCursoTDD-Notas/branch/master)

Proyecto realizado por:

- Carlos Enriquez Lopez
- Víctor Vázquez Rodríguez

***Nota:** este proyecto es desarrollado como parte del [seminario sobre TDD](https://github.com/JJ/curso-tdd) impartido en la UGR en el curso 19/20.*

El microservicio desarrollado en este proyecto permitirá la gestión de las notas en las prácticas de las asignaturas. Las historias de usuario obtenidas son las siguientes:

- [[HU0] Añadir una asignatura](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/1)
- [[HU1] Añadir una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/4)
- [[HU2] Añadir una calificación](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/6)
- [[HU3] Obtener descripción de una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/2)
- [[HU4] Obtener calificación de una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/3)
- [[HU5] Obtener estadísticas de una asignatura](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/5)
- [[HU6] Recalificar práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/7)
- [[HU7] Obtener estadísticas de una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/8)
- [[HU8] Obtener calificación de una asignatura](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/9)

La implementación de este microservicio se va a realizar usando Python y el *framework* [Flask](https://palletsprojects.com/p/flask/). Para el almacenamiento persistente de datos usaremos [PostgreSQL](https://www.postgresql.org/) y para la configuración remota [etcd](https://etcd.io/).
