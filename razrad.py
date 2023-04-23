num = input("Введите число: ")
m=int(input("Введите разряд: "))

l = len(num)
num = int(num)

if m > l:
    print("Разрядность числа ", l, "Вы ввели слишком большую разрядность")
else:
    tails = num % 10**(m-1)
    print("Хвосты разрядв ", m,": ", tails)
    
    heads = num // 10**m
    print("Головы разрядв ", m,": ", heads)
    
    print("Без хвостов: ", num - tails)
    
    print("Без хвостов: ", num - heads*10**m)
    
    print("Без головы и хвоста: ", num - heads*10**m-tails)
    
    print("Рязряд ", m, ": ", int((num -heads*10**m -tails)/10**(m-1)))