a1 = range(ord("A"),ord("Z")+1)
a2 = range(ord("a"),ord("z")+1)
a3 = range(ord("0"),ord("9")+1)

a1 = list(a1)
a2 = list(a2)
a3 = list(a3)

print(a1, end = " ")
print()
print(a2, end = " ")
print()
print(a3, end = " ")
print()
print(a1+a2+a3, end = " ")
print()

for i in a1 + a2 + a3:
    for j in a1 + a2 + a3:
        if (i in a1 and j in a1) or (i in a2 and j in a2) or (i in a3 and j in a3):
            continue
        for k in a1 + a2 + a3:
            if (i in a1 and k in a1) or (i in a2 and k in a2) or (i in a3 and k in a3):
                continue
            if (j in a1 and k in a1) or (j in a2 and k in a2) or (j in a3 and k in a3):
                continue
            print(chr(i),chr(j),chr(k), sep="", end=" ")