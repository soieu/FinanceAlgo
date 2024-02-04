def solution(n, times):
    
    # 최소(가능한 최소 시간)/최대(주어진 작업시간 중 가장 큰 값) 범위 설정
    start = 1
    end = max(times)*n
    ans = end
    
    # 이진탐색 : 중간값을 찾아 작은쪽, 큰쪽으로 반을 나눠서 최종적으로 원하는 값에 도달
    while start <= end:
        mid = (start+end) // 2
        
        # mid 시간 동안 각 작업을 처리할 수 있는 사람 수 계산
        poeple = 0
        for time in times:
            poeple += mid//time
            
        # 사람 수에 따른 범위(위치) 조정
        if poeple < n:
            start = mid + 1
        else:
            end = mid - 1
            ans = min(ans, mid)
            
    return ans
            
            
        