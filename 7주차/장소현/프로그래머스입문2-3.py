# 컨트롤 제트
def solution(s):
    answer = 0
    arr = s.split()

    for i in range(len(arr)):
        # 문자열에 있는 숫자를 차례대로 더하기
        if arr[i] != 'Z':
            answer += int(arr[i])
        # Z가 나오면 바로 전에 더했던 숫자 빼기
        else:
            answer -= int(arr[i - 1])

    return answer

# 배열 원소의 길이
def solution(strlist):
    answer = []

    # strlist 각 원소의 길이를 배열에 담기
    for str in strlist:
        answer.append(len(str))

    return answer

# 중복된 문자 제거
def solution(my_string):
    answer = ''

    # my_string에서 중복된 문제를 제거
    for i in my_string:
        if i not in answer:
            answer += i

    return answer

# 삼각형의 완성조건(1)
def solution(sides):
    i, j, k = sorted(sides)

    # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다.
    return 1 if k < (i + j) else 2

# 가까운 수
def solution(array, n):
    answer = 0
    array.sort()
    d = 101

    for i in array:
        if d > abs(i - n):
            d = abs(i - n)
            answer = i

    return answer

# 369게임
def solution(order):
    answer = 0

    # 3, 6, 9의 개수만큼 박수를 치는 게임
    for i in list(str(order)):
        if i in ['3', '6', '9']:
            answer += 1

    return answer

# 암호 해독
def solution(cipher, code):
    answer = ''

    # 문자열에서 code의 배수 번째 글자만 진짜 암호
    for i in range(code, len(cipher) + 1, code):
        answer += cipher[i - 1]

    return answer

# 대문자와 소문자
def solution(my_string):
    answer = ''

    # 대문자는 소문자로, 소문자는 대문자로 변환하기
    for i in my_string:
        answer += (i.lower() if i.isupper() else i.upper())

    return answer