import pandas as pd
import tkinter as tk
from tkinter import ttk
from negocio.alumno_negocio import AlumnoNegocio

class InterfaceRegistroAlumno:
    root = tk.Tk()
    negocio = AlumnoNegocio()
    root.title("Registro de Alumno")
    root.geometry("400x550")
    
    def __init__(self):
        #root = tk.Tk()
        self.root.title("Registro de Alumno")
        self.root.geometry("400x550")

    def limpiar_controles(self):
        self.indice_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido_p_entry.delete(0, tk.END)
        self.apellido_m_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.carrera_entry.delete(0, tk.END)
        self.anio_entry.delete(0, tk.END)
        self.codigo_entry.delete(0, tk.END)

    def guardar_alumnos(self):
        indice = int(self.indice_entry.get())
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_p_entry.get()
        apellido_materno = self.apellido_m_entry.get()
        dni = self.dni_entry.get()
        codigo = self.codigo_entry.get()
        facultad = self.carrera_entry.get()
        anio = int(self.anio_entry.get())
        print(f'{nombre}, {apellido_paterno}, {apellido_materno}, {dni}, {facultad}, {anio}')
        
        reg = self.negocio.registrar_alumnos(nombre, apellido_paterno, apellido_materno, dni, codigo, facultad, anio)
        reg = self.negocio.guardar_alumnos()
        print(f"guardado en el excel {reg}")
        self.limpiar_controles()

    def salir(self):
        self.root.quit()

    # Etiquetas y campos de entrada
    indice_label = ttk.Label(root, text="Codigo alumno:")
    indice_label.pack()
    indice_entry = ttk.Entry(root)
    indice_entry.pack()

    nombre_label = ttk.Label(root, text="Nombre:")
    nombre_label.pack()
    nombre_entry = ttk.Entry(root)
    nombre_entry.pack()

    apellido_p_label = ttk.Label(root, text="Apellido paterno:")
    apellido_p_label.pack()
    apellido_p_entry = ttk.Entry(root)
    apellido_p_entry.pack()

    apellido_m_label = ttk.Label(root, text="Apellido Materno:")
    apellido_m_label.pack()
    apellido_m_entry = ttk.Entry(root)
    apellido_m_entry.pack()

    dni_label = ttk.Label(root, text="DNI:")
    dni_label.pack()
    dni_entry = ttk.Entry(root)
    dni_entry.pack()

    codigo_label = ttk.Label(root, text="Codigo de estudiante:")
    codigo_label.pack()
    codigo_entry = ttk.Entry(root)
    codigo_entry.pack()

    carrera_label = ttk.Label(root, text="Facultad:")
    carrera_label.pack()
    carrera_entry = ttk.Entry(root)
    carrera_entry.pack()

    anio_label = ttk.Label(root, text="Año de ingreso:")
    anio_label.pack()
    anio_entry = ttk.Entry(root)
    anio_entry.pack()

    editar_button = ttk.Button(root, text="Guardar", command=guardar_alumnos)
    editar_button.pack()

    salir_button = ttk.Button(root, text="Cancelar", command=salir)
    salir_button.pack()

    root.mainloop()
    
   