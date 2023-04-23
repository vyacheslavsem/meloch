import random

sss=str()
for i in range(0,30):
    sss += chr(random.randint(ord("A"), ord("Z")))
print(sss, len(sss))

sss_backword = str()
for i in range(29,-1,-1):
    sss_backword += sss[i]
print(sss_backword)

print(sss[::-1])

print(sss[0:5:2])

num = random.randint(10000,99999)
num = str(num)
print(num,num[2])

print(sss)
print(sss[4:11])
print(sss[4:11:3])
print(sss[10:3:-1])
print(sss[10:3:-3])


l = list(sss)
print(l)
print("длина строки" , len(l))
s=set(l)
print("строка состоит из " , len(s), "уникальных символов")
print("Это символы " , s)