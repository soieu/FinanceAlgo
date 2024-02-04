# 1. 나머지 구하기
def solution(num1, num2):
    return num1 % num2

# 2. 중앙값 구하기
def solution(array):
    
    array.sort()
    
    n = int((len(array)+1) / 2)
    return array[n-1]

# 3. 최빈값 구하기
def solution(array):
    
    m = {}
    for a in array:
        if a not in m:
            m[a] = 1
        else:
            m[a] += 1
    
    
    # 최빈값 반환
    c = 0
    for i,j in m.items():
        if j == max(m.values()):
            c += 1
    
    if c == 1:
        return [k for k,v in m.items() if v == max(m.values())][0]
    else:
        return -1
    
# 4. 짝수는 싫어요
def solution(n):
    ans = []
    
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        else:
            ans.append(i)
            
    return ans

# 5. 피자 나눠 먹기 (1)
def solution(n):
    
    for i in range(1, n+1):
        if 7 * i >= n:
            return i
            break

# 6. 피자 나눠 먹기 (2)
def solution(n):
    for i in range(1, n+1):
        if (6*i) % n == 0:
            return i
        else:
            continue

# 7. 피자 나눠 먹기 (3)
def solution(slice, n):
    for i in range(1, n+1):
        if slice*i // n >= 1:
            return i
            break

# 8. 배열의 평균값
def solution(numbers):
    return sum(numbers) / len(numbers)
