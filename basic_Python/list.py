#리스트에 대해 알아본다.
list1 =[1,2,3,4,5]
list2 =[5,4,3,2,1]

#list1.extend(list2)
list1.append(10);
for i in list1:
    print('{}'.format(i), end =' ')
print()
list1.insert(2,10); #2자리에 넣으면 하나씩 다 밀린다.
for i in list1:
    print('{}'.format(i), end =' ')
print()
#값 2의 인덱스 호출
print( '2의 인덱스 호출 : {}'.format(list1.index(2)))
#리스트 동시 출력
print([list1,list2])
#리스트 속 10의 갯수 찾기
print('10은 몇 개인가요? : {}개!!'.format(list1.count(10)))
#삭제
list1.remove(10)
list1.pop(3)
for i in list1:
    print('{}'.format(i), end =' ')
print()
list1.reverse() #내림차순 정렬
for i in list1:
    print('{}'.format(i), end =' ')
list1.sort() #오름차순 정렬

