import random

def merge_sort(list):
    if len(list) < 2 :
        return list
    
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    
    return merge(left, right)
        
def merge(left, right):
    help = []
    low, high = 0,0

    while low < len(left) and high < len(right):
        if left[low] > right[high]:
            help.append(right[high])
            high += 1
        else: 
            help.append(left[low])
            low +=1 
    
    while(low < len(left)):
        help.append(left[low])
        low += 1
    
    while(high < len(right)):
        help.append(right[high])
        high += 1
        
    return help

list = random.sample(range(10),10)
print("before")
print(list)

print("after")
print(merge_sort(list))