import pickle
import sys
import random

from PyQt5.QtWidgets import QApplication,\
                            QMainWindow,\
                            QPushButton,\
                            QLabel,\
                            QAction,\
                            QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Введем константы
# Размер поля
RX = 4
RY = 4
DICE_NUM = RX*RY

# Сгенерируем условие победы - правильная последовательность
WIN = []
for i in range(DICE_NUM-1):
    WIN.append(i+1)
WIN.append(0)

# Настройки интерфейса
WIN_SPC = 50
DICE_SIZE = 70
INTER_SIZE = 30

# Вычислим размеры окна
WIN_X = 2*WIN_SPC+DICE_SIZE*RX
WIN_Y = 2*WIN_SPC+DICE_SIZE*RY+INTER_SIZE

class SetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        w = 400
        h = WIN_SPC*2+INTER_SIZE*4
        self.setFixedSize(w, h)
        self.setWindowTitle("Настройки цветов")
        
        palette = [win.palette[0],
                   win.palette[1],
                   win.palette[2],
                   win.palette[3]]
        
        collbls = ["R","G","B"]
        for i in range(3):
            self.lbl = QLabel(collbls[i],self)
            x = WIN_SPC + 90 + (5+30)*i
            y = WIN_SPC - 30
            self.lbl.setGeometry(x,y,30, INTER_SIZE)
            self.lbl.setAlignment(Qt.AlignCenter)
            self.lbl.setStyleSheet("border-style: solid;"
                                   'border-width: 0px;'
                                   'border-color: red;')
        
        
        collbls = ["Цвет1 :","Цвет2 :","Цвет текста :","Цвет доски :"]
        
        for i in range(4):
            self.lbl = QLabel(collbls[i], self)
            x = WIN_SPC
            y = WIN_SPC + INTER_SIZE*i
            self.lbl.setGeometry(x,y,90, INTER_SIZE)
            self.lbl.setStyleSheet("border-style: solid;"
                                   'border-width: 0px;'
                                   'border-color: red;')
            
        colorLE = {"c1":[0]*3,
                   "c2":[0]*3,
                   "c3":[0]*3,
                   "c4":[0]*3}
        keys = list(colorLE.keys())
        for c in range(4):              # ключи - цвета с1 с2 с3 с4
            for i in range(3):          # основные цвета RGB
                self.cle= QLineEdit(self)
                x = WIN_SPC + 90 + (5+30)*i
                y = WIN_SPC + INTER_SIZE*c
                self.cle.setGeometry(x,y,30, INTER_SIZE)
                self.cle.setText(str(palette[c][i]))
                colorLE[keys[c]][i] = self.cle
                obj = self.cle
                p = palette
                ar = (c,i)
                self.cle.textChanged.connect(lambda a, obj=obj, p=p, ar=ar:
                                             self.changePal(obj=obj,p=p, ar=ar))
                
    def changePal(self, obj, p, ar):
        
        win.palette[ar[0]][ar[1]] = int(obj.text())
        win.redraw_field()
        
        #p[ar[0]][ar[1]] = int(obj.text())
        #print(obj.text(), p)
        #return p
                
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,50,WIN_X,WIN_Y)
        self.setFixedSize(WIN_X, WIN_Y)
        
        self.palette = [ [255,255,255],      # цвет кости
                         [150,150,150],      # цвет border
                         [0,0,0],            # цвет текста
                         [50,50,50]]        # цвет пустого поля
        self.drawField()
        self.drawGUI()
        self.GameInit()
        
    def drawGUI(self):
        self.winlbl = QLabel("", self)
        self.winlbl.hide()
        
        ngameAction = QAction('Новая игра',self)
        ngameAction.setShortcut('Ctrl+N')
        ngameAction.setStatusTip('Новая игра')
        ngameAction.triggered.connect(self.GameInit)
        
        lgameAction = QAction('Загрузить игру',self)
        lgameAction.setShortcut('Ctrl+L')
        lgameAction.setStatusTip('Загрузить сохраненную игру')
        lgameAction.triggered.connect(self.GameLoad)
        
        sgameAction = QAction('Сохранить игру',self)
        sgameAction.setShortcut('Ctrl+S')
        sgameAction.setStatusTip('Сорхранить текущую игру')
        sgameAction.triggered.connect(self.GameSave)
        
        
        exitAction = QAction(QIcon('exit.png'), 'Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из игры')
        exitAction.triggered.connect(self.GameInit)
        
        colorAction = QAction('Цвета', self)
        colorAction.setShortcut('Ctrl+C')
        colorAction.setStatusTip('Настройки цветов')
        colorAction.triggered.connect(self.SetColors)
        
        fieldAction = QAction('Поле', self)
        fieldAction.setShortcut('Ctrl+O')
        fieldAction.setStatusTip('Настройки интерфейса')
        fieldAction.triggered.connect(self.SetField)
        
        menubar = self.menuBar()
        gameMenu = menubar.addMenu('Игра')
        gameMenu.addAction(ngameAction)
        gameMenu.addAction(sgameAction)
        gameMenu.addAction(lgameAction)
        gameMenu.addAction(exitAction)
        
        settingsMenu = menubar.addMenu('Настройки')
        settingsMenu.addAction(colorAction)
        settingsMenu.addAction(fieldAction)
                           
    def drawField(self):
        self.field = []
        for i in range(RY):
            
            for j in range(RX):
                s = str(i*RX+j)
                self.btn = QPushButton(s, self)
                name = s
                self.btn.setObjectName(name)
                self.btn.setFixedSize(DICE_SIZE, DICE_SIZE)
                self.btn.move(WIN_SPC+DICE_SIZE*j,
                          WIN_SPC+DICE_SIZE*i)
                self.btn.setStyleSheet("border-style: outset;"
                                       "border-width: 5px;"
                                       "border-color: green;"
                                       "background-color: black;"
                                       "color: white;"
                                       "font-size: 35px;"
                                       "font-weight: bold;")
                btn = self.btn
                self.btn.clicked.connect(lambda a, btn = btn:
                                         self.btn_clk(btn))
                self.field.append(self.btn)
                

    def btn_clk(self, btn):
        moves = self.find_move()
        m = int(btn.text())
        if m in moves:
            a = self.seq.index(0)
            b = self.seq.index(m)
            self.move_number +=1
            self.statusBar().showMessage("Сделано ходов: \t"+str(self.move_number))
            self.seq[a], self.seq[b] = self.seq[b], self.seq[a]
            
        self.redraw_field()
        
        if self.seq == WIN:
            self.statusBar().showMessage("ПОБЕДА! Затрачено ходов: \t"+str(self.move_number))
            
            self.showMsg("ВЫ ПОБЕДИЛИ!")
            
    def showMsg(self, s):
        self.winlbl.show()
        self.winlbl.setText(s)
        
        self.winlbl.setGeometry(WIN_SPC,
                                WIN_SPC,
                                DICE_SIZE*RX,
                                DICE_SIZE*RY)
        self.winlbl.setAlignment(Qt.AlignCenter)
        self.winlbl.setStyleSheet("border-style: solid;"
                               "border-width: 0px;"
                               "border-color: black;"
                               "font-size:24px;"
                               "font-family: Andale Mono;"
                               "font-weight: bold;"
                               "color: rgb(200,0,50);"
                               "background-color: rgb(255,255,255,200)")
            
    def GameInit(self):
        self.winlbl.hide()
        self.move_number = 0
        self.statusBar().showMessage("Сделано ходов: \t"+str(self.move_number))
        
        self.gen_v()
        
        # Вызовем функцию подсчета инверсий
        inv = self.inv_count()
        
        #Пока количесвто инверсий нечетное
        while(inv/2 != inv//2):
            #занаво генерируем последовательность
            self.gen_v()
            inv = self.inv_count()
        self.seq.append(0)
        
        print(self.seq)
    
        self.redraw_field()
        
    
    def redraw_field(self):
        palette =[self.setCol(self.palette[0][0],self.palette[0][1],self.palette[0][2]),
                  self.setCol(self.palette[1][0],self.palette[1][1],self.palette[1][2]),
                  self.setCol(self.palette[2][0],self.palette[2][1],self.palette[2][2]),
                  self.setCol(self.palette[3][0],self.palette[3][1],self.palette[3][2])]
        
        for i in range(DICE_NUM):
            value = self.seq[i]
            btn = self.field[i]
            if value == 0:
                btn.setStyleSheet("border-style: none;"
                                      "border-width: 0px;"
                                       "border-color: {c1};"
                                       "background-color: {c4};"
                                       "color: {c3};"
                                       "font-size: 35px;"
                                       "font-weight: bold;".format(c1=palette[0],
                                                                    c4=palette[3],
                                                                    c3=palette[2]))
                btn.setText("")
                btn.setEnabled(False)
            else:
                btn.setText(str((value)))
                btn.setStyleSheet("border-style: outset;"
                                       "border-width: 5px;"
                                       "border-color: {c1};"
                                       "background-color: {c2};"
                                       "color: {c3};"
                                       "font-size: 35px;"
                                       "font-weight: bold;".format(c1=palette[1],
                                                                    c2=palette[0],
                                                                    c3=palette[2]))
                btn.setEnabled(True)
                
    def setCol(self,r,g,b):
        color = "rgb("+str(r)+","+str(g)+","+str(b)+")"
        
        return color

    def gen_v(self):
        
        self.seq = [0]*(DICE_NUM-1)
        seq2 =[]

        
        for i in range(DICE_NUM - 1):
            seq2.append([i+1,random.random()])

        
        ss = sorted(seq2, key=lambda x: x[1])
        
        for i in range(DICE_NUM - 1):
            self.seq[i]=ss[i][0]
        
        
        
    def inv_count(self):
        #Эта функция подсчитывает количество инверсий
        #Инверсия - числа в неправильном порядке

        n = 0
        
        for i in range(DICE_NUM-2):
            for j in range(i+1,DICE_NUM-1):
                if self.seq[i] > self.seq[j]:
                    n += 1    
        
        return n


    def find_move(self):
        #функция для поиска допустимых ходов
        
        seq = self.seq
        
        #найдем элемент 0
        #Его индекс
        i_z = seq.index(0)
        #Он в строке row_z
        row_z = 1+i_z//4
        #Он в столбце col_z
        col_z = i_z - (row_z - 1)*4 + 1
        
        #Список допустимыз ходов. Пока пуст
        moves=[]
        
        #UP Можно подать вверх
        if row_z <4:
            row_m = row_z+1
            col_m = col_z
            i_m = (row_m -1)*4 +col_m -1
            moves.append(seq[i_m])
            
        #DOWN Можно подать вниз
        if row_z  > 1:
            row_m = row_z-1
            col_m = col_z
            i_m = (row_m -1)*4 +col_m -1
            moves.append(seq[i_m])
        #LEFT Можно подать влево
        if col_z < 4:
            row_m = row_z
            col_m = col_z+1
            i_m = (row_m -1)*4 +col_m -1
            moves.append(seq[i_m])
        #RIGHT Можно подать вправо
        if col_z > 1:
            row_m = row_z
            col_m = col_z-1
            i_m = (row_m -1)*4 +col_m -1
            moves.append(seq[i_m])
             
        print("Доступные ходы:",moves)
        
        return moves
        

    def GameLoad(self):
        
        file = None
        savefile = 'game15.sav'
        
        try:
            file = open(savefile, "rb")
            savedata = pickle.load(file)
        except:
            print("ERROR LOADING FILE!\n")
            self.statusBar().showMessage("ОШИБКА ЗАГРУЗКИ ФАЙЛА!")
        else:
            self.move_number = savedata[0]
            self.seq = savedata[1]
            print('LOADING SUCCESS!\n')
            self.statusBar().showMessage("ЗАГРУЗКА ПРОШЛА УСПЕШНО")
            self.redraw_field()    
        finally:
            if file != None:
                file.close()
    def GameSave(self):
        file = None
        savefile = 'game15.sav'
        
        savedata = [self.move_number, self.seq]
        
        try:
            file = open(savefile, "wb")
            res = pickle.dump(savedata, file)
            
        except:
            print('ERROR SAVING FILE! \n')
            self.statusBar().showMessage("ОШИБКА СОХРАНЕНИЯ ФАЙЛА!")
            
        else:
            print('SAVING SUCCESS!\n')
            self.statusBar().showMessage("СОХРАНЕНИЕ ПРОШЛО УСПЕШНО")
            
        finally:
            if file != None:
                file.close()
        
    def SetColors(self):
        
        print("Changing colors...\n")
        
        self.winc = SetWindow()
        self.winc.show()
        self.winc.setGeometry(WIN_X+70,50,200,200)
        
    def SetField(self):
        print("Setting GUI...\n")
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())