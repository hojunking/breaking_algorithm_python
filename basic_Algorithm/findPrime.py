from pickle import TRUE #특정 함수를 불러오기 from pickle 에서
from tkinter import N
import math

def isPrime(n):  #함수 선언
    for i in range(2,math.floor(math.sqrt(n))+1):
        if(n % i==0):
            return False
        else:
            return True
        
n = int(input('숫자를 입력하세요 : '))

is_prime = True
    
if(isPrime(n)): #함수를 호출하고 인자(n)을 넣음
    print(n,'은 소수입니다.')
else:
    print(n,'은 소수가 아닙니다.')
    
