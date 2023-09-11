import tkinter as tk
from tkinter import ttk
from negocio.alumno_negocio import AlumnoNegocio


class MainMenuApp:
    #instanciamos la clase de logica para el alumno
    negocio = AlumnoNegocio()
    # obtenemos el listado 
    listado_alumnos =[]
    treeview = []
    detalle_label =[]
    indice_alumno = 0

    def __init__(self, root):
        self.negocio = AlumnoNegocio()
        self.listado_alumnos = self.negocio.obtener_alumnos()
        self.root = root
        self.root.title("Interfaz con Panel de Opciones y Contenido")
        self.root.config(bg='white')
        self.root.geometry('800x650')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Crear el contenedor principal
        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Crear el panel de opciones en el lado izquierdo
        self.options_panel = ttk.Frame(self.container, width=150)
        self.options_panel.pack(side="left", fill="y")

        # Crear el área de contenido en el lado derecho
        self.content_frame = ttk.Frame(self.container)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Crear el menú en el panel de opciones
        self.opciones_menu = tk.Menu(self.root)
        self.root.config(menu=self.opciones_menu)
        self.opciones_menu.add_command(label="Alumnos", command=self.mostrar_contenido_opcion1)
        self.opciones_menu.add_command(label="Docentes", command=self.mostrar_contenido_opcion2)
        self.opciones_menu.add_command(label="Cursos", command=self.mostrar_contenido_opcion2)

        

    def mostrar_contenido_opcion1(self):
        self.limpiar_contenido()
        # Crear un TreeView para mostrar el listado de alumnos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configurar columnas
        self.treeview["columns"] = ("Nombre", "Apellidos","DNI", "Facultad")
        self.treeview.column("#0", width=50)  # Índice
        self.treeview.column("Nombre", width=100)
        self.treeview.column("Apellidos", width=100)
        self.treeview.column("DNI", width=100)
        self.treeview.column("Facultad", width=100)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellidos", text="Apellidos")
        self.treeview.heading("DNI", text="DNI")
        self.treeview.heading("Facultad", text="Facultad")
        # Llenar el TreeView con datos de la lista de alumnos
        for i, alumno in enumerate(self.listado_alumnos):
            self.treeview.insert("", "end", text=i, values=(alumno.nombre, alumno.ap_paterno + ' ' + alumno.ap_materno, alumno.dni, alumno.facultad))
        # Botón para mostrar detalles del alumno seleccionado
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_alumno)
        detalle_button.pack(pady=10)
        nuevo_button = ttk.Button(self.content_frame, text="Nuevo registro", command=self.nuevo_alumno)
        nuevo_button.pack(pady=10)
        editar_button = ttk.Button(self.content_frame, text="Editar registro", command=self.editar_alumno)
        editar_button.pack(pady=10)

        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)
    #funcion para mostrar el detalle de la tabla de los alumnos
    def mostrar_detalle_alumno(self):
        # Etiqueta para mostrar los detalles del alumno seleccionado
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            alumno = self.listado_alumnos[indice]
            self.detalle_label.config(text=f"Nombre: {alumno.nombre}\nApellido: {alumno.ap_paterno} {alumno.ap_materno}\nDNI: {alumno.dni} \n Facultad: {alumno.facultad}")
        else:
            self.detalle_label.config(text="Seleccione un alumno")

    def nuevo_alumno(self):
        self.limpiar_contenido()
         # Etiquetas y campos de entrada
        self.indice_label = ttk.Label(self.content_frame, text="Codigo alumno:")
        self.indice_label.pack()
        self.indice_entry = ttk.Entry(self.content_frame)
        self.indice_entry.pack()

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()

        self.apellido_p_label = ttk.Label(self.content_frame, text="Apellido paterno:")
        self.apellido_p_label.pack()
        self.apellido_p_entry = ttk.Entry(self.content_frame)
        self.apellido_p_entry.pack()

        self.apellido_m_label = ttk.Label(self.content_frame, text="Apellido Materno:")
        self.apellido_m_label.pack()
        self.apellido_m_entry = ttk.Entry(self.content_frame)
        self.apellido_m_entry.pack()

        self.dni_label = ttk.Label(self.content_frame, text="DNI:")
        self.dni_label.pack()
        self.dni_entry = ttk.Entry(self.content_frame)
        self.dni_entry.pack()

        self.codigo_label = ttk.Label(self.content_frame, text="Codigo de estudiante:")
        self.codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.content_frame)
        self.codigo_entry.pack()

        self.carrera_label = ttk.Label(self.content_frame, text="Facultad:")
        self.carrera_label.pack()
        self.carrera_entry = ttk.Entry(self.content_frame)
        self.carrera_entry.pack()

        self.anio_label = ttk.Label(self.content_frame, text="Año de ingreso:")
        self.anio_label.pack()
        self.anio_entry = ttk.Entry(self.content_frame)
        self.anio_entry.pack()

        self.editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_alumnos)
        self.editar_button.pack()

        self.salir_button = ttk.Button(self.content_frame, text="Cancelar")
        self.salir_button.pack()
    
    def editar_alumno(self):
        # Etiqueta para mostrar los detalles del alumno seleccionado
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_alumno = int(self.treeview.item(seleccionado)['text'])
            self.editar_alumno_fr()
        else:
            self.detalle_label.config(text="Seleccione un alumno")


    def editar_alumno_fr(self):
            self.limpiar_contenido()
            alumno = self.listado_alumnos[self.indice_alumno]
            self.indice_label = ttk.Label(self.content_frame, text="Codigo alumno:")
            self.indice_label.pack()
            self.indice_entry = ttk.Entry(self.content_frame)
            self.indice_entry.pack()
            self.indice_entry.insert(0, self.indice_alumno)

            self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
            self.nombre_label.pack()
            self.nombre_entry = ttk.Entry(self.content_frame)
            self.nombre_entry.pack()
            self.nombre_entry.insert(0, alumno.nombre)

            self.apellido_p_label = ttk.Label(self.content_frame, text="Apellido paterno:")
            self.apellido_p_label.pack()
            self.apellido_p_entry = ttk.Entry(self.content_frame)
            self.apellido_p_entry.pack()
            self.apellido_p_entry.insert(0, alumno.ap_paterno)

            self.apellido_m_label = ttk.Label(self.content_frame, text="Apellido Materno:")
            self.apellido_m_label.pack()
            self.apellido_m_entry = ttk.Entry(self.content_frame)
            self.apellido_m_entry.pack()
            self.apellido_m_entry.insert(0, alumno.ap_materno)

            self.dni_label = ttk.Label(self.content_frame, text="DNI:")
            self.dni_label.pack()
            self.dni_entry = ttk.Entry(self.content_frame)
            self.dni_entry.pack()
            self.dni_entry.insert(0, alumno.dni)

            self.codigo_label = ttk.Label(self.content_frame, text="Codigo de estudiante:")
            self.codigo_label.pack()
            self.codigo_entry = ttk.Entry(self.content_frame)
            self.codigo_entry.pack()
            self.codigo_entry.insert(0, alumno.codigo)

            self.carrera_label = ttk.Label(self.content_frame, text="Facultad:")
            self.carrera_label.pack()
            self.carrera_entry = ttk.Entry(self.content_frame)
            self.carrera_entry.pack()
            self.carrera_entry.insert(0, alumno.facultad)

            self.anio_label = ttk.Label(self.content_frame, text="Año de ingreso:")
            self.anio_label.pack()
            self.anio_entry = ttk.Entry(self.content_frame)
            self.anio_entry.pack()
            self.anio_entry.insert(0, alumno.año_ingreso)

            self.editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_alumnos)
            self.editar_button.pack()

            self.salir_button = ttk.Button(self.content_frame, text="Cancelar")
            self.salir_button.pack()
       
    def guardar_alumnos(self):
            indice = int(self.indice_entry.get())
            nombre = self.nombre_entry.get()
            apellido_paterno = self.apellido_p_entry.get()
            apellido_materno = self.apellido_m_entry.get()
            dni = self.dni_entry.get()
            codigo = self.codigo_entry.get()
            facultad = self.carrera_entry.get()
            anio = int(self.anio_entry.get())
            print(f'año es : {anio}')
            
            reg = self.negocio.registrar_alumnos(nombre, apellido_paterno, apellido_materno, dni, codigo, facultad, anio)
            reg = self.negocio.guardar_alumnos()
            print(f"guardado en el excel {reg}")
            self.listado_alumnos = self.negocio.obtener_alumnos()
            self.mostrar_contenido_opcion1()

    def editar_alumnos(self):
            indice = int(self.indice_entry.get())
            nombre = self.nombre_entry.get()
            apellido_paterno = self.apellido_p_entry.get()
            apellido_materno = self.apellido_m_entry.get()
            dni = self.dni_entry.get()
            codigo = self.codigo_entry.get()
            facultad = self.carrera_entry.get()
            anio = int(self.anio_entry.get())
            print(f'{nombre}, {apellido_paterno}, {apellido_materno}, {dni}, {facultad}, {anio}')
            
            reg = self.negocio.editar_alumno(indice, nombre, apellido_paterno, apellido_materno, dni, codigo, facultad, anio)
            print(f"editado en el excel {reg}")
            self.listado_alumnos = self.negocio.obtener_alumnos()
            self.mostrar_contenido_opcion1()

    def mostrar_contenido_opcion2(self):
        self.limpiar_contenido()
        label = ttk.Label(self.content_frame, text="Contenido de Opción 2")
        label.pack(padx=20, pady=20)

    def limpiar_contenido(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

# Crear la ventana principal
root = tk.Tk()
app = MainMenuApp(root)
root.mainloop()
