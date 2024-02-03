#6주차(3차시)
#1. 옷가게 할인받기
def solution(price):
    if(price >= 500000):
        return int(price*0.8)
    elif(price >= 300000):
        return int(price*0.9)
    elif(price >= 100000):
        return int(price*0.95)
    else:
        return price

#2. 아이스아메리카노
def solution(money):
    return [money//5500, money%5500]

#3. 나이 출력
def solution(age):
    return 2022-(age-1)

#4. 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

#5. 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

#6. 직각삼각형 출력하기
n = int(input())
for i in range(n):
    print('*'*(i+1))

#7. 짝수 홀수 개수
def solution(num_list):
    cnt = 0
    for i in num_list:
        if(i%2==0):
            cnt += 1
    return [cnt, len(num_list)-cnt]

#8. 문자 반복 출력하기
def solution(my_string,n):
    result = ''
    for i in my_string:
        result += i*n