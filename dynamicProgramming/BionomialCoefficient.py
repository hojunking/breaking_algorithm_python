
#이항계수 최적화 알고리즘
def bin3(n,k,MAX):
    if(k > n //2):
        k = n -k
        
    B = [0]*(k +1) #크기가 k인 배열에 값을 0으로 초기화
    B[0] =1
    
    for i in range(1, n+1):
        j = min(i,k)
        while (j > 0):
            B[j] = (B[j] + B[j-1]) % MAX
            j-=1
    return B[k]


n,k,MAX = map(int,input().split()) #정수 한꺼번에 받기
#print("{0} + {1} ={2}".format(n,k, n+k))
print(bin3(n,k,MAX))