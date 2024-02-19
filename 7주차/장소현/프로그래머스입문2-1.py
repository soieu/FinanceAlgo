# 개미 군단
def solution(hp):
    answer = 0
    # 장군개미
    answer += hp // 5
    hp %= 5
    # 병정개미
    answer += hp // 3
    hp %= 3
    # 일개미
    answer += hp

    return answer

# 모스부호(1)
def solution(letter):
    # 모스부호
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }

    return ''.join(morse[i] for i in letter.split())

# 가위 바위 보
def solution(rsp):
    answer = ''

    # 가위 : 2, 바위 : 0, 보 : 5
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        else:
            answer += "2"

    return answer

# 구슬을 나누는 경우의 수
def solution(balls, share):
    answer = 1

    # 머쓱이가 갖고 있는 구슬의 개수 balls
    # 친구들에게 나누어 줄 구슬 개수 share
    if balls == share:
        return answer

    for i in range(balls, balls - share, -1):
        answer *= i

    for i in range(share, 1, -1):
        answer //= i

    return answer

# 점의 위치 구하기
def solution(dot):
    # 제1사분면
    if dot[0] > 0 and dot[1] > 0:
        return 1
    # 제2사분면
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    # 제3사분면
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    # 제4사분면
    else:
        return 4

# 2차원으로 만들기
def solution(num_list, n):
    answer = []

    # num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경하기
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])

    return answer

# 공 던지기
def solution(numbers, k):
    # 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던진다
    answer = numbers[2*(k-1) % len(numbers)]
    return answer

# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    # 오른쪽으로 배열 회전
    if direction == "right":
        answer = [numbers[-1]] + numbers[:-1]
    # 왼쪽으로 배열 회전
    else:
        answer = numbers[1:] + [numbers[0]]

    return answer