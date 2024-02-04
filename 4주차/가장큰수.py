def solution(numbers):
    
    # 리스트 안에 있는 값을 str으로 변환
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x*3) ,reverse=True)

    n = ''.join(numbers)
    
    # [0, 0] => 결과가 0으로 나와야 함
    return str(int(n))