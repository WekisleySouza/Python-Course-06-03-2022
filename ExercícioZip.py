from itertools import zip_longest


listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]
#listaSoma = [listaA[soma] + listaB[soma] for soma in range(0, len(listaB))]

#Solução do professor:
#listaSoma = [x + y for x, y in zip(listaA, listaB)]

#Outra solução:
listaSoma = [x + y for x, y in zip_longest(listaA, listaB, fillvalue=0)]

print(listaSoma)