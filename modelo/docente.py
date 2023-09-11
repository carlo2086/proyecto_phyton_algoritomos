from modelo.persona import Persona

class Docente(Persona):
    codigo_docente = ''
    facultad = ''
    
    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo_docente = codigo
        self.facultad = facultad

    def get_codigo(self):
        return self.codigo_docente

    def set_codigo(self, codigo):
        self.codigo_docente = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo_docente
        facultad = self.facultad
        return f'datos del docente es : {per_data}, codigo de ingreso {codigo}, {facultad=}'
    
