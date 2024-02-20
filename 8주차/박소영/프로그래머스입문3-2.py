# 7의 개수
def solution(array):
    answer = 0
    for i in array:
        while i > 0:
            if (i % 10) == 7:
                answer += 1
            i //= 10
            
    return answer

# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    while my_str:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer

# 중복된 숫자 개수
def solution(array, n):
    answer = 0

    for i in array:
        if i == n:
            answer += 1
    return answer

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer+=1
    return answer

# 직사각형 넓이 구하기
def solution(dots):
    answer = 0
    x = -256
    xx = 256
    y = -256
    yy = 256
    for i in dots:
        x = max(x, i[0])
        xx = min(xx, i[0])
        y = max(y, i[1])
        yy = min(yy, i[1])
        
    answer = abs(x - xx) * abs(y - yy)
    return answer

# 캐릭터의 좌표
#   위 아래 오른 왼
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(keyinput, board):
    answer = []
    limitx = board[0]//2
    limity = board[1]//2
    boards = [0,0]
    for i in keyinput:
        if i == 'left' and boards[0] + dx[3] >= limitx * -1 :
            boards[0] += dx[3]
            boards[1] += dy[3]
        elif i == 'right' and boards[0] + dx[2] <= limitx:
            boards[0] += dx[2]
            boards[1] += dy[2]
        elif i == 'up' and boards[1] + dy[0] <= limity:
            boards[0] += dx[0]
            boards[1] += dy[0]
        elif i == 'down' and boards[1] + dy[1] >= limity * -1:
            boards[0] += dx[1]
            boards[1] += dy[1]
            print(boards)
    answer = boards
    return answer

# 최댓값 만들기 (2)
def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    print(numbers)
    answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    return answer

# 다항식 더하기
# https://asthtls.tistory.com/1573?category=970704 
# 참조했습니다..
def solution(polynomial):
    x, num = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric():
            num += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    x = str(x)
    num = str(num)
    if x == "0" and num == "0":
        return "0"
    if x == "0":
        return num
    if x == "1":
        x = ""
    if num == "0":
        return str(x) + "x"
    return x + "x + " + num
