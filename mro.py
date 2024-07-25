# Metodo Resolución de Order

class A:
    def hablar(self):
        print('Hola desde A')

class B:
    def hablar(self):
        print('Hola desde B')

class C:
    def hablar(self):
        print('Hola desde C')

class D(C,B):
   def hablar(self):
      print('Hola desde D(B,C)')

d=D()

d.hablar()

B.hablar(d) # llamo desde B
C.hablar(d)  # llamo desde C
print(D.mro())