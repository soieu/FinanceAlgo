#6주차
#1. 두 수의 합
def solution(num1, num2):
    return num1+num2
    
#2. 두 수의 차
def solution(num1, num2):
    return num1 - num2
    
#3. 두 수의 곱
def solution(num1, num2):
    return num1*num2

#4. 몫 구하기
def solution(num1, num2):
    return num1 // num2
#이때 몫(//), 나누기(/), 나머지(%)

#5. 두 수의 나눗셈
def solution(num1, num2):
    return int(num1/num2*1000)
    
#6. 숫자 비교하기
def solution(num1, num2):
    return 1 if(num1==num2) else -1

#7. 분수의 덧셈(모르겠음)
def solution(numer1, denom1, numer2, denom2):
    #두 분수를 더한값을 "기약분수"로 나타냈을때
    #기약분수 == 더이상 나눌 수 없는 ...
    #**분모들의 최대공약수를 분모로하고.. 1~분모 나눠보기?
    import math
    def solution(numer1, denom1, numer2, denom2):
        bunmo = denom1*denom2
        bunja = numer1*denom2 + numer2*denom1
    
        gcd = math.gcd(bunmo, bunja)
        return [bunja//gcd, bunmo//gcd]
    
#8. 배열 두 배 만들기
def solution(numbers):
    return [i*2 for i in numbers]