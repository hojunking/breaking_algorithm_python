
import random
import math

global answer
global count
def isSafe(height):
    if(height < answer):
        return True
    else: return False

def twoEggsDrop(n):
    count = 0
    sqrt_n = math.floor(math.sqrt(n))
    for height1 in range(sqrt_n, n+1, sqrt_n):
        count +=1
        if (not isSafe(height1)):
            break
    for height2 in range(height1 - sqrt_n +1, height1 +1):
        count +=1
        if(not isSafe(height2)):
            return count

n = 100
for answer in range(1,101):
    print(answer, twoEggsDrop(n))