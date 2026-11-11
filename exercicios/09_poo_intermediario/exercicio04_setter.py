class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):

        if not novo_nome:
            print('Nome inválido.')
            return

        self._nome = novo_nome


pessoa1 = Pessoa('Otavio')

pessoa1.nome = ""

print(pessoa1.nome)