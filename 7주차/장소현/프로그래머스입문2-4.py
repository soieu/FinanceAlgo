# 영어가 싫어요
def solution(numbers):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in num.keys():
        numbers = numbers.replace(i, num[i])

    return int(numbers)

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    string = list(my_string)
    # my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾸기
    string[num1], string[num2] = string[num2], string[num1]

    return ''.join(string)

# 한 번만 등장한 문자
def solution(s):
    answer = ''.join(sorted([c for c in s if s.count(c) == 1]))

    return answer

# 약수 구하기
from math import sqrt


def solution(n):
    answer = []

    # 약수
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            answer.append(i)
            if i == n / i:
                continue
            answer.append(n / i)

    # 약수 정렬하기
    answer.sort()

    return answer

# 편지
def solution(message):
    # 글자 한 자를 2cm 크기로 적기
    return len(message)*2

# 가장 큰 수 찾기
def solution(array):
    x = max(array)
    y = array.index(x)

    return [x, y]

# 문자열 계산하기
def solution(my_string):
    return eval(my_string)

# 배열의 유사도
def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)

    return len(s1 & s2)