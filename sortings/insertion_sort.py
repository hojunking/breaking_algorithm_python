

import random

def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1],list[j]
    return list

list = random.sample(range(10),10)

print('before')
print(list)

print('after')
print(insertion_sort(list))