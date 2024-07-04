# TestCase 
# 6 5 2
# 3 7 10 13 17 20
# 1 10
# 3 9
# 4 23
# 12 19
# 3 15

# TestCase 
# 10 6 0
# 1 5 10 20 29 40 55 64 71 79
# 7 60
# 20 77
# 1 21
# 5 53
# 10 71
# 22 27

import sys

N,Q,K=map(int,sys.stdin.readline().split())
system = list(map(int,sys.stdin.readline().split()))
numbers = [list(map(int,sys.stdin.readline().split())) for i in range(Q)]


def solution(system,numbers,K):
    answer = 0
    
    system_used = {}

    for _ in system:
        system_used[_] = 0
    
    for num in numbers:
        for target in system:
            if num[1] < target:
                break
            if num[0] <= target and num[1] >= target:
                system_used[target] += 1
    
    sorted_system_used = sorted(system_used.items(), key=lambda item:(item[1],-item[0]))
    
    if K == 0:
        pass
    else:
        del sorted_system_used[-K:]
    answer = sorted_system_used[-1][0]
    
    return answer

print(solution(system,numbers,K))