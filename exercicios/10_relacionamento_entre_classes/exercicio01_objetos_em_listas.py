class Pessoa:

    def __init__(self, nome):
        self._nome = nome


pessoa1 = Pessoa('Otavio')
pessoa2 = Pessoa('Maria')
pessoa3 = Pessoa('João')

pessoas = []

pessoas.append(pessoa1)
pessoas.append(pessoa2)
pessoas.append(pessoa3)

print(pessoas)