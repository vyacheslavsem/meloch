from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(600, 400)
        
        btn = QPushButton("kick me", self)
        btn.move(100,200)
        btn.clicked.connect(self.b_click)
        
    def b_click(self):
        print("ouch!")
        

app = QApplication([])
window = MainWindow()
window.show()

app.exec()

