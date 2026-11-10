class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


conta1 = ContaBancaria("Otavio", 1000)

print(conta1.titular)
print(conta1.saldo)