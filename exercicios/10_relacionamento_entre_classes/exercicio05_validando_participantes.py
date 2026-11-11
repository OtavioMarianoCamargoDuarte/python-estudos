class Pessoa:

    def __init__(self, nome):
        self.nome = nome


class Conta:

    def __init__(self, descricao):
        self.descricao = descricao
        self.participantes = []

    def adicionar_participantes(self, pessoa):

        if pessoa in self.participantes:
            print('Participante já cadastrado.')
            return

        self.participantes.append(pessoa)


pessoa1 = Pessoa('Otavio')

conta = Conta('Pizza')

conta.adicionar_participantes(pessoa1)
conta.adicionar_participantes(pessoa1)

for participante in conta.participantes:
    print(participante.nome)