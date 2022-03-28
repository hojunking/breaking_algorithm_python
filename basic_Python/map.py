# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int,a))
# print(a)

# b = list(map(str, range(10))) # str로 저장
# print(b) #'1','2' 형식으로 나온다

#int를 추가해서 자료형을 정할 수 있다.
# a,b = map(int, input('숫자 두 개를 입력하세요 : ').split())

# print(a+b)

#공백이 아닌 콤마를 기준으로 분리
a,b = map(int, input('숫자 두 개를 입력하세요: ').split(','))

print(a+b)