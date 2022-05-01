import math

def calc(X,aveX,Y,aveY):
    son =0
    mon =0
    for i in range(0,len(X)):
        son +=  (X[i] - aveX)*(Y[i]-aveY)
        mom += math.pow(X[i] - aveX,2)
    
    return son // mom

X = list(map(int, input().split()))
Y = list(map(int, input().split()))
aveX = sum(X)/len(X)
aveY = sum(Y)/len(Y)
 
result =calc(X,aveX,Y,aveY)

print(result)
