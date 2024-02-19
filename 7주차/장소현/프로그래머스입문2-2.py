# 주사위의 개수
 def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)

# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            # 약수 존재
            if i % j == 0:
                answer += 1
                break

    return answer

# 최댓값 만들기(1)
def solution(numbers):
    # 배열 정렬
    numbers.sort()
    return numbers[-1]*numbers[-2]


# 팩토리얼
def solution(n):
    answer = 1
    m = 1

    # 팩토리얼 구하기
    for i in range(2, 11):
        m *= i

        if m == n:
            return i
        elif m > n:
            return i - 1

    return answer

# 모음 제거
def solution(my_string):
    vowel = ["a", "e", "i", "o", "u"]

    # 모음 제거
    for i in vowel:
        my_string = my_string.replace(i, "")

    return my_string

# 문자열 정렬하기(1)
def solution(my_string):
    answer = []

    # 숫자만 추출
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))

    # 오름차순 정렬
    answer.sort()

    return answer

# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0

    # 자연수를 추출해서 더하기
    for i in my_string:
        if i.isdigit():
            answer += int(i)

    return answer

# 소인수분해
def solution(n):
    answer = []
    m = 2

    while m <= n:
        if n % m == 0:
            if m not in answer:
                answer.append(m)
            n //= m
        else:
            m += 1

    return answer