
# 옷가게 할인 받기
def solution(price):
    answer = 0
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    return int(answer)

# 아이스 아메리카노
def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer

# 나이 출력
def solution(age):
    answer = 0
    answer = 2022 - age + 1
    return answer

# 배열 뒤집기
def solution(num_list):
    answer = []
    answer = list(reversed(num_list))
    return answer

# 문자열 뒤집기
def solution(my_string):
    answer = ''
    answer = ''.join(reversed(my_string))
    return answer

# 직각삼각형 출력하기
n = int(input())

for i in range(n):
    for ii in range(1, i+2):
        print("*", end='')
    print()
# 짝수 홀수 개수
def solution(num_list):
    answer = [0, 0]
    
    for i in num_list:
        if i % 2 == 0 : answer[0] = answer[0] + 1
        else : answer[1] = answer[1] + 1
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        for j in range(n):
            answer += i
    return answer

