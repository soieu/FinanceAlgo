# 1. 특정 문자 제거하기
def solution(my_string, letter):
    
    ans = ''
    for s in my_string:
        if s in letter:
            continue
        else:
            ans += s
            
    return (ans)

# 2. 각도기
def solution(angle):
    
    if 0 < angle < 90:
        return 1
    
    elif angle == 90:
        return 2
    
    elif 90 < angle < 180:
        return 3
    
    else:
        return 4
    

# 3. 양꼬치
def solution(n, k):
    service = n // 10

    return 12000 * n + 2000 * k - 2000 * service

# 4. 짝수의 합
def solution(n):
    
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
            
    return (sum)

# 5. 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:(num2+1)]

# 6. 외계행성의 나이
def solution(age):
    
    dic = {}
    alphbet = ['a','b','c','d','e'
               ,'f','g','h','i','j'
               ,'k','l','m','n','o'
               ,'p','q','r','s','t'
               ,'u','v','w','x','y',
               'z']
    
    for idx, a in enumerate(alphbet):
        dic[idx] = a
        
    ans = ''
    for i in str(age):
        ans += (dic[int(i)])
    
    return (ans)

# 7. 진료순서 정하기
def solution(emergency):
    
    sort_em = sorted(emergency, reverse=True)
    
    ans = []
    for i in emergency:
        ans.append(sort_em.index(i)+1)

    return ans

# 8. 순서쌍의 개수
def solution(n):
    
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    return (c)
