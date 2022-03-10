from Functions import finalCNPJ

CNPJ = input("Qual é o seu cnpj [Somente os números]?")

if len(str(CNPJ)) != 12 or not CNPJ.isnumeric():
    option = input("\nCNPJ inválido!\n")
else:
    validadoCNPJ = finalCNPJ(CNPJ[0, 10])

    if validadoCNPJ == CNPJ:
        print("CNPJ é válido!")
    else:
        print("CNPJ não é válido!")