import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
     QGridLayout, QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora') # Muda nome no cabeçalho.
        self.setFixedSize(400, 400) # Fixa tamanho.

        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit() # Cria o input.
        self.display.setDisabled(True) # Não premite que o usuário digite no input.
        self.display.setStyleSheet(
            '* {'
            'background-color: #fff;'
            'color: #000;'
            'font-size: 30px;'
            '}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding) # Faz o input se ajustar ao espaço vazio.

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1, 
            lambda: self.display.setText(''),
            'background-color: #d5580d; color: #fff; font-weight: 700;'
        )
        

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1, 
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background-color: #13823a; color: #fff; font-weight: 700;'
        )
        

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton('**'), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background-color: #095177; color: #fff; font-weight: 700;'
        )

        self.grid.addWidget(self.display, 0, 0, 1, 5)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        
        if funcao:
            btn.clicked.connect(funcao)
            
        else:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text())) # Fax a conta digitada se for válida.
            )
        except Exception as error:
            self.display.setText('Conta inválida!')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()