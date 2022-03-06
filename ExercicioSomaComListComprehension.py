carrinho = [('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

total = sum([carrinho[s][1] for s in range(0, len(carrinho))])

print(f"Meu: {total}")

#Solução do professor:

totalProf = sum([float(y) for x, y in carrinho])

print(f"\nProf: {totalProf:.2f}")