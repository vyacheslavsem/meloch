from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import *

# Размеры создаваемого окна
WIN_X_SIZE = 1000
WIN_Y_SIZE = 650

# Кнопки управления
KEY_SIZE = 50         # Размер кнопок управления(UPLR)
KEY_SPC = 5           # Расстояник между кнопками управления
KEY_OSPC = 30         # Отступ блока кнопок от нижнего правого угла

# Игровое поле
F_SIZE = 40     # Размер ячейки игрового поля(ИП)
F_SPC = 5       # Расстояние между клетками ИП
F_OSPC = 30     # Отступ начала ИП от левого верхнего угла
F_MAX_X = 20    # Количество клеток по горизонтали
F_MAX_Y = 10    # Количество клеток по вертикали

# Лягушка
FROG_START_X = 2
FROG_START_Y = 5

# Глобальные пременные
# Текущие координаты лягушки на ИП
frog_i = FROG_START_X
frog_j = FROG_START_Y

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(WIN_X_SIZE, WIN_Y_SIZE)
       
        self.draw_GUI()
        self.draw_Field()
        self.draw_Frog()
        
    def draw_GUI(self):
        btn_up = QPushButton("UP",self)
        btn_up.setObjectName('UP')
        btn_up.setFixedSize(KEY_SIZE,KEY_SIZE)
        btn_up.move(WIN_X_SIZE - KEY_OSPC - 2*KEY_SIZE, WIN_Y_SIZE - KEY_OSPC - 2*KEY_SIZE )
        name = btn_up.objectName()
        btn_up.clicked.connect(lambda a, name = name: self.btn_click(name))
        
        btn_left = QPushButton("LEFT",self)
        btn_left.setObjectName('LEFT')
        btn_left.setFixedSize(KEY_SIZE,KEY_SIZE)
        btn_left.move(WIN_X_SIZE - KEY_OSPC - 3*KEY_SIZE, WIN_Y_SIZE - KEY_OSPC - KEY_SIZE )
        name = btn_left.objectName()
        btn_left.clicked.connect(lambda a, name = name: self.btn_click(name))
        
        btn_down = QPushButton("DOWN",self)
        btn_down.setObjectName('DOWN')
        btn_down.setFixedSize(KEY_SIZE,KEY_SIZE)
        btn_down.move(WIN_X_SIZE - KEY_OSPC - 2*KEY_SIZE, WIN_Y_SIZE - KEY_OSPC - KEY_SIZE )
        name = btn_down.objectName()
        btn_down.clicked.connect(lambda a, name = name: self.btn_click(name))
        
        btn_right = QPushButton("RIGHT",self)
        btn_right.setObjectName('RIGHT')
        btn_right.setFixedSize(KEY_SIZE,KEY_SIZE)
        btn_right.move(WIN_X_SIZE - KEY_OSPC - KEY_SIZE, WIN_Y_SIZE - KEY_OSPC - KEY_SIZE )
        name = btn_right.objectName()
        btn_right.clicked.connect(lambda a, name = name: self.btn_click(name))
        
    def draw_Field(self):
        num = 0
        self.cells = []
        for i in range (F_MAX_X):
            for j in range(F_MAX_Y):
                btn = QPushButton("",self)
                btn.setObjectName('btn_'+str(i)+"_"+str(j))
                btn.setCheckable(True)
                btn.setFixedSize(F_SIZE, F_SIZE)
                btn.move(F_OSPC+(F_SIZE+F_SPC)*i,F_OSPC+(F_SIZE+F_SPC)*j)
                
                obj = btn
                btn.clicked.connect(lambda a, obj = obj:self.FieldToggle(btn))
                self.cells.append(btn)
                btn = QPushButton('',self)
                btn.hide()
                num+=1
    def FieldToggle(self, obj):
        obj.toggle()            
    
    def draw_Frog(self):
        global frog_i
        global frog_j
        
        self.frog = QPushButton('',self)
        self.frog.setFixedSize(F_SIZE,F_SIZE)
        #icon = QIcon(QPixmap("froggy.jpg"))
        #frog.setIcon(icon)
        self.frog.setStyleSheet("border-style: solid;"
                           "border-width: 0px;"
                           "border-color: green;"
                           "background-color: white;"
                           "border-radius:20px;"
                           "image: url(bat.gif)")
        
        x,y = self.getFrogCoord(frog_i, frog_j)
        self.frog.move(x,y)
        
    def getFrogCoord(self, i,j):
        x = F_OSPC + (i - 1)*(F_SPC + F_SIZE)
        y = F_OSPC + (j - 1)*(F_SPC + F_SIZE)
        return x,y
        
        
    def btn_click(self,name):
        global frog_i
        global frog_j
        
        if name == 'UP':
            res = self.validateCoord(frog_i,frog_j-1)
            if res == True:
                frog_j -=1
        
        if name == 'DOWN':
            res = self.validateCoord(frog_i,frog_j+1)
            if res == True:
                frog_j +=1
                
        if name == 'LEFT':
            res = self.validateCoord(frog_i-1,frog_j)
            if res == True:
                frog_i -=1
                
        if name == 'RIGHT':
            res = self.validateCoord(frog_i+1,frog_j)
            if res == True:
                frog_i +=1
                
        x,y = self.getFrogCoord(frog_i, frog_j)
        self.frog.move(x,y)
            
    def validateCoord(self, i,j):
        res = False
        
        if i > 0 and i <= F_MAX_X and j > 0 and j <= F_MAX_Y:
            cells_i = i - 1
            cells_j = j - 1
            num = int(str(cells_i)+str(cells_j))
            if self.cells[num].isChecked() != True:
                res = True
        return res
            
    
    
app = QApplication([])
window = MainWindow()

window.show()

app.exec()