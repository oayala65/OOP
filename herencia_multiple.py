class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
   
    def hablar(self):
        print('Estoy habalando por telefono')

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa
    
    def presentarse(self):
       print(f'Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')
    
# Crear instancias

roberto=EmpleadoArtista('Roberto',43,'argentino','Cantar',100.000,'Yahoo')

roberto.presentarse()

