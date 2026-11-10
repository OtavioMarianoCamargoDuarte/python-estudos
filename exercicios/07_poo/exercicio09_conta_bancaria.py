class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'Saldo atual: R$ {self.saldo}')


conta1 = ContaBancaria("Otavio", 1000)

conta1.mostrar_saldo()