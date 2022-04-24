
n,k,m =map(int ,input().split())


A = [[]for _ in range (1,n+1)]
for i in range(1,n+1):
    A[i] = list(map(int, input().split()))

B = [list(map(int, input().split())) for _ in range(1,m+1)]
C = [[]for _ in range(1,n+1)]

for i in range (1,n+1):
    for j in range (1,k+1):
        for t in range (1,m+1):
            C[i][j] += A[i][j] * B[j][k]

print(C)