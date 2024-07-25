class Animal:

    def comer(self):
        print('El animal está comiendo')
        
class Ave(Animal):
    def volar(self):
        print('El animal está volando')
        
class Mamifero(Animal):
    def amamantar(self):
        print('El animal está amamantando')

class Murcielago(Mamifero,Ave):
    pass

murcielago=Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()

ave=Ave()

ave.comer()
ave.volar()
#ave.amamantar()

print(Murcielago.mro())