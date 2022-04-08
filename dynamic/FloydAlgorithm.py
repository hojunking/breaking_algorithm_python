#c++ 소스로 파이썬 할 예정!

def floyd2 (n,W,D,P):
    for i in range (1,n+1):
        for j in range (1,n+1):
            D[i][j] = W[i][j]
            P[i][j] = 0
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range (1,n+1):
                if(D[i][j] > D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] =k