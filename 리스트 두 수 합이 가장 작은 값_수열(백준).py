import sys

N,T = map(int,sys.stdin.readline().strip().split())

numbers = list(map(int,sys.stdin.readline().split()))

def solution(numbers,N,T):
    answer = 0
    start = 0
    end = T
    
    for _ in range(T,N):
        temp = sum(numbers[start:end])
        start += 1
        end += 1
        answer = max(answer,temp)
    
    return answer

print(solution(numbers=numbers, N=N, T=T))