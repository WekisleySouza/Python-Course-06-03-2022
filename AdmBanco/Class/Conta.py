from abc import abstractclassmethod

class Conta:
    def __init__ (self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.__numero_da_conta = numero_da_conta
        self.saldo = saldo

    @property
    def numero_da_conta(self):
        return self.__numero_da_conta

    def deposito(self, valor):
        self.saldo += valor

    @abstractclassmethod
    def sacar():
        pass