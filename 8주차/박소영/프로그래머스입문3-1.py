
# 숫자 찾기
def solution(num, k):
    answer = 0
    answer = str(num).find(str(k))
    
    if answer != -1:
        answer += 1
        
    return answer

# n의 배수 고르기
def solution(n, numlist):
    answer = [i for i in numlist if i % n == 0]
    return answer


# 자릿수 더하기
def solution(n):
    answer = 0
    for _ in range(n):
        answer += n%10
        n //= 10
    return answer

# OX퀴즈
def solution(quiz):
    answer = []
    
    for str in quiz:
        quiz_list = str.split(' ')
        if quiz_list[1] == '+':
            if int(quiz_list[0])+int(quiz_list[2]) == int(quiz_list[4]):
                answer.append('O')
            else:
                answer.append('X')
        if quiz_list[1] == '-':
            if int(quiz_list[0])-int(quiz_list[2]) == int(quiz_list[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
# 문자열안에 문자열
def solution(str1, str2):
    answer = 2
    for i in range(len(str1)-len(str2)+1):
        if str1[i] == str2[0]:
            for j in range(len(str2)):
                if j == len(str2) -1 and str2[j] == str1[i+j]:
                    answer = 1
    if str1 == str2:
        answer = 1
    return answer

# 제곱수 판별하기
def solution(n):
    answer = 2
    for i in range(n//2):
        if i*i == n:
            answer = 1
    return answer
# 세균 증식
def solution(n, t):
    answer = n
    for _ in range(t):
        answer *= 2
    return answer
# 문자열 정렬하기 (2)
def solution(my_string):
    answer = ''
    answer = my_string.lower();
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer
