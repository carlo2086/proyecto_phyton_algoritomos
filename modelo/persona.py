class Persona:
    id = 0
    nombre = ""
    ap_paterno = ""
    ap_materno = ""
    dni = ""
    fecha_nac = ""

    # constructo
    def __init__(self, nombre, ap_paterno, ap_materno, dni):
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ap_paterno(self):
        return self.ap_paterno

    def set_ap_paterno(self, ap_paterno):
        self.ap_paterno = ap_paterno

    def get_ap_materno(self):
        return self.ap_materno

    def set_ap_materno(self, ap_materno):
        self.ap_materno = ap_materno

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_fecha_nac(self):
        return self.fecha_nac

    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def imprimir(self):
        nombres = self.nombre
        apellidos = self.ap_paterno + ' ' + self.ap_materno
        dni = self.dni
        return f' {nombres=},  {apellidos=}, {dni=}'
