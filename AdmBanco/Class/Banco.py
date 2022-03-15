from Class.Cliente import Cliente
from Class.ContaCorrente import ContaCorrente
from Class.ContaPoupanca import ContaPoupanca


class Banco:
    """Checar se agencia é do banco
    Checar se cliente é do banco
    Checar se conta é do banco"""
    def __init__(self):
        self.__agencias = (23, 11, 21)
        self.__clientes = list()
        self.__numero_da_conta = 10000000

    @property
    def Banco(self):
        return self.__clientes
            
    def verificar_agencia(self, agencia):
        if agencia in self.__agencias:
            return True
        else:
            return False

    def verificar_conta(self, conta, retornar_indice=0):
        verificacao = False
        indice = None
        for n, acount in enumerate(self.__clientes):
            if conta == acount.conta.numero_da_conta:
                verificacao = True
                indice = n
                break

        if retornar_indice == 1 and verificacao == True:
            return indice
        else:
            return verificacao

    def cadastrar(self):

        nome = input("Qual é o seu nome? ")
        idade = input("Qual é a sua idade? ")
        tipo_de_conta = int(input("Que tipo de conta deseja abrir? \n 1 para poupança;\n 2 para corrente:\n"))
        inicio = input("Quanto deseja depositar inicialmente? ")
        agencia = int(input("Qual é a agencia?\n 1- 23;\n 2- 11; \n 3- 21:\n"))
        conta = None

        if tipo_de_conta == 1:
            conta = ContaPoupanca(agencia, self.__numero_da_conta, inicio)

        elif tipo_de_conta == 2:
            limite = input("Qual será o limite inicial? ")
            conta = ContaCorrente(agencia, self.__numero_da_conta, inicio, limite)
        
        
        cliente = Cliente(nome, idade, conta)
        self.__clientes.append(cliente)

        self.__numero_da_conta += 1

    def clientes_cadastrados(self):
        self.__clientes.append(Cliente("Wekisley", 22, ContaPoupanca(23, 10000, 20000)))
        self.__clientes.append(Cliente("Vanessa", 29,ContaCorrente(23, 10080, 20000, 800)))
        
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        for cliente in self.__clientes:
            print(f"Nome: {cliente.nome}")
            print(f"Idade: {cliente.idade}")
            print(f"Conta: {cliente.conta.numero_da_conta}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

    def logar(self, agencia, conta):
        if self.verificar_agencia(agencia) and self.verificar_conta(conta):
            return self.__clientes[self.verificar_conta(conta, 1)]
        else:
            print("Conta ou agência não existente!")