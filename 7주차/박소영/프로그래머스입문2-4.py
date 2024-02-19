#영어가 싫어요
def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    while numbers != "":
        for idx, num in enumerate(nums):
            
            if numbers.startswith(num):
                answer *= 10
                answer += idx
                numbers = numbers[len(num):]
    return answer

#인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = my_string[num1]
    strr = list(my_string)
    strr[num1] = strr[num2]
    strr[num2] = answer
    answer = ''.join(strr)
    return answer

#한 번만 등장한 문자
def solution(s):
    answer = ''
    for aph in range(ord('a'), ord('z')+1):
        if s.count(chr(aph)) == 1:
            answer+=chr(aph)
    return answer

#약수 구하기
def solution(n):
    answer = []
    
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

#편지
def solution(message):
    answer = 0
    answer = len(message)*2
    return answer

#가장 큰 수 찾기
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

#문자열 계산하기
def solution(my_string):
    answer = 0
    operand = 0
    sign = 1
    for s in my_string:
        if s >= '0' and s <= '9':
            operand *= 10
            operand += int(s)
            print(operand)
        elif s == '-':
            if operand != 0:
                answer += operand * sign
                operand = 0
            sign = -1
        elif s == '+':
            if operand != 0:
                answer += operand * sign
                operand = 0
            sign = 1
    answer += operand * sign
        
            
            
    return answer


#배열의 유사도
def solution(s1, s2):
    answer = 0
    
    for ss1 in s1:
        if s2.count(ss1):
            answer += 1
    return answer


