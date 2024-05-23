#print(1+2+3+4+5 )


# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

#(1,2), (2,1)
print(abs(1-2) + abs(2-1))

#(1,2), (1,4)
print(abs(1-1) + abs(2-4))

#(1,2), (2,3)
print(abs(1-2) + abs(2-3))

#(5,5) ,(5,4)
print(abs(5-5) + abs(5-4))

#(5,5) ,(4,4)
print(abs(5-4) + abs(5-4))

#(5,5) ,(4,5)
print(abs(5-4) + abs(5-5))

import sys

N, M = map(int,sys.stdin.readline().split())

# map 입력받기
m = []
for i in range(N):
    raw = list(map(int,sys.stdin.readline().split()))
    m.append(raw)

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            