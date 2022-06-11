import math

def findPrimeNumber(f,n):
    sieve =[1] * (n+1)
    sieve[1] = 0
    
    m = int(n **0.5) #math.floor(math.sqrt(n+1)) # 
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j] =0
            
    #print([i for i in range(f,n) if sieve[i] == 1])
    
    for i in range(f, n+1):
        if sieve[i]:
            print(i)        

a,b = map(int, input().split())   
findPrimeNumber(a,b)
