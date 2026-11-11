class Pessoa:

    def __init__(self, nome):
        self.nome = nome


pessoa1 = Pessoa("Otavio")

print(pessoa1.nome)

pessoa1.nome = ''

print(pessoa1.nome)