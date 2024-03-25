# 1439 번 : 숫자 뒤집기

import sys

S = sys.stdin.readline().strip()

def sol(S):
    cnt = 0
    result = 0
    for i in range(1,len(S)):
        if S[i] != S[i-1]:
            cnt += 1 
    
    if cnt % 2 == 0:
        result = int(cnt/2)
    else:
        result = int((cnt - 1)/2 + 1)
    
    return result

print(sol(S))