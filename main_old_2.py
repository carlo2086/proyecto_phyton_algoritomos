lista_alumnos = []
# incluir los 5 registros por integrante
alumno1 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni',
                 'codigo', 'Informatica y Sistemas', 2023)
alumno2 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni',
                 'codigo', 'Informatica y Sistemas', 2023)
alumno3 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni',
                 'codigo', 'Informatica y Sistemas', 2023)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)

lista_docente = []
docente1 = Docente('nombre1', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')
docente2 = Docente('nombre2', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')

lista_docente.append(docente1)
lista_docente.append(docente2)

lista_curso = []
curso1 = Curso('codigo 1', 'nombre 1')
curso2 = Curso('codigo 2', 'nombre 2')
curso3 = Curso('codigo 3', 'nombre 3')
curso4 = Curso('codigo 4', 'nombre 4')

lista_curso.append(curso1)
lista_curso.append(curso2)
lista_curso.append(curso3)
lista_curso.append(curso4)


band = 0
for curso in lista_curso:
    if (band < 2):
        curso.asignar_docente(docente1)
    else:
        curso.asignar_docente(docente2)
    band += 1

for curso in lista_curso:
    docente = curso.mostrar_docente()
    print(docente.imprimir())


#for alumno in lista_alumnos:
#    for curso in lista_curso:
#        alumno.agregar_curso(curso)

for curso in lista_curso:
    lista_alumnos[1].agregar_curso(curso)
#mostrar los cursos asignados a alumno 

for curso_asignado in lista_alumnos[1].Curso:
    print(curso_asignado.mostrar_curso())

#ingresar notas al alumno
# Ingresar notas y calcular promedio para un alumno
for alumno in lista_alumnos:
    print(f"Ingresar notas para {alumno.get_nombre()}:")
    for curso in alumno.Curso:
        while True:
            try:
                nota = float(input(f"Ingrese nota para el curso {curso.get_nombre()}: "))
                curso.ingresar_notas(nota)
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

    ##promedio = curso.calcularPromedio(curso.notas)
    ##print(f"Promedio de notas para {alumno.get_nombre()}: {promedio:.2f}")


#calcular el promedio

for alumno in lista_alumnos:
    for curso in alumno.Curso:
        print(curso.reporte())

