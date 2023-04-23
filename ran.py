import random 

for i in range(0, 10):

    num = random.randint(1,6)
    print("random number ", num)

print(chr(70))
print(ord("F"))


string = str()
for i in range(0,100):
    string += chr(random.randint(ord("˧"), ord(" ﻻ")))
print(string, len(string))

string=str(num)
print(string*3)