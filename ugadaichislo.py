import random

MINN = 1     # Минимальное число для угадывания
MAXN = 100   # Максимальное число для угадывания
MAXDEV = 20  # Отклонение, вызывающее слово "намного"

INPUT_MSG = "Введите число от "+str(MINN)+" до "+str(MAXN)+" или 0 для выхода: "

def intro():
    # Это правила игры
    print("Эта программа загадывает число")
    print("от", MINN, "до", MAXN)
    print("Попробуй угадать!\n")
    
def exit_game():
    # Это увидит пользователь когда выйдет из игры
    print("Не хотите играть? Очень жаль(")
    print("Заходите в другой раз!")
    print("ASTA LA VISTA, BABY")
    print("I'L BE BACK")
    
def win():
    print("ВЫ УГАДАЛИ!")  
    print("ПОЗДРАВЛЯЕМ!")

def validate_num(s):
    # Получает строку s
    # Проверяет строку:
    # Если в ней только цефры - возвращает число
    # Иначе выдает сообщение об ошибке и возвращает -1
    
    
    vs = set(s)
    
    # Проеряем, не содержит ли строка что-то кроме цифр
    for c in vs:
        if c < "0" or c > "9":
            print("Недопустимый ввод!")
            return -1
    
    # Преобразуем строку в число
    n = int(s)
        
        # Если 0 - пользователь не хочет играть
    if n == 0:
        return 0
        
    # Попало ли число в допустимый интервал
    if n < MINN or n > MAXN:
        print("Загадано число от", MINN, "до", MAXN)
        print("Введите другой ответ!")
        return -1

    return n

def message(n):
    m=[["ОГО! Намного меньше!", "Слишком большое! Бери меньше", "Число намного меньше"],  # message 1 значит больше
       ["Перебор!","Загаданное число меньше"],  # message 2 больше
       ["Недолет! Нужно намного больше", "Холодно! Загаданное число намного больше"],  # message 3 значит меньше
       ["Бери больше", "Чуть побольше"]]  # message 4 меньше
    
    print(m[n-1][random.randint(1,len(m[n-1]))-1])

def main():
    intro()
    
    # Сгенереруем случайное целое число от MINN до MAXN
    gnumber = random.randint(MINN, MAXN)
    
    # Введеем пользовательский ввод и отправим на валидацию
    number = -1
    
    
    while number != gnumber:
        while number < 0:
            number = validate_num(input(INPUT_MSG))
    
        if number == gnumber:
            break
    
        if number == 0:
            exit_game()
            return

        # Проверка основных условий
        difference = gnumber - number
        if difference < 0 and difference < -MAXDEV:
            message(1)
        elif difference < 0 and difference > -MAXDEV:
            message(2)
        elif difference > 0 and difference > MAXDEV:
            message(3)
        else:
            message(4)
            
        number = -1

    print("ВЫ УГАДАЛИ!\nБыло загадано число", gnumber)
    print("Заходите еще!")
    

main()