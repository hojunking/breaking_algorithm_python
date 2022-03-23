import math

def findPrime(n):
    for i in range(2,math.floor(math.sqrt(n)+1)): #범위 range를 꼭 써줄 것
        if (n % i==0):
            return False
        else:
            return True
list = []

# for i in range(2,101):
#     if(not findPrime(i)):
#         continue
#     else: 
#         list.append(i)

for i in range(2,101): #continue문 사용 필요없이 이렇게 하면 된다
    if(findPrime(i)):
        list.append(i)

print(list)    