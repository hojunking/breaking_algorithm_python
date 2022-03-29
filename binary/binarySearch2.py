


def binarySearch(n,S,x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2;
        if x == S[mid]:
            return mid
        elif x > S[mid]:
            low = mid +1
        else :
            high = mid -1
    return "not found"

n = int(input('리스트의 크기 : '))
S = list(map(int, input('리스트 값 : ').split())) 
x = int(input('찾을 값 : '))
location = binarySearch(n,S,x)
print('{}'.format(location))
    
    