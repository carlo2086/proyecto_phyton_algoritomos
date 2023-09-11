import tkinter as tk
from tkinter import ttk
from negocio.alumno_negocio import AlumnoNegocio

#instanciamos la clase de logica para el alumno
negocio = AlumnoNegocio()
# obtenemos el listado 
listado_alumnos = negocio.obtener_alumnos()

#funcion para mostrar el detalle de la tabla de los alumnos
def mostrar_detalle_alumno():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(treeview.item(seleccionado)['text'])
        alumno = listado_alumnos[indice]
        detalle_label.config(text=f"Nombre: {alumno.nombre}\nApellido: {alumno.ap_paterno} {alumno.ap_materno}\nDNI: {alumno.dni} \n Facultad: {alumno.facultad}")
    else:
        detalle_label.config(text="Seleccione un alumno")

# Crear la interfaz principal
root = tk.Tk()
root.title("Listado de Alumnos")
root.geometry("540x450")

# Crear un TreeView para mostrar el listado de alumnos
treeview = ttk.Treeview(root)
treeview.pack()

# Configurar columnas
treeview["columns"] = ("Nombre", "Apellidos","DNI", "Facultad")
treeview.column("#0", width=50)  # Índice
treeview.column("Nombre", width=100)
treeview.column("Apellidos", width=100)
treeview.column("DNI", width=100)
treeview.column("Facultad", width=100)

treeview.heading("#0", text="Índice")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Apellidos", text="Apellidos")
treeview.heading("DNI", text="DNI")
treeview.heading("Facultad", text="Facultad")

# Llenar el TreeView con datos de la lista de alumnos
for i, alumno in enumerate(listado_alumnos):
    treeview.insert("", "end", text=i, values=(alumno.nombre, alumno.ap_paterno + ' ' + alumno.ap_materno, alumno.dni, alumno.facultad))
# Botón para mostrar detalles del alumno seleccionado
detalle_button = ttk.Button(root, text="Mostrar Detalle", command=mostrar_detalle_alumno)
detalle_button.pack(pady=10)

# Etiqueta para mostrar los detalles del alumno seleccionado
detalle_label = ttk.Label(root, text="")
detalle_label.pack()

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
opciones_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opciones", menu=opciones_menu)
# Crear instancias de las clases de interfaz

opciones_menu.add_command(label="Alumnos")


root.mainloop()