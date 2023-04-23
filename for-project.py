import random
sss = "AbraKadajldf"
print("длина строки " , len(sss))
for i in range(0, 12):
    print(sss[i])


for i in range(0, 10):
    print("Значение индекса ", i)
    print("Случайное число ", random.randint(1,10))


for i in range(1,11):
    for j in range(1,11):
        print(i, " x ", j, " = ", i*j)
    print()



for i in range(ord("A"), ord("Z")+1):
    for j in range(ord("A"), ord("Z")+1):
        for k in range(ord("A"), ord("Z")+1):
            print(chr(i), chr(j), chr(k), sep="")