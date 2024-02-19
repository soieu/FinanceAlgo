#컨트롤 제트
def solution(s):
    answer = 0
    
    num = 0
    pre_num = 0
    minus = 1
    for i in s:
        if i >= '0' and i <= '9':
            num *= 10
            num += int(i)
        if i == '-':
            minus *= -1
        if i == 'Z':
            answer -= pre_num
        if i == ' ' and num != 0: 
            answer += num * minus
            #변수들 초기화
            pre_num = num * minus
            num = 0
            minus = 1
    answer += num * minus
            
    
    return answer

#배열 원소의 길이
def solution(strlist):
    answer = []
    for str in strlist:
        answer.append(len(str))
    return answer

#중복된 문자 제거
def solution(my_string):
    answer = ''
    answer = ''.join(dict.fromkeys(my_string))
    return answer


#삼각형의 완성조건 (1)
def solution(sides):
    answer = 2
    sides.sort()
    if sides[2] - sides[1] - sides[0] < 0:
        answer = 1
    return answer


#가까운 수
def solution(array, n):
    answer = 0
    array.sort()
    minv = 200
    for i in array:
        if abs(n-i) < minv:
            answer = i
            minv = abs(n-i)
        elif abs(n-i) == minv and answer != i:
            break
        
    return answer

#369게임
def solution(order):
    answer = 0
    order = str(order)
    
    answer = order.count("3") +order.count("6") + order.count("9")
    return answer


#암호 해독
def solution(cipher, code):
    answer = ''
    
    answer = cipher[code-1::code]
    return answer


#대문자와 소문자
def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - ord("a") + ord("A"))
            answer += ch
        else:
            ch = chr(ord(ch) + ord("a") - ord("A"))
            answer += ch
            
    return answer

