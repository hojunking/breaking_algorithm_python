import math

def findPrimeNumber(n):
    list =[]
    for i in range(2,n+1):
        list.insert(i,i)
    for i in range(2,math.floor(math.sqrt(n))+1):
        if(list[i]==0):
            continue
        for j in range(i+i,n+1,i):
            list[j] =0;
    for i in range(2,n+1):
        if(not list[i] == 0):
            print(list[i], end=' ')
    
findPrimeNumber(100)