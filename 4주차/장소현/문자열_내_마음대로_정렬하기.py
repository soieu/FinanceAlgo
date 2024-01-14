def solution(strings, n):
    # 사전순으로 정렬
    strings.sort()
    
    # 인덱스 n번째 글자를 기준으로 오름차순 정렬
    strings.sort(key=lambda x:x[n])
    
    return strings