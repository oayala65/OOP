class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self):
        print('Estudiando a full')

nombre=input('digame su nombre: ')
edad=input('Ahora su edad: ')
grado=input('Por último, su grado: ')

estudiante=Estudiante(nombre,edad,grado)

print(f'''
      DATOS DEL ESTUDIANTE \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      ''')

while True:
    estudiar=input('Que estás haciendo?  ')
    if estudiar.lower()=='estudiar':
        estudiante.estudiar()
        break