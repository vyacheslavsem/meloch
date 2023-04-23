#Эта программа переводит вводимое число в текст

#Ввод числа
num = input("Введите число (1 99 999):")

# Определеям количество разрядов
l = len(num)
print("Количество рязрядов:" , l)

#Переводим ввод в число int
num = int(num)

# Введем имена чисел и разрядов
n1 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n11 = ['Eleven', 'Twelve', 'Thrirteen', 'Forteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eightyeen', 'Nineteen']
n10 = ['Ten', 'Twenty', 'Thrity', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
nx = [' ', 'Hundreed', 'Thousand', 'Million']

# Определим числа соответствующих разрядов
n = ['']*l
print(len(n),n)

for i in range(0, l):
    tails = num % 10**i
    heads = num // 10**(i+1)
    n[i] = str(int((num - heads*10**(i+1) - tails)/10**i))
    print("Рязряд ", i+1, " :", n[i])

s = str("")

for i in range(l-1,-1,-1):
    if i == 4:
        flag =0
        if n[i] =='1':
            s += n11[int(n[i])]
            s += " Thousands "
            flag = 1
        elif int(n[i])> 1:
            s += n10[int(n[i])-1]
            s += " "
        else:
            continue
    if i == 3:
        if flag == 1:
            continue
        else:
            s += n1[int(n[i])-1]
            s += " Thousands "
            
    if i == 2:
        if n[i] !='0':
            s += n1[int(n[i])-1]
            s += " Hundreds "
        else:
            continue
        if i == 1:
            flag = 0
        if n[i] == '1':
           s += n11[int(n[i])]
           flag = 1
        elif int(n[i]) > 1:
           s += n10[int(n[i])-1]
           s += " "
        else:
           continue

    if i == 0:
       if n[i] !="0":
           s+= n1[int(n[i])-1]
       else:
           continue
            
        
print(s)

    
