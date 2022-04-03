import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet( # Isso funciona para estilizar como no css.
            'font-size: 40px;' 
            'background-color: red'
        ) 

        self.grid.addWidget(self.btn, 0, 0, 1, 1) # Botão a adicionar, linha, coluna, linspan, colspan.
        
        self.btn.clicked.connect(lambda: print('Olá Wekisley!')) # Adiciona ação a um botão.

        self.setCentralWidget(self.cw)

if __name__ == '__main__':
    qt = QApplication(sys.argv)

    app = App()

    app.show()

    qt.exec_()