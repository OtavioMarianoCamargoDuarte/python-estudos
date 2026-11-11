class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome


pessoa1 = Pessoa("Otavio")

print(pessoa1.nome)