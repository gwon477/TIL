import sys
import heapq

N = int(sys.stdin.readline())
l = []
answer = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

for _ in l:
    if _ == 0:
        if len(answer) == 0:
            print(0)
        else:
            print(heapq.heappop(answer))
    else:
        heapq.heappush(answer,_)
    