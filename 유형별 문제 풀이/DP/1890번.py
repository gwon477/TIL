N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

# 시작점 초기화
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0 or (i == N-1 and j == N-1):
            continue
        dist = board[i][j]
        if i + dist < N:
            dp[i + dist][j] += dp[i][j]
        if j + dist < N:
            dp[i][j + dist] += dp[i][j]

print(dp[N-1][N-1])