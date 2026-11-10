class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}')


pessoa1 = Pessoa('Otavio')
pessoa2 = Pessoa('Maria')

pessoa1.apresentar()
pessoa2.apresentar()