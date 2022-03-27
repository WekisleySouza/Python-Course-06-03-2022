from zipfile import ZipFile
import os

caminho = r'C:\Users\wekis\Desktop\Python\Python - Udemy\Compactando e Decompactando arquivos\arquivos\compactar'

with ZipFile(r'C:\Users\wekis\Desktop\Python\Python - Udemy\Compactando e Decompactando arquivos\arquivos\decompactar\arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

with ZipFile(r'C:\Users\wekis\Desktop\Python\Python - Udemy\Compactando e Decompactando arquivos\arquivos\decompactar\arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile(r'C:\Users\wekis\Desktop\Python\Python - Udemy\Compactando e Decompactando arquivos\arquivos\decompactar\arquivo.zip', 'r') as zip:
    zip.extractall(r'C:\Users\wekis\Desktop\Python\Python - Udemy\Compactando e Decompactando arquivos\arquivos\decompactar\descompactado')
    