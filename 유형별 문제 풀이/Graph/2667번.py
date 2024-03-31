# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# BFS 풀이
from collections import deque
import sys

N = int(sys.stdin.readline().strip())
grid = []
for i in range(N):
    grid.append(list(sys.stdin.readline().strip()))


num_of_islands = 0

visited = [[False]* N for _ in range(N)]
    
count = []

    
def bfs(x,y):
    visited[x][y] = True
    queue = deque()
    queue.append((x,y))
    cnt = 1
    
    while queue:
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < N:
                if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))
                    cnt += 1
    
    count.append(cnt)
        
for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:
            bfs(i,j)
            num_of_islands += 1  
    
print(num_of_islands)
count.sort()
for _ in count:
    print(_)



# DFS 풀이