
from re import X
from xml.dom import minidom


def binarySearch(n,S,x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid -1
        else:
            low = mid +1
    return "not exist"

n = int(input('리스트 크기를 정해주세요 : '))
S = list(map(int, input('리스트 값 :').split())) #list 값 넣기
T = int(input('검색 횟수 : '))
for _ in range(T): #T번 돌려서 x값의 위치 찾기
    x = int(input('값 :'))
    location = binarySearch(n,S,x)
    print('위치 : {}'.format(location))
    

