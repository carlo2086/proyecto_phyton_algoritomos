# from openpyxl import Workbook, load_workbook
import pandas as pd
from openpyxl import Workbook

from alumno import Alumno
from docente import Docente
from curso import Curso
from datetime import datetime

##########################
listado_alumno=[]
listado_docente=[]
listado_curso=[]
registros_alumnos = 'listado_alumnos.xlsx'
#region alumnos

def registrar_alumnos():
    listado_alumno = obtener_alumnos()
    alumno1 = Alumno('nombre1', 'apellido 1', 'apellido 1', 'dni','codigo', 'Informatica y Sistemas', 2023)
    alumno2 = Alumno('nombre2', 'apellido 2', 'apellido 2', 'dni', 'codigo', 'Informatica y Sistemas', 2023)
    alumno3 = Alumno('nombre3', 'apellido 3', 'apellido 3', 'dni', 'codigo', 'Informatica y Sistemas', 2023)
    listado_alumno.append(alumno1)
    listado_alumno.append(alumno2)
    listado_alumno.append(alumno3)
    
    print(f'registro de estudiantes es: {len(listado_alumno)}')

def guardar_alumnos():
    print(f'registro de estudiantes es: {len(listado_alumno)}')
    if len(listado_alumno)>0:
        data =[]
        for alumno in listado_alumno:
            data.append([alumno.nombre, alumno.ap_paterno, alumno.ap_materno, alumno.dni, alumno.codigo, alumno.facultad, alumno.año_ingreso])
        columnas = ['Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'DNI', 'Codigo', 'Facultad', 'Año']
        df = pd.DataFrame(data, columns=columnas)
        # Guardar el DataFrame en un archivo Excel
        df.to_excel(registros_alumnos, index=False, engine='openpyxl')
    else:
        print("no existen registros :(")
def obtener_alumnos():
    df = pd.read_excel(registros_alumnos)
    listado_alumno = []
    for index, row in df.iterrows():
        alumno = Alumno(row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'], row['DNI'], row['Codigo'], row['Facultad'], row['Año'])
        listado_alumno.append(alumno)
    return listado_alumno
    #print(f'registro de estudiantes es: {len(listado_alumno)}')

def editar_alumno():
    df = pd.read_excel(registros_alumnos)
    indice_editar = 0
    print('ingrese el indice a editar: \n')
    indice_editar= int(input('ingrese un indice valor numerico: '))
    if(indice_editar>=0):
        df.loc[indice_editar, 'Nombre'] = input('Ingrese el nuevo nombre: ')
        df.to_excel(registros_alumnos, index=False, engine='openpyxl')
        print('actualización correcta')
    else:
        print('valor erroneo intentelo despues')
#endregion


def registrar_docentes():
    docente1 = Docente('nombre1', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')
    docente2 = Docente('nombre2', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')
    listado_docente.append(docente1)
    listado_docente.append(docente2)
    print("Registro de docentes")

def registrar_cursos():
    curso1 = Curso('codigo 1', 'nombre 1')
    curso2 = Curso('codigo 2', 'nombre 2')
    curso3 = Curso('codigo 3', 'nombre 3')
    curso4 = Curso('codigo 4', 'nombre 4')

    listado_curso.append(curso1)
    listado_curso.append(curso2)
    listado_curso.append(curso3)
    listado_curso.append(curso4)
    print("Registro de cursos")

def asignar_docente_curso():
    if(len(listado_docente)>0):
        if(len(listado_curso)>0):
            band = 0
            for curso in listado_curso:
                if (band < 2):
                    curso.asignar_docente(listado_docente[0])
                else:
                    curso.asignar_docente(listado_docente[1])
                band += 1

        else:
            print("no existe datos de curso para asignar")
    else:
        print("No existe datos de docentes para asignar")



def actualizar_docente_curso():
    print("Actualización de docente en curso")

def registrar_notas_alumno():
    print("Registro de notas de alumno")

def reporte_alumno():
    print("Generando el Reporte de alumno")
    fecha_actual = datetime.now()
    formato = fecha_actual.strftime("%d_%m_%Y")
    print("Fecha actual en formato 'día_mes_año':", formato)
    nom_reporte = 'reporte_'+ formato + '.txt'
    with open(nom_reporte, 'a') as archivo:
       archivo.write("*******Listado de Alumnos registrados en el Sistema*******************.\n")
       for alumno in listado_alumno:
           archivo.write(alumno.imprimir())
           archivo.write("\n ---------------Datos del curso-----------------------------\n")
       #  return f'datos del alumno es : {per_data}, codigo de ingreso {codigo}, {facultad=}, el año de ingreso es: {año}'    
       archivo.write("*************************************************.\n")


def reporte_docente():
    print("Reporte de docente")

def curso_alumno():
    print("agregar curso a alumno")
##diccionario
opciones = {
    "1": registrar_alumnos,
    "2": registrar_docentes,
    "3": registrar_cursos,
    "4": asignar_docente_curso,
    "5": actualizar_docente_curso,
    "6": registrar_notas_alumno,
    "7": reporte_alumno,
    "8": reporte_docente,
    "9": curso_alumno,
    "10": exit,
    "11": guardar_alumnos,
    "12": editar_alumno

}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar alumnos")
    print("2. Registrar docentes")
    print("3. Registrar cursos")
    print("4. Asignar docente curso")
    print("5. Actualizar docente curso")
    print("6. Registrar notas alumno")
    print("7. Reporte de alumno")
    print("8. Reporte de docente")
    print("9. Matricular alumno al curso")
    print("11. Guadar alumno")
    print("12. Editar alumno")
    print("10. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")