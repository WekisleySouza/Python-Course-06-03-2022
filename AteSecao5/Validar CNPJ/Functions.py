def encontrarDigito(cnpj, serie):    
    soma = sum([(int(serie[n]) * int(cnpj[n])) for n in range(0, len(serie))])
    digito = 11 - (soma % 11)

    if digito > 9:
        digito = 0
    
    return str(digito)

def finalCNPJ(cnpj):
    cnpj = str(cnpj)
    serie = "543298765432"
    primeiro = encontrarDigito(cnpj, serie)

    serie = "6543298765432"
    segundo = encontrarDigito(cnpj, serie)

    return int(cnpj + primeiro + segundo)