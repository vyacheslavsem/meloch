import time
# Эта программа позваляет компьтеру угадать
# загаданное пользователем число с помошью
# алгоритма двоичного поиска

# Введем именованные константы
NUM_MIN = -10**30    # Минимально возможно загаданное число
NUM_MAX = 10**30   # Максимально возможно загаданное число

MSG="Введите загаданное число (от " +\
    str(NUM_MIN) + " до " + str(NUM_MAX) + "):"
    
#gnum = int(input(MSG))
gnum = -889999999997999994799147015487.485321

nmin = NUM_MIN
nmax = NUM_MAX
attempts = 0

t1 = time.time()

while 1:
    guess = (nmax+nmin)/2
    attempts += 1
    print("Может быть", guess, "?..")
          
    if (guess == gnum):
        print("Загаданное число ", guess)
        break
        
    if (guess > gnum):
        print("Ааааа, мое число больше загаданного?..")
        nmax = guess - 1
    else:
        print("Ааааа, мое число меньше загаданного?..")
        nmin = guess + 1

t2 = time.time()

print("Я угадаол загаданное число с ", attempts, "попыток")
print("это заняло",t2-t1,"секунд")
    