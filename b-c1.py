from  random import choice                      # Импортируем функцию choice из библиотеки random
z = '0123456789'                                # Создаём строку z
x = choice(z[1:10])                             # Создаём строку x из одного случайно выбранного символа из среза строки z (без 0)
for i in range(3):                              # В цикле из 3-x повторений
    z = ''.join(z.split(x[i]))                  # удаляем из строки z символ который добавили в строку x,
    x += choice(z)                              # добавляем к строке x случайно выбранные символы из строки z.
n = 0                                           # Счётчик ходов
while True:
    y = input("Введите четырёхзначное число: ") # Функция ввода строки
    n += 1                                      # Увеличиваем счётчик ходов на 1
    b = 0; c = 0                                # Создаём переменные Bulls и Cows
    for i in range(4):                          # В цикле из 4-x повторений
        if x[i] == y[i]:                        # проверяем цифра на своём месте,
            b += 1                              # если да, то добавляем быка,
        elif y[i] in x:                         # если нет, проверяем есть ли в загаданном числе эта цифра?
            c += 1                              # если да, то добавляем корову
    print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
    if b == 4:                                  # Если число угадано
        print('Вы победили за', n, 'ходов')     # Победа
        break                                   # Выход из игры