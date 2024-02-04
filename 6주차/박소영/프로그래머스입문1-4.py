#특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter,'')
    return answer

#각도기
def solution(angle):
    answer = 0
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    else:
        answer = 4
    return answer

#양꼬치
def solution(n, k):
    answer = 0
    answer = n * 12000 + 2000 * (k - n // 10)
    return answer

#짝수의 합
def solution(n):
    answer = 0
    for i in range(0, n+1 ,2):
        answer = answer + i
    return answer
# sum([i for i in range(2, n + 1, 2)]) 이렇게도 가능!!

#배열 자르기
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1, 1):
        answer.append(numbers[i])
        
    return answer
# return numbers[num1:num2+1] 이렇게도 가능


#외계행성의 나이
def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i) + ord('a'))
    return answer

#진료순서 정하기 - 검색 참조..
def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(temp.index(i)+1)
    return answer

#순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer

