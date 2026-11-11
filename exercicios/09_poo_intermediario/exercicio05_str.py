class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Pessoa: {self._nome}'


pessoa1 = Pessoa('Otavio')

print(pessoa1)