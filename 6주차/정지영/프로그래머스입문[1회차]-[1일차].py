# 1. 두 수의 합
def solution(num1, num2):
    return num1 + num2

# 2. 두 수의 차
def solution(num1, num2):
    return num1 - num2

# 3. 두 수의 곱
def solution(num1, num2):
    return num1 * num2

# 4. 몫 구하기
def solution(num1, num2):
    return num1 // num2

# 5. 두 수의 나눗셈
def solution(num1, num2):
    return int((num1 / num2) * 1000)

# 6. 숫자 비교하기
def solution(num1, num2):
    
    if num1 != num2:
        return -1
    else:
        return 1
    
# 7. 분수의 덧셈 🐠
from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    
    f = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [f.numerator, f.denominator]

# 8. 배열 두 배 만들기
def solution(numbers):
    
    ans = [i*2 for i in numbers]
    return ans