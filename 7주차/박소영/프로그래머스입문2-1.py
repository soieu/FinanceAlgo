#개미 군단
def solution(hp):
    answer = 0
    ants = [5, 3, 1]
    for ant in ants:
        answer = answer + hp // ant
        hp = hp % ant
    return answer

#모스부호 (1)
def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    for code in letter.split(' '):
        answer += morse[code]
    return answer

#가위 바위 보
def solution(rsp):
    answer = ''
    dic = {'2' : '0', '5' : '2', '0' : '5'}
    for one in rsp:
        answer += dic[one]
    return answer

#구슬을 나누는 경우의 수
import math

def solution(balls, share):
    answer = 0
    answer = math.comb(balls, share)
    return answer

#점의 위치 구하기
def solution(dot):
    answer = 0
    
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer

#2차원으로 만들기
def solution(num_list, n):
    answer = []
    
    part = []
    count = 0
    for nn in num_list:
        if count == n:
            answer.append(part)
            part = []
            count = 0
        part.append(nn)
        count += 1
    answer.append(part)
    return answer

#공 던지기
def solution(numbers, k):
    answer = 0
    multiply_numbers = numbers * (k // (len(numbers)//2) + 1)
    print(multiply_numbers)
    pingpong = multiply_numbers[::2]
    answer = pingpong[k -1 ]
    return answer

#배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right":
        last = numbers.pop()
        numbers.insert(0, last)
        answer = numbers
    else:
        first = numbers[0]
        numbers.remove(first)
        numbers.append(first)
        
        answer = numbers
    
    return answer


