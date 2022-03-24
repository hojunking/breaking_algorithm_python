import math

n = 1000
prime = [True for i in range(n+1)] #인덱스 n까지 삽입

print(prime[n+1])

# for i in range(2, int(math.sqrt(n))+1):
#     if prime[i] == True:
#         j = 2
#         while i*j <= n:
#             prime[i*j] =False
#             j +=1

# for i in range(2, n+1):
#     if prime[i]:
#         print(i,end = " ")
        
        