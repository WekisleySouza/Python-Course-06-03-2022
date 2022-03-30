from threading import Thread
from time import sleep

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        Thread.__init__(self)

    def run(self):
        sleep(self.tempo)
        print(self.texto)

'''t1 = MeuThread('Thread 1', 5)
t1.start()'''

def teste_modo_2(texto, tempo):
    sleep(tempo)
    print(texto)

# Outro modo:
t = Thread(target=teste_modo_2, args=('Olá mundo!', 3))
t.start()

# Esperando thread termonar:
while t.is_alive():
    print('Esperando a thread!')
    sleep(2)

print('Thread acabou!')

for i in range(20):
    print(i)
    sleep(i)

