import pandas as pd
import tkinter as tk
from tkinter import ttk
from alumno_negocio import AlumnoNegocio



#region interface
root = tk.Tk()
root.title("Registro de Alumno")
root.geometry("400x550")

negocio = AlumnoNegocio()

status_label = ttk.Label(root, text="")
status_label.config(text=f"Registro en el índice {1} editado y guardado.")

def limpiar_controles():
    indice_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    apellido_p_entry.delete(0, tk.END)
    apellido_m_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_entry.delete(0, tk.END)
    anio_entry.delete(0, tk.END)
    codigo_entry.delete(0, tk.END)

def guardar_alumnos():
    indice = int(indice_entry.get())
    nombre = nombre_entry.get()
    apellido_paterno = apellido_p_entry.get()
    apellido_materno = apellido_m_entry.get()
    dni = dni_entry.get()
    codigo = codigo_entry.get()
    facultad = carrera_entry.get()
    anio = int(anio_entry.get())
    print(f'{nombre}, {apellido_paterno}, {apellido_materno}, {dni}, {facultad}, {anio}')
    
    reg = negocio.registrar_alumnos(nombre, apellido_paterno, apellido_materno, dni, codigo, facultad, anio)
    reg = negocio.guardar_alumnos()
    print(f"guardado en el excel {reg}")
    limpiar_controles()

def salir():
    root.quit()

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

status_label.pack()

root.mainloop()
#endregion