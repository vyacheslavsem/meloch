if 2 > 3:
    print("Да, так и есть")
else:
    print("Нет, не так")
    

print(2>3)
print(12>3)


if False:
    print("Ложь")
else:
    print("Истина")

num = int(input("Enter a number:"))

if num == 1:
    print("One")
    
elif num == 2:
    print("Two")
    
elif num == 3:
    print("Three")
    
elif num == 4:
    print("Four")
    
elif num == 5:
    print("Five")
    
else:
    print("Number is large")
    
if num in range(1,6):
    print("Podhodit")
else:
    print("Ne podhodit")
    
a1 = range(ord("A"), ord("Z")+1)
a2 = range(ord("a"), ord("z")+1)
a3 = range(ord("0"), ord("9")+1)

symbol = input("enter symbol:")

if ord(symbol) in a1:
    print("ЗАГЛАВНАЯ")
elif ord(symbol) in a2:
    print("строчаня")
elif ord(symbol) in a3:
    print("цифра")
else:
    print("Неизвестный символ")
    
          