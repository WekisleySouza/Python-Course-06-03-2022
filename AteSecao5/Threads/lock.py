from threading import Thread
from time import sleep
from threading import Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() # Tranca método para não ter threads simultâneas nele.
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release() # Libera o lock de cima.
            return

        sleep(1)

        self.estoque -= quantidade

        print(f'Você comprou {quantidade} ingresso(s).'
        f'Ainda temos {self.estoque} em estoque.')
        
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    threads = list()

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False
        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)
