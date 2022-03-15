from Class.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite):
        Conta.__init__(self, agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
            