def solution(numbers):    
    numbers = list(map(str, numbers))

    # numbers 역순으로 정렬 = 가장 큰 수
    numbers.sort(key=lambda x:x*3, reverse=True)

    # 반례 [0, 0, 0] / "0"
    return str(int(''.join(numbers)))