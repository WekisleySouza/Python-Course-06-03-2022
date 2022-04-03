from Class.Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        Conta.__init__(self, agencia, numero_da_conta, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
            