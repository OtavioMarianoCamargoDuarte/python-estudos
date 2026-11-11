class Pessoa:

    def __init__(self, nome):
        self.nome = nome


class Conta:

    def __init__(self, descricao):
        self.descricao = descricao
        self.participantes = []


pessoa1 = Pessoa('Otavio')
pessoa2 = Pessoa('Maria')

conta = Conta('Pizza')

conta.participantes.append(pessoa1)
conta.participantes.append(pessoa2)

print(conta.descricao)

for participante in conta.participantes:
    print(participante.nome)