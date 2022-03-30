import subprocess

# Windowns - ping 127.0.0.1
# Linux - 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'], 
    capture_output=True
)
# O capture faz a saída do comando ir para a própria variável.

print(proc.stderr)
print(proc.stdout) 
print(proc.returncode) # Executou com sucesso?
print(proc.args) # Seus argumentos

saida = proc.stdout
print(saida)