lista_de_listas = [[1, 2, 3, 3, 4, 5, 6, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

def doppel(lista):
    listaTemp = list()
    listaRep = list()

    for subLista in lista:
        for item in subLista:
            if not item in listaTemp:
                listaTemp.append(item)

            elif not item in listaRep:
                listaRep.append(item)
        
        del listaTemp[0:]
            
    if listaRep:
        return True
    else:
        return False

rep = doppel(lista_de_listas)

if rep:
    print("Existem valores repetidos!")
else:
    print("Não tem valores repetidos!")

#Poderia ter usado o Set!