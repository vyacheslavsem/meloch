PI = 3.141592

class Shapes:
    
    def __init__(self, v, l):
        self.__vertices = v # Количество вершин
        self.__lenth = l # Длина сторон
    
    def __str__(self):
        return "У этой фигуры "+str(self.__vertices)+\
            " вершин. Стороны равны: "+str(self.__lenth)
    
    def setVert(self, v):
        if v < 0:
            print("Количество вершин не может быть отрицательным")
        else:
            self.__vertices = v
    
    def setLen(self, l):
        self.__lenth = l
    
    def getVert(self):
        return self.__vertices
    
    def getLen(self):
        return self.__lenth
    
    def findP(self):
        return "Необходимо уточнить форму фигуры"
    
    def findS(self):
        return "Необходимо уточнить форму фигуры"

class Circle(Shapes):
    
    def __init__(self, v, l, n):
        Shapes.__init__(self, v, l)
        self.__name = n
    
    def getName(self):
        return self.__name
    
    def __str__(self):
        return "Это окружность с радусом "+str(Shapes.getLen(self))
    
    def findP(self):
        r = Shapes.getLen(self)
        P = 2*PI*r
        return P
    
    def findS(self):
        r = Shapes.getLen(self)
        S = PI*r**2
        return S

class Rectangle(Shapes):
    
    def __init__(self, v, l, n):
        Shapes.__init__(self, v, l)
        self.__name = n
    
    def getName(self):
        return self.__name
    
    def __str__(self):
        return "Это прямоугольник со сторонами "+str(Shapes.getLen(self))
    
    def findP(self):
        a = Shapes.getLen(self)[0]
        b = Shapes.getLen(self)[1]
        P = 2*(a+b)
        return P
    
    def findS(self):
        a = Shapes.getLen(self)[0]
        b = Shapes.getLen(self)[1]
        S = a*b
        return S
    

