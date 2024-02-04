# 두 수의 합
def solution(num1, num2):
    answer = -1
    answer = num1 + num2
    return answer


# 두 수의 차 
def solution(num1, num2):
    answer = 0
    answer = num1 - num2
    return answer

# 두 수의 곱
def solution(num1, num2):
    answer = 0
    answer = num1 * num2
    return answer

# 몫 구하기
def solution(num1, num2):
    answer = 0
    answer = num1 // num2
    return answer


# 두 수의 나눗셈 - 이거 한번 더
def solution(num1, num2):
    answer = 0
    answer = ((num1 / num2) * 1000) // 1
    return answer

# 숫자 비교하기 - 파이썬 삼항연산자 구조
def solution(num1, num2):
    answer = 0
    answer = 1 if num1 == num2 else -1
    return answer

# 분수의 덧셈 - gcd 구현해보기
import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    result_numer = numer1 * denom2 + numer2 * denom1
    result_denom = denom1 * denom2
    gcd = math.gcd(result_numer, result_denom)
    answer = [result_numer // gcd, result_denom // gcd]
    
    
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number*2)
    return answer