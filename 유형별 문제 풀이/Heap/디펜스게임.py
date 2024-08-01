from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i

    return len(enemy)

print("answer :", solution(7,3,[4, 2, 4, 5, 3, 3, 1]))
#print("answer :", solution(2,4,[3, 3, 3, 3]))
# n	k	enemy	result
# 7	3	[4, 2, 4, 5, 3, 3, 1]	5
# 2	4	[3, 3, 3, 3]	4