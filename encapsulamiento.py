class MiClase:
    def __init__(self):
        self._atributo_privado='Valor'

    def _hablar(self):  # ESTE DEJA EJECUTAR. ES SEMI PRIVADO.
        return ('Semi Privado')

    def __hablar(self):         # ESTE NO DEJA EJECUTAR. ES PRIVADO
        print('Semi Privado')

objeto=MiClase()

print(objeto._hablar())