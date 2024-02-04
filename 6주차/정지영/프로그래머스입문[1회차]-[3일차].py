# 1. 옷가게 할인 받기
def solution(price):
    
    if price >= 500000 :
        rate = (price*0.2)
        price = price - rate
        
    elif (price >= 300000):
        rate = (price*0.1)
        price = price - rate

    elif price >= 100000 :
        rate = (price*0.05)
        price = price - rate
        
    return int(price)
        
# 2. 아이스 아메리카노
def solution(money):
    
    # 몫, 나머지 구하기
    a = money // 5500
    b = money % 5500
    
    return [a, b]

# 3. 나이 출력
def solution(age):
    return (2022 - age + 1)

# 4. 배열 뒤집기
def solution(num_list):
    
    a = num_list[::-1]
    return a

# 5. 문자열 뒤집기
def solution(my_string):
    return (my_string[::-1])

# 6. 직각삼각형 출력하기
n = int(input())

for i in range(1, n+1):
    print("*"*i)

# 7. 짝수 홀수 개수
def solution(num_list):
    
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return [even, odd]

# 8. 문자 반복 출력하기
def solution(my_string, n):
    
    ans = ''
    for s in my_string:
        ans += s * n
        
    return ans
    
    