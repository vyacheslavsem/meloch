import random

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
        
        
        

    print(cc)
    
    
    return dice_comb
    
def main():
    
    l = [0]*5
    for i in range (len(l)):
        l[i] = random.randint(1,6)
    
    res = comb(l)
    l.sort()
    print(l, res)
    
main()