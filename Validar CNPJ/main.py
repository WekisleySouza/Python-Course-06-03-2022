from Functions import finalCNPJ

tam = 0
while tam == 0:
    CNPJ = input("Qual é o seu cnpj [Somente os números]?")
    print(len(str(CNPJ)))
    if len(str(CNPJ)) == 12:
        tam == 1
    else:
        print("\nCNPJ inválido, tente novamente!\n")

validadoCNPJ = "04252011000110"

print(finalCNPJ(validadoCNPJ))

