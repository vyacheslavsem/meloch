import random

def main():
    
    l = [0]*20
    for i in range (len(l)):
        l[i] = random.randint(1,10)
        
    print(l)
    print(l)
    print(l)
    
    
    s = set(l)
    
    print(s)
    
    string = "I do love Python ! Python is a cool language. I will stydy Python"

    print (string)
    print()
    
    slist = string.split(" ")
    
    print(slist)
    print()
    
    sset=set(slist)
    print(sset)
    print()
    
    sdict={}
    for i in sset:
        sdict[i] = 0
        
    print(sdict)
    print()
    
    for i in range(len(slist)):
        sdict[slist[i]] +=1
        
    print(sdict)
    
    l1 = [1,2,3,4,2,3]
    l2 = [4,3,2,1]
    
    s1=set(l1)
    s2 = set(l2)
    
    print(s1 ==s2)
main()
