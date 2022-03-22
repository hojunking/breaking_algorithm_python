str = ['songu','janguu','honguuu','king']

str.sort(key=len)

str.append(5) #? char로 들어가는 건가?

for s in str:
    print(s,end=' ')   #길이에 따른 정렬

print()

print('%d에 있구나'%str.index('songu')) #몇 번 인덱스에 있는지 찾아보기

# for t in str[-1:-4] :
#     print(t,end=' ') 이건 안 된다.