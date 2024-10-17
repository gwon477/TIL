import sys

input = sys.stdin.readline()

N = int(input)
print(N)

comu = []

for i in range(N):
    T, P = map(int,sys.stdin.readline().strip().split(" "))
    comu.append((T,P))

start = 0
a = [0 for i in range(N)]

while start<N:
    start_idx = start
    next_idx = start_idx + comu[start_idx][0]
    print("next_idx",next_idx)
    total_sum = comu[start_idx][1]
    while next_idx < N:
        if next_idx + comu[next_idx][0] > N:
            break
        total_sum += comu[next_idx][1]
        next_idx += comu[next_idx][0]
    if next_idx <= N:
        a[start] = total_sum
    start += 1
print(a)
print(max(a))

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200