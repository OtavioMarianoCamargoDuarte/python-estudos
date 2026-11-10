class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor


conta1 = ContaBancaria("Otavio", 1000)

conta1.sacar(1500)

print(conta1.saldo)