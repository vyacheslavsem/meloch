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
        
        for i in range(5):
        
            btn = QPushButton(self)
            btn.setFixedSize(50,50)
            btn.move(50+55*i,50)
            iname="btn"+str(i+1)+".jpg"
            ic = QIcon(QPixmap(iname))
            btn.setIcon(ic)
            btn.setObjectName("b"+str(i+1))
            #Создадим обработчик событий
            name = btn.objectName()
            btn.clicked.connect(lambda a, name=name :self.btn_click(name))
        
        
        
    def btn_click(self,name):
        print(name)
    
    
    
app = QApplication([])
window = MainWindow()

window.show()

app.exec()