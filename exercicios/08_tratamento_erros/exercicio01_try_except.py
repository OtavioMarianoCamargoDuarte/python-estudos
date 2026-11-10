class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= valor


conta1 = ContaBancaria("Otavio", 1000)

try:
    conta1.sacar(1500)

except ValueError as erro:
    print(f'Erro encontrado: {erro}')

print('Programa finalizado.')