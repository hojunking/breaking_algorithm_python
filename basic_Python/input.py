
# a = input('입력하세요 : ')
# print(f'{a} 라고 입력하셨습니다.')

# n = int(input('숫자를 입력하세요 : '))
# print(f'{n} 이라고 입력하셨습니다.')

#split() 이용

a,b  =input('문자열 두 개를 입력하세요: ').split()

print(a) #입력 시 공백을 기준으로 변수에 입력한다.
print(b)

c,d = input('숫자 두 개를 입력하세요:').split()

print(c + d) #int형으로 변환을 하지 않았다.

c=int(c)
d=int(d)
print (c+d)
