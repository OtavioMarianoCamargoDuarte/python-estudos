class Pessoa:

    def __init__(self, nome):
        self._nome = nome

pessoa1 = Pessoa("Otavio")

print(pessoa1._nome)