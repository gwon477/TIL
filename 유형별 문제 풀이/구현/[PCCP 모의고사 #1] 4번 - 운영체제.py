import heapq

def solution(program):
    answer = [0] * 11
    
    program.sort(key= lambda x:x[1])
    
    N = len(program)
    idx = 0
    hq = []
    currnet_time = 0
    
    while idx < N or hq:
        while idx < N and currnet_time >= program[idx][1]:
            heapq.heappush(hq,(program[idx][0],program[idx][1],program[idx][2]))
            idx += 1
        
        if hq:
            priority, call_time, duration = heapq.heappop(hq)
            
            answer[priority] += currnet_time - call_time
            
            currnet_time += duration
        else:
            # 실행할 프로그램이 없다면 현재 시간을 다음 호출 시간으로 이동
            if idx < N:
                currnet_time = program[idx][1]
    
    answer[0] = currnet_time
    
    return answer