from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(600,400)
        
        self.lbl = QLabel('', self)
        
        self.lbl.setGeometry(20,20,560,360)
        self.lbl.setStyleSheet("border-style: solid;"
                               "border-width: 1px;"
                               "border-color: red;"
                               "background-image: url(froggy.jpg)")



app = QApplication([])
win = MainWindow()
win.show()
app.exec()