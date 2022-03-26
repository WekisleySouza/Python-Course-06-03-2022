import os

caminho_procura = r"C:\Users\wekis\Desktop\Python\Python - Udemy"

termo_procura = "Pessoa"

for raiz, diretórios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        tamanho_arquivo = os.path.getsize(caminho_completo)
        print(f"\nArquivo: {arquivo}")
        print(f"Nome: {nome_arquivo}")
        print(f"Extensão: {extensao_arquivo}")
        print(f"Tamanho: {tamanho_arquivo}")
        print(f"Caminho: {caminho_completo}\n")
        