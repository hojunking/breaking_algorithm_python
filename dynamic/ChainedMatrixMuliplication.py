
from re import I
#chained matrix multiplication

INF = 99999

def minimum(i,j,d,M):
    minValue, minK =INF, -1
    for k in range(i,j):
        value = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
        if minValue > value:
            minValue, minK = value,k
    return minValue,minK

def minMult(n,d): #make matrix, chained, multiplication
    M = [[0] * (n+1) for _ in range(n+1)] # set matrix 0
    P = [[0] * (n+1) for _ in range(n+1)]
    for diagonal in range (1,n): #1~n-1 input matrix 
        for i in range (1,n-diagonal+1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(i,j,d,M)
    return M,P

def printMatrix(M):
    for i in range(1, len(M)):
        for j in range(i, len(M[i])):
            if j < len(M[i])-1:
                print(M[i][j], end=" ")
            else:
                print(M[i][j])

def order(i,j,P):
    if i==j:
        return "(A" + str(i) + ')'
    else:
        return '(' + \
                order(i, P[i][j],P) + \
                order(P[i][j] +1,j,P) + \
                ')'

n = int(input())
d = list(map(int, input().split())) #default " "
M,P = minMult(n,d)
printMatrix(M)
printMatrix(P)
print(M[1][n])
print(order(1,n,P))

