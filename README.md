# Gestor de notas

Proyecto realizado por:

- Carlos Enriquez Lopez
- Víctor Vázquez Rodríguez

***Nota:** este proyecto es desarrollado como parte del [seminario sobre TDD](https://github.com/JJ/curso-tdd) impartido en la UGR en el curso 19/20.*

El microservicio desarrollado en este proyecto permitirá la gestión de las notas en las prácticas de las asignaturas. Las historias de usuario obtenidas son las siguientes:

- [[H0] Añadir una asignatura](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/1)
- [[H1] Añadir una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/4)
- [[H2] Añadir una calificación](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/6)
- [[H3] Obtener los datos de una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/2)
- [[H4] Obtener calificación de una práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/3)
- [[H5] Obtener datos de una asignatura](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/5)
- [[H6] Recalificar práctica](https://github.com/carlos-el/ProyectoCursoTDD-Notas/issues/7)

La implementación de este microservicio se va a realizar usando Python y el *framework* [Flask](https://palletsprojects.com/p/flask/). Para el almacenamiento persistente de datos usaremos [PostgreSQL](https://www.postgresql.org/) y para la configuración remota [etcd](https://etcd.io/).
