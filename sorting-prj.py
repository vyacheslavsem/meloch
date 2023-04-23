import random

unsort=[5,6,2,1,7,9,5,4,3]
print("Есть список из ", len(unsort), "чисел")
print(unsort)

unsort0 = list() #Создаем пустой список


print(unsort0)

unsort0 += unsort

print(unsort0)

count=1

for i in range(len(unsort)):
    for j in range(i+1, len(unsort)):
        if unsort[i] > unsort[j]:
            unsort[i], unsort[j] = unsort[j], unsort[i]
        count+=1
        
print("Отсортированная последовательность:")
print(unsort)

print("Алгоритм отработал ", count, "раз")
print(unsort0)

print("временно отсортировали ", sorted(unsort))

unsort0.sort()
print("Отсортированная последовательность ", unsort0)

nums = list([0])*10
print(nums)

for i in range(0,10):
    nums[i] = str(random.randint(1, 10000))
    print(nums[i], end = " ")
    
print()
print(nums)

nums.sort()
for i in range(0,10):
    print(format(int(nums[i]), "10d"))
    