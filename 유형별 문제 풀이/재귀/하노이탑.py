# https://school.programmers.co.kr/learn/courses/30/lessons/12946


def solution(n):
    answer = []
    
    def hanoi(N,start,end,sub):
        if N == 1:
            answer.append([start,end])
            return
        else:
            hanoi(N-1,start,sub,end)
            answer.append([start,end])
            hanoi(N-1,sub,end,start)
            return answer
        
    answer = hanoi(n,1,3,2)
    
    return answer

print(solution(2))
