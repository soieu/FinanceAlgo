def solution(n, times):
    #초기값 설정
    start = 0
    end = max(times)*n
    
    while start <= end:
        mid = (start+end)//2    #어짜피 몫만 필요하니까

        #현재 시간안에 확인가능한 사람수
        people = sum([mid//t for t in times])
        
        if(people < n):
            #이러면 시간을 더 늘려서 더 확인해야함
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer
        