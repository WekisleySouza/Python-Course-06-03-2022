tarefas = list()
tarefasDesfeitas = list()

def adicionarTarefa(tarefa, lista):
    lista.append(tarefa)

def listarTarefas(lista):
    print("\n=-=-=- Lista de Tarefas =-=-=-\n")
    for n, tarefa in enumerate(lista):
        print(n + 1, "° ->",tarefa)

    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

def desfazer(lista, listaDesfeitos):
    listaDesfeitos.append(lista[len(lista) - 1])
    del(lista[len(lista) - 1])

def refazer(lista, listaDesfeitos):
    lista.append(listaDesfeitos[len(listaDesfeitos) - 1])
    del(listaDesfeitos[len(listaDesfeitos) - 1])

def menu():
    print("\n##### Menu De Tarefas #####\n")
    print("- O que deseja fazer? \n")
    print("1 - Adicionar tarefa?")
    print("2 - Listar as tarefas?")
    print("3 - Desfazer tarefa adicionada?")
    print("4 - Refazer tarefa removida?")
    print("5 - Fechar programa?")

option = 0

while(option != 5):
    menu()
    option = int(input("\nOpção: "))

    if(option == 1):
        newTarefa = input("\nQual tarefa deseja adicionar?")
        adicionarTarefa(newTarefa, tarefas)
    
    elif(option == 2):
        listarTarefas(tarefas)
    
    elif(option == 3):
        desfazer(tarefas, tarefasDesfeitas)
    
    elif(option == 4):
        refazer(tarefas, tarefasDesfeitas)

print("\nObrigado por utilizar o nosso sistema! ^-^")