
from re import I

global cnt
cnt =0

def merge(left,right):
    low  = high =0
    temp = []
    while (low < len(left)) and (high < len(right)):
        if left[low] < right[high]:
            temp.append(left[low])
            low +=1
        else:
            temp.append(right[high])
            high +=1
    if low < len(left):
        temp += left[low:]
    if high < len(right):
        temp += right[high:]
    return temp
    
    

def mergeSort(data):
    global cnt
    cnt +=1
    if len(data) < 2:
        return data
    
    mid = len(data) //2
    #(left+right) /2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    return merge(left, right)

n = int(input()) #배열 크기
data = list(map(int,input().split()))
# data = [int(x) for x in input().split()]
#for x in input().split(): data.append(int(x))
data = mergeSort(data)
print(cnt//2)
for i in range(0,n):
    if(i < n-1):
        print(data[i], end=" ")
    else: print (data[i])
