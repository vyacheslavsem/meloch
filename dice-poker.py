import random 

#Введем глобальные константы
#Количество костей
NUM_OF_DICES = 5
#Количество переброса костей
NUM_OF_REROLLS = 2
def reroll(d,r):
    #Функция reroll() получает набор костей и номеря костей для переброса
    #и возвращает переброшенные кости
    
    #переменная флаг переброса
    succes_reroll = 0 #переброс не состоялся
    # Преобразовывать строку в список с номерами костей
    r = set(r)
    
    #Проверка не слишком ли много костей
    if len(r) > NUM_OF_DICES:
        print("У вас не столько костей!")
        return d,succes_reroll   #Возвращает список костей без изменений
    
    # Проверка корректности номеров костей
    for i in r:
        if i > str(NUM_OF_DICES) or i < '1':
            print("Неверные номера костей!")
            return d, succes_reroll
    
    # Преобразовываем кости из списка 
    for i in r:
        d[int(i)-1] = random.randint(1,6)
    
    succes_reroll = 1
    
    return d,succes_reroll

def comb(dice):
    
    #Введем константы
    #Множества, образующие комбинацию стрит
    #Большие стриты
    BIGSTREET1 = set([1,2,3,4,5])
    BIGSTREET2 = set([2,3,4,5,6])
    
    
    #Малые стриты
    SMSTREET1 = set([1,2,3,4])
    SMSTREET2 = set([2,3,4,5])
    SMSTREET3 = set([3,4,5,6])
    
    #Каре
    KARE = [4]
    
    #Фуллхаус
    FULLH = [2,3]
    
    #Сет
    DSET =  [3]
    
    #Две двойки
    DD = [2,2]
    
    #ДВойка
    SD = [2]
    

    
    #Получаем длину переданной последовательности - 
    #количество костей в комбинации
    l = len(dice)


    #Создаем новый словарь
    #Ключи - это значиния на костях
    d = {1:0,2:0,3:0,4:0,5:0,6:0}
    
    
    #Считаем количество каждого исхода
    for i in range(l):
        d[dice[i]] += 1
                
    #Список комбинаций
    
    cc = []
    
    for i in range(1,7):
        if d[i]>1:
            cc.append(d[i])
    cc.sort()
    
    #Анализ комбинаций
    dice_set = set(dice)
    
    dice_comb = "Шанс"
    
    if len(dice_set) == 5:
        if (dice_set == BIGSTREET1 or dice_set== BIGSTREET2):
            dice_comb = "Большой стрит"
    if len(dice_set) == 4:
        if (dice_set == SMSTREET1 or dice_set == SMSTREET2 or dice_set == SMSTREET3):
            dice_comb="Малый стрит"
        elif cc == SD:
            dice_comb = "Двойка"
    if len(dice_set) == 3:
        if cc == DSET:
            dice_comb = "Сет"
        elif cc == DD:
            dice_comb = "Две двойки"
    if len(dice_set) == 2:
        if cc == FULLH:
            dice_comb = "Фуллхаус"
        if cc == KARE:
            dice_comb = "Каре"
    if len(dice_set) == 1:
        dice_comb="Покер"
    
    return dice_comb
    

def menu(): 

    print("ВЫБЕРИТЕ ДЕЙСТВИЕ: \n")
    print("1 - Бросить кости")
    print("2 - Сортировка комбинаций")
    print("3 - Перебросить кости")
    print()
    print("0 - передать ход")
    print("-"*20)
    
    
def main_menu():
    print("ДОБРО ПОЖАЛОВАТЬ!\n")
    print("ВЫБЕРИТЕ ДЕЙСТВИЕ: \n")
    print("1 - Игроки")
    print("2 - Перейти к игре")
    print("3 - Просмотреть результаты")
    print()
    print("0 - Выйти из игры")

def main_menu_gamers():
    print("ВЫБЕРИТЕ ДЕЙСТВИЕ: \n")
    print("1 - Задать игроков")
    print("2 - Изменить игроков")
    print("3 - Просмотреть игроков")
    print()
    print("0 - назад")
    
def mgamers(g):
    main_menu_gamers()
    answer = input(">>>")
    
    while answer != '0':
        if answer == '1':
            n = int(input("Ведите количество игроков: "))
            for i in range(n):
                g[i] = [input("Ведите имя игрока: "), list(0)*NUM_OF_DICES]
            print(g)
            main_menu_gamers()
            answer = input(">>>")
            
        if answer == '2':
            
            main_menu_gamers()
            answer = input(">>>")
            
        if answer == '3':
            
            main_menu_gamers()
            answer = input(">>>")
            
        else:
            main_menu()
            answer = input(">>>")

def pdice(d):
    res = comb(d)
    print(d, "\t", res)
    

def main_cycle():

    dice = list([0])*NUM_OF_DICES
    
    reroll_times = 0
    
    
    menu()
    answer = input(">>>")


    while(answer != '0' ):
        if answer == '1':
            
            dice,sr = reroll(dice, "12345") #Бросаем кости
            pdice(dice)
            menu()
            answer = input(">>>")
            
        elif answer == '2':
            dice.sort()
            pdice(dice)
            menu()
            answer = input(">>>")
            
        elif answer == '3':
            if reroll_times < NUM_OF_REROLLS:
                rr = input("Укажите номера костей которые нужно перебросить: ")
                dice,sr = reroll(dice,rr)
                if sr == 1:
                    print("Отличный бросок!")
                    reroll_times += 1
        
            else:
                print("Попытки переброса исчерпаны")
                
            pdice(dice)
            menu()
            answer = input(">>>")
            
        else:
            menu()
            answer = input(">>>")
                    
    print("Adios!")
    
def main():
    gamers = {}
    
    main_menu()
    answer = input(">>>")
    
    while answer != '0':
        if answer == '1':
            gamers = mgamers(gamers)
            main_menu_gamers()
            answer = input(">>>")
        else:
            main_menu()
            answer = input(">>>")
   # main_cycle()
    
main()