class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor


conta1 = ContaBancaria("Otavio", 1000)

conta1.depositar(500)

print(conta1.saldo)
