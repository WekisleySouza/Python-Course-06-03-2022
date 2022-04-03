from Class.Cliente import Cliente
from Class.ContaCorrente import ContaCorrente
from Class.ContaPoupanca import ContaPoupanca


class Banco:
    def __init__(self, nome = "Unknown"):
        self.__nome = nome
        self.__agencias = (23, 11, 21)
        self.__clientes = list()
        self.__numero_da_conta = 10000000
        self.adm_pass = "wek123"

    @property
    def nome(self):
        return self.__nome
            
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
        print("=" * 10, f"Banco {self.nome}", "=" * 10)

        nome = input("Qual é o nome do cliente? ")
        idade = input("Qual é a idade? ")
        tipo_de_conta = int(input("Que tipo de conta deseja abrir? \n 1 para poupança;\n 2 para corrente:\n"))
        inicio = float(input("Quanto deseja depositar inicialmente? "))
        agencia = int(input("Qual é a agencia?\n 1- 23;\n 2- 11; \n 3- 21:\n"))
        conta = None

        if tipo_de_conta == 1:
            conta = ContaPoupanca(agencia, self.__numero_da_conta, inicio)

        elif tipo_de_conta == 2:
            limite = float(input("Qual será o limite inicial? "))
            conta = ContaCorrente(agencia, self.__numero_da_conta, inicio, limite)
        
        
        cliente = Cliente(nome, idade, conta)
        self.__clientes.append(cliente)

        self.__numero_da_conta += 1

    def clientes_cadastrados(self):
        
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        for cliente in self.__clientes:
            print(f"Nome: {cliente.nome}")
            print(f"Idade: {cliente.idade}")
            print(f"Conta: {cliente.conta.numero_da_conta}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

    def menu_cliente(self, indice_do_cliente):
        print("=" * 10, f"Banco {self.nome}", "=" * 10)

        print(f"Olá {self.__clientes[indice_do_cliente].nome}, o que deseja fazer? [Digite o número da opção]")
        opcao = int(input(" 1- Sacar;\n 2- Depositar;\n 3- Consultar saldo;\n 4- Sair?\n "))

        if opcao == 1:
            valor =  float(input("Quanto você deseja sacar? "))
            self.__clientes[indice_do_cliente].conta.sacar(valor)
        elif opcao == 2:
            valor =  float(input("Quanto você deseja depositar? "))
            self.__clientes[indice_do_cliente].conta.deposito(valor)
        elif opcao == 3:
            saldo_da_conta = self.__clientes[indice_do_cliente].conta.saldo
            print(f"Seu saldo na conta: {saldo_da_conta:.2f}")
        elif opcao == 4:
            print("Obrigado por utilizar o nosso sistema! ^-^")
            self.menu()
        
        if opcao != 4:
            self.menu_cliente(indice_do_cliente)

    def logar(self):
        print("=" * 10, f"Banco {self.nome}", "=" * 10)
        
        agencia = int(input("Qual é o número da agência? "))
        conta = int(input("Qual é o número da conta? "))

        if self.verificar_agencia(agencia) and self.verificar_conta(conta):
            indice_do_cliente = self.verificar_conta(conta, 1)
            print(indice_do_cliente)
            self.menu_cliente(indice_do_cliente)
        else:
            print("Conta ou agência não existente!")
            self.menu()

    def menu_adm(self):
        print("=" * 10, f"Banco {self.nome}", "=" * 10)
        print("\nO que deseja fazer? [Digite o número da opção]")
        opcao = int(input(" 1- Cadastrar Cliente;\n 2- Ver clientes cadastrados;\n 3- Fazer login?\n 4- Sair\n "))

        if opcao == 1:
            self.cadastrar()
        elif opcao == 2:
            self.clientes_cadastrados()
        elif opcao == 3:
            self.logar()
        elif opcao == 4:
            self.menu()
            
        if opcao != 4:
            self.menu_adm()

    def menu(self):
        print("=" * 10, f"Banco {self.nome}", "=" * 10)
        print("Quem é você? [Digite o número da opção]")
        opcao = int(input(" 1- Administrador?\n 2- Cliente?\n "))
        if opcao == 1:
            senha = input("Digite a senha administrativa: ")
            if senha == self.adm_pass:
                self.menu_adm()
            else:
                print("Senha incorreta!")
                self.menu()
        elif opcao == 2:
            self.logar()