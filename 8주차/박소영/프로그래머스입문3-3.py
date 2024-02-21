# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    answer = 0
    num = 0
    for i in my_string:
        if i >= '0' and i <= '9':
            num *= 10
            num += int(i)
        else:
            answer+=num
            num = 0
    answer+=num
            
    return answer

# 안전지대
dx=[-1,0,1,-1,1,-1,0,1]
dy=[1,1,1,0,0,-1,-1,-1]
dy
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for k in range(8):
                    if i+dy[k] < len(board) and i+dy[k] > -1 and j+dx[k] < len(board) and j+dx[k] > -1 and board[i+dy[k]][j+dx[k]] != 1:
                        board[i+dy[k]][j+dx[k]] = 2
    print(board)
                        
                        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer += 1
        
    return answer

# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    answer = 2 * min(sides) - 1
    return answer

# 외계어 사전
def solution(spell, dic):
    answer = 2
    
    for i in dic:
        for j in spell:
            if i.count(j):
                print(j, spell[len(spell)-1])
                if j == spell[len(spell)-1]:
                    print(j, spell[len(spell)-1])
                    answer=1
                    continue;
            else:
                break;
    return answer


# 저주의 숫자 3
#https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%80%EC%A3%BC%EC%9D%98-%EC%88%AB%EC%9E%903

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
    return answer

# 평행
temp = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]]

def solution(dots):
    answer = 0
    for i in temp:
        first = i[0]
        sec = i[1]
        # 기울기 비교를 위한 교차 곱 사용
        dx1, dy1 = dots[first[1]][0] - dots[first[0]][0], dots[first[1]][1] - dots[first[0]][1]
        dx2, dy2 = dots[sec[1]][0] - dots[sec[0]][0], dots[sec[1]][1] - dots[sec[0]][1]
        
        # 교차 곱을 이용한 기울기 비교 (dx1*dy2 == dx2*dy1)
        if dx1 * dy2 == dx2 * dy1:
            answer = 1
            break  # 조건을 만족하는 경우 반복문 탈출
    
    return answer


# 겹치는 선분의 길이
# 얘 모르겠어요!!!!!!!!!!!!!!!!!!!

# 유한소수 판별하기
# 얘도 모르겠어요!!!!!!!!!!!!

