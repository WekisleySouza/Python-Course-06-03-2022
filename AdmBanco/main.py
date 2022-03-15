from Class.Banco import Banco
from Class.ContaPoupanca import ContaPoupanca

a = Banco()
#a.cadastrar()
a.clientes_cadastrados()

print(a.logar(23, 10000))

'''def teste():
    tupla = (1, 2, 3, 4, 5,  6, 7,8)

    for i, n in enumerate(tupla):
        if n == 5:
            print("Igual!!")
            return "Foi!"
        print('Diferente!!')

    print("Não parou!")
    return "Oloko bicho!"

print(teste())'''