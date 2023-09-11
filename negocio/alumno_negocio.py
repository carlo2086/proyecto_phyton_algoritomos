import pandas as pd
from openpyxl import Workbook
from modelo.alumno import Alumno
from datetime import datetime

class AlumnoNegocio():
    listado_alumno=[]
    registros_alumnos = 'listado_alumnos_v2.xlsx'

    def __init__(self):
        self.listado_alumno=[]
        #self.registros_alumnos = 'listado_alumnos.xlsx'

    def obtener_alumnos(self):
        listado_alumno = []
        try:
            df = pd.read_excel(self.registros_alumnos)
           
            for index, row in df.iterrows():
                alumno = Alumno(row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'], row['DNI'], row['Codigo'], row['Facultad'], row['Año'])
                listado_alumno.append(alumno)

        except FileNotFoundError:
            print('No existe el archivo')
        return listado_alumno

        #print(f'registro de estudiantes es: {len(listado_alumno)}')

    def registrar_alumnos(self,_nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad, _anio):
        print(f'{_nombre}, {_apellido_paterno}, {_apellido_materno}, {_dni}, {_codigo}, {_facultad}, {_anio}')
        self.listado_alumno = self.obtener_alumnos()
        alumno = Alumno(_nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad, _anio)
        self.listado_alumno.append(alumno)
        
        print(f'se agrego un alumno : {len(self.listado_alumno)}')

    def guardar_alumnos(self):
        print(f'listado de alumnos es: {len(self.listado_alumno)}')
        if len(self.listado_alumno) > 0:
            data =[]
            for alumno in self.listado_alumno:
                data.append([alumno.nombre, alumno.ap_paterno, alumno.ap_materno, alumno.dni, alumno.codigo, alumno.facultad, alumno.año_ingreso])
            columnas = ['Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'DNI', 'Codigo', 'Facultad', 'Año']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_alumnos, index=False, engine='openpyxl')
            return f'se registro correctamento los datos del alumno'
        else:
            return f'se genero un erro al registrar el alumno'
        

    def editar_alumno(self,_indice, _nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad, _anio_ingreso):
        df = pd.read_excel(self.registros_alumnos)
        df.loc[_indice, 'Nombre'] = _nombre
        df.loc[_indice, 'Apellido_Paterno'] = _apellido_paterno
        df.loc[_indice, 'Apellido_Materno'] = _apellido_materno
        df.loc[_indice, 'DNI'] = _dni
        df.loc[_indice, 'Codigo'] = _codigo
        df.loc[_indice, 'Facultad'] = _facultad
        df.loc[_indice, 'Año'] = _anio_ingreso
        df.to_excel(self.registros_alumnos, index=False, engine='openpyxl')
        return f'actualización correcta'