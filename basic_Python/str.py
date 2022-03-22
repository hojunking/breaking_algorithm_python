#str

s ='101100011'
cnt = 0
for i in s:
    if i == '1':
        cnt +=1
print('1은 %d개입니다.'%cnt)
print('1은 {}개입니다.'.format(cnt))

print('test1 : {}, test2 : {}, test3 : {}'.format(
    '인덱스1','인덱스2','인덱스 3'))

print('test1 : {1}\n, test2 : {0}\n, test3 : {2}\n'.format(
    '인덱스1','인덱스2','인덱스 3'))
#다음과 같이 \n 개행이 가능하고, 인덱스 번호에 foramtting시킬 수 있다.
a = '나는 첫번째'; b='난 두번째'; c='난 세번째'
print(f"인덱스 1:{a}, 인덱스 2:{b}, 인덱스 3:{c}")
#print(f"~~{변수}") 방식으로 변수를 바로 넣어서 출력 가능

#왼쪽 정렬
print('this is {0:<10} | done {1:<5} |'.format('left','a'))
#오른쪽
print('this is {0:>10} | done {1:>5} |'.format('right','b'))
#센터
print('this is {0:^10} | done {1:^5} |'.format('center','c'))

#공백에 값 채우기 ^ 앞에 .을 넣어서 .으로 공백을 채운다
print('this is {0:.^10} | done {1:.^5} |'.format('center','c'))