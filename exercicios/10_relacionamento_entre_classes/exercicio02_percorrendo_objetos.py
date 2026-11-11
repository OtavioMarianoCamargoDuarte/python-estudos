class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


pessoa1 = Pessoa("Otavio")
pessoa2 = Pessoa("Maria")
pessoa3 = Pessoa("João")

pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in pessoas:
    print(pessoa.nome)