
highest = 0
lowest = 99999

n = int(input())

A = list(map(int, input().split()))

for i in range(n):
    if A[i] > highest:
        highest = A[i]
    if A[i] < lowest:
        lowest = A[i]
print(lowest)
print(highest)