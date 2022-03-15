from Class.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.__conta = conta

    @property
    def conta(self):
        return self.__conta