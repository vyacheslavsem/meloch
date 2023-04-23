import random 
#Введем именованные константы
NUM = 15
WIN = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# Эта программа моделирует "игру 15"

def gen_v():
    seq = [0]*NUM
    seq2 =[]

    
    for i in range(NUM):
        seq2.append([i+1,random.random()])

    
    def funcSort(x):
        return x[1]
    
    ss = sorted(seq2, key=funcSort)
    
    for i in range(NUM):
        seq[i]=ss[i][0]
    
    return seq

def inv_count(seq):
    #Эта функция подсчитывает количество инверсий
    #Инверсия - числа в неправильном порядке

    n = 0
    
    for i in range(NUM-1):
        for j in range(i+1,NUM):
            if seq[i]>seq[j]:
                n += 1    
    
    return n

def print_dice(n):
    if n == 0:
        return "  "
    
    if n < 10:
        return " "+str(n)
    else:
        return str(n)
        

def print_row(seq):

    s1 = " "+chr(9556)+chr(9552)*6+chr(9559)
    s2 = " "+chr(9553)+" "*6 +chr(9553)
    s31= " "+chr(9553)+"  "
    s32="  "+ chr(9553)
    s5 = " "+chr(9562)+chr(9552)*6+chr(9565)
    print()
    print(s1*4)
    print(s2*4)
    print(s31+seq[0]+s32+
          s31+seq[1]+s32+
          s31+seq[2]+s32+
          s31+seq[3]+s32)
    print(s2*4)
    print(s5*4)
    
def print_all(seq):
    
    s = []
    for i in range (NUM+1):
        s.append(print_dice(seq[i]))
    print(s)
    
    print_row(s[0:4])
    print_row(s[4:8])
    print_row(s[8:12])
    print_row(s[12:16])
    
def find_move(seq):
    #функция для поиска допустимых ходов
    
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

def validate_input():
    answer = input(">>> ")
    
    if answer == "":
        return -1
    
    s = set(answer)
    
    for i in s:
        if i <"0" or i > "9":
            return -1
    
    move = int(answer)
    
    return move

def main():
    v = ['']*NUM
    
    # Вызов функции генератора случайной последовательности
    v = gen_v()
    
    # Вызовем функцию подсчета инверсий
    inv = inv_count(v)
    
    #Пока количесвто инверсий нечетное
    while(inv/2 != inv//2):
        #занаво генерируем последовательность
        v = gen_v()
        inv = inv_count(v)
   
    print(v)    
    print("Всего инверсий:", inv)
    
    #Добавляем пустую кость в конец последовательности
    v.append(0)
        
    print_all(v)
    valid_moves=find_move(v)
    
    n = 0
    
    m = -1
    
    
    
    
    while m != 0:
        
        m = validate_input()
        while m == -1:
            m = validate_input()
        
        if m == 0:
            print("больше не хочешь играть? очень жаль")
            break
        
        if m in valid_moves:
            
            a = v.index(0)
            b = v.index(m)
            n+=1
            v[a], v[b] = v[b], v[a]
        else:
            continue
        
        if v == WIN:
            print("ПОЗДРАВЛЯЕМ! Головомка решена!")
            break
    
        print_all(v)
        valid_moves=find_move(v)
    
    print("Потрачено ходов", n)

            
main()