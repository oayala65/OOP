class Celular():
    def __init__(self,marca,modelo,camara):
        self.marca = marca # Corregido el nombre de la marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Estas haciendo una llamada desde un: {self.modelo}")

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular("Samsung","S23","48MP")  # Corregido el nombre de la clase
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

celular2.llamar()