class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, edad:{self.edad}')


class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad) # NO SE USA LA FUNCION self CON super().
        self.grado=grado

    def mostrar_grado(self):
        print(f'Grado: {self.grado}')


estudiante=Estudiante('Juancho',19,'10mo')

estudiante.mostrar_datos()
estudiante.mostrar_grado()


