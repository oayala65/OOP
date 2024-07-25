class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
   
    def hablar(self):
        print('Estoy habalando por telefono')

    def imprimir(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}')


class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

    def imprimir(self):
        super().imprimir()
        print(f'Trabajo: {self.trabajo}, Salario: {self.salario}')

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas=notas
        self.universidad=universidad
    
    def imprimir(self):
        super().imprimir()
        print(f'Notas: {self.notas}, Universidad: {self.universidad}')


# Crear instancias
persona = Persona('Juan', 30, 'argentino')
empleado = Empleado('Ana', 25, 'mexicana', 'ingeniera', 50000)
estudiante = Estudiante('Roberto', 43, 'argentino', 'SIETE', 'UFGRS')

# Imprimir atributos
print("Atributos de Persona:")
persona.imprimir()
print("\nAtributos de Empleado:")
empleado.imprimir()
print("\nAtributos de Estudiante:")
estudiante.imprimir()

estudiante.hablar()

