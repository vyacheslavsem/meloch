from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(1000, 600)
        self.setMaximumSize(700,800)
        self.setMinimumSize(600,400)
        
        self.draw_GUI()
        
    def draw_GUI(self):
        
        btn1 = QPushButton(self)
        btn1.setFixedSize(50,50)
        btn1.move(50,50)
        ic = QIcon(QPixmap("btn1.jpg"))
        btn1.setIcon(ic)
        btn1.setObjectName("b1")
        #Создадим обработчик событий
        name = btn1.objectName()
        btn1.clicked.connect(lambda a, name=name :self.btn_click(name))
        
        btn2 = QPushButton(self)
        btn2.setFixedSize(50,50)
        btn2.move(105,50)
        ic1 = QIcon(QPixmap("btn2.jpg"))
        btn2.setIcon(ic1)
        btn2.setObjectName("b2")
        name = btn2.objectName()
        btn2.clicked.connect(lambda  a, name=name:self.btn_click((name)))
        
        btn3 = QPushButton(self)
        btn3.setFixedSize(50,50)
        btn3.move(160,50)
        ic2 = QIcon(QPixmap("btn3.jpg"))
        btn3.setIcon(ic2)
        btn3.setObjectName("b3")
        name = btn3.objectName()
        btn3.clicked.connect(lambda a, name=name :self.btn_click((name)))
        
        btn4 = QPushButton(self)
        btn4.setFixedSize(50,50)
        btn4.move(215,50)
        ic3 = QIcon(QPixmap("btn4.jpg"))
        btn4.setIcon(ic3)
        btn4.setObjectName("b4")
        name = btn4.objectName()
        btn4.clicked.connect(lambda a, name=name :self.btn_click((name)))
        
        btn5 = QPushButton(self)
        btn5.setFixedSize(50,50)
        btn5.move(270,50)
        ic4 = QIcon(QPixmap("btn5.jpg"))
        btn5.setIcon(ic4)
        btn5.setObjectName("b5")
        name = btn5.objectName()
        btn5.clicked.connect(lambda a, name=name :self.btn_click(name))
        
    def btn_click(self,name):
        print(name)
    
    
    
app = QApplication([])
window = MainWindow()

window.show()

app.exec()