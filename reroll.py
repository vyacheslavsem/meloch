import random

NUM_OF_DICES = 5

def reroll(d,r):
    #Функция reroll() получает набор костей и номеря костей для переброса
    #и возвращает переброшенные кости
    
    # Преобразовывать строку в список с номерами костей
    r = set(r)
    
    #Проверка не слишком ли много костей
    if len(r) > NUM_OF_DICES:
        print("У вас не столько костей!")
        return d   #Возвращает список костей без изменений
    
    # Проверка корректности номеров костей
    for i in r:
        if i > str(NUM_OF_DICES) or i < '1':
            print("Неверные номера костей!")
            return d
    
    # Преобразовываем кости из списка 
    for i in r:
        d[int(i)-1] = random.randint(1,6)
    
    return d

def main():
    
    dice = list([0])*NUM_OF_DICES
    
    s = ""
    n = random.randint(0,6) #Сколько кубиков хотим перебросить
    for i in range(0,n):
        s += str(random.randint(1,5))
        
    print("n = ", n, set(s))
    
    dice = reroll(dice,s)
    print(dice)

main()