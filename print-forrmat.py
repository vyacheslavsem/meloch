import random

for i in range (0,10):
    num = random.randint(0, 10000)/random.randint(1, 10000)
    print(format(num, "10.3f"))