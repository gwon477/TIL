# https://www.acmicpc.net/problem/20310

import sys
from itertools import permutations

S = list(sys.stdin.readline())


zeroCnt = S.count('0')
oneCnt = S.count('1')
cnt = 0
for _ in S:
    if cnt == oneCnt//2:
        break
    if _ == '1':
        S.remove(_)
        cnt += 1

cnt = 0
S=S[::-1]
for _ in S:
    if cnt == zeroCnt//2:
        break
    if _ == '0':
        S.remove(_)
        cnt += 1

for _ in S[::-1]:
    print(_,end='')
