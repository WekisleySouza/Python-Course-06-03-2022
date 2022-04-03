CPF = '168995350'
tot = 0
pri = 0
mul = 10

for cpf in CPF:
    tot += int(cpf) * mul
    mul -= 1

pri = 11 - (tot % 11)
pri = 0 if pri > 9 else pri

CPF += str(pri)

mul = 11
tot = 0

for cpf in CPF:
    tot += int(cpf) * mul
    mul -= 1

ult = 11 - (tot % 11)
CPF += str(ult)

cpf = input("Digite o seu CPF: ")

print("Válido") if CPF == cpf else print("Inválido")