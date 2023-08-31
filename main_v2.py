# from openpyxl import Workbook, load_workbook
import pandas as pd
from openpyxl import Workbook

from alumno_negocio import AlumnoNegocio

##########################
listado_alumno=[]
registros_alumnos = 'listado_alumnos_v2.xlsx'
#region alumnos
negocio = AlumnoNegocio()

def registrar_alumnos():
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    dni = input('Ingrese dni: ')
    codigo = input('Ingrese codigo: ')
    facultad = input('Ingrese facultad: ')
    anio_ingreso = int(input('Ingrese anio_ingreso: '))
    negocio.registrar_alumnos(nombre,ap_paterno, ap_materno,dni, codigo, facultad,anio_ingreso)
    negocio.guardar_alumnos()
    print(f'registro correctamente elestudiantes')

def obtener_alumnos():
    listado_alumno = negocio.obtener_alumnos()
    for alumno in listado_alumno:
        print(alumno.imprimir())

def editar_alumno():
    indice = int(input('Ingrese un valor numerico: '))
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    dni = input('Ingrese dni: ')
    codigo = input('Ingrese codigo: ')
    facultad = input('Ingrese facultad: ')
    anio_ingreso = int(input('Ingrese anio_ingreso: '))
    print(negocio.editar_alumno(indice,nombre,ap_paterno, ap_materno,dni, codigo, facultad,anio_ingreso))
#endregion

##diccionario
opciones = {
    "1": registrar_alumnos,
    "2": obtener_alumnos,
    "3": editar_alumno,
    "4": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar alumnos")
    print("2. Listar alumnos")
    print("3. Editar alumno")
    print("4. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")