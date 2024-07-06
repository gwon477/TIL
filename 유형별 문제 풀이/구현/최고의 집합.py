# https://school.programmers.co.kr/learn/courses/30/lessons/12938


def solution(n,s):
    answer = []
    
    if s < n:
        return [-1]
    
    target = s//n
    ano = s%n
    
    answer = [target] * n
    
    for _ in range(ano):
        answer[_] += 1

    answer.sort()
    return answer

print(solution(2,9))

