# 5 3
# 10 50 20 70 100
# 1 3
# 3 4
# 1 5


# 26.67
# 45.00
# 50.00

# 1 ≤ N ≤ 106 인 정수

# 1 ≤ K ≤ 104 인 정수

# 1 ≤ Si ≤ 100 인 정수

# 1 ≤ Ai ≤ Bi ≤ N

import sys

N,K = map(int,sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

for i in range(K):
    Si,Ai = map(int,sys.stdin.readline().split())
    scores_sec = scores[Si-1:Ai]
    print(format(round(sum(scores_sec)/len(scores_sec),2),".2f"))
    

