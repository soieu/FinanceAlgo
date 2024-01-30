# 나머지 구하기
def solution(num1, num2):
    answer = -1
    answer = num1 % num2
    return answer

# 중앙값 구하기
def solution(array):
    answer = 0
    answer = sorted(array)[len(array) // 2]
    return answer

# 최빈값 구하기 -- 너무 엉망으로 푼 느낌
def solution(array):
    answer = 0
    dict = {}
    
    # 최빈 딕셔너리 저장
    for i in array:
        if dict.get(i, -1) == -1 :
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
        
    # 최빈값 구하기
    maxNum = 0
    target = 0
    count = 0
    for key, value in dict.items():
        if maxNum == value:
            count = 1
        elif maxNum < value:
            maxNum = max(maxNum, value)
            target = key
            count = 0
    if count == 1:
        return -1
    answer = target
    return answer

# 짝수는 싫어요 

# 아래가 좀 더 파이써닉한 코드같아용..
# def solution(n):
#     return [x for x in range(n + 1) if x % 2]

def solution(n):
    answer = []
    i = 1
    while i <= n:
        answer.append(i)
        i = i + 2
    return answer


# 피자 나눠 먹기 (1)
def solution(n):
    answer = 0
    answer = n // 7 + (0 if n % 7 == 0 else 1)
    return answer


# 피자 나눠 먹기 (2) - lcm 관련해서 더 공부
import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(n):
    answer = 0
    answer = lcm(n,6) // 6
    return answer

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = 0
    answer = (n-1) // slice + 1
    return answer

# 배열의 평균값
def solution(numbers):
    sum = 0 
    for i in numbers:
        sum += i 
    answer = sum / len(numbers)
    return answer
