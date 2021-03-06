import os
import shutil

caminho_original = r"C:\Users\wekis\Desktop\Python\Python - Udemy\Mover, copiar e apagar\Teste1"
caminho_novo = r"C:\Users\wekis\Desktop\Python\Python - Udemy\Mover, copiar e apagar\Teste2"

try:
    os.mkdir(caminho_novo)
except FileExistsError as error:
    print(f"Pasta {caminho_novo} já existe!")

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        
        if ".txt" in file:
            os.remove(old_file_path)
            print(file)