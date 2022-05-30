import math

def findPrimeNumber(n):
    sieve =[1] * n
    
    m = math.floor(math.sqrt(n)) # int(n **0.5)
    for i in range(2,m+1):
        if(sieve[i] == 1):
            for j in range(i+i,n,i):
                sieve[j] =0
            
    print([i for i in range(2,n) if sieve[i] == 1])
    
findPrimeNumber(100)
