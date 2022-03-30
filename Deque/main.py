from collections import deque

# Parâmetro opcional -> deque(maxlen=5) Define um tamanho máximo para a fila.
# Se você adiciona acima do max permitido, ele apaga o elemento mais antigo na fila. 
fila = deque()
fila.extend(['Caio', "Ana", "Dinorá"])
fila.append("João")
fila.append("Carlos")
fila.append("Maria")

print(fila)

print(f"Saiu {fila.pop()}!")

# Colocar um número de termos do fim da fila para o início:
fila.rotate(2)

print(fila)