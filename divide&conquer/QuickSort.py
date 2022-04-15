

global cnt
cnt =0
def partition(data,low,high):
    global cnt 
    cnt += 1
    pivot =data[low]
    j= low
    
    for i in range(low+1, high+1):
        if (data[i] < pivot):
            j += 1
            data[i],data[j] =data[j], data[i]
    data[low],data[j] = data[j], data[low]
    return j
    

def quickSort(data,low,high):
    if(low < high):
        pivotPoint = partition(data,low,high)
        quickSort(data,low,pivotPoint -1)
        quickSort(data,pivotPoint+1, high)

n = int(input())
data = list(map(int,input().split()))

partition(data,0,n-1)
for i in range(0,n):
    if (i <n-1):
        print(data[i],end=" ")
    else:
        print(data[i], end ="\n")
cnt =0
quickSort(data,0,n-1)
print(cnt)
for i in range(0,n):
    if (i <n-1):
        print(data[i],end=" ")
    else:
        print(data[i], end ="\n")
