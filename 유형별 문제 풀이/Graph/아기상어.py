# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

# 3
# 0 0 0
# 0 0 0
# 0 9 0

def bfs(start_x,start_y,size,N,map):
    
    direction = [(-1,0),(0,-1),(1,0),(0,1)]
    visited = [[False] * N for i in range(N)]
    queue = deque([(start_x,start_y,0)])
    visited[start_x][start_y] = 0
    fishes = []
    
    while queue:
        cur_x,cur_y,dist = queue.popleft()
        for dx,dy in direction:
            next_x,next_y = cur_x+dx,cur_y+dy
            if 0<=next_x<N and 0<=next_y<N and not visited[next_x][next_y]:
                if map[next_x][next_y] <= size:
                    visited[next_x][next_y] = True
                    if 0 < map[next_x][next_y] < size:
                        fishes.append((dist + 1 ,next_x,next_y))
                    queue.append((next_x,next_y,dist + 1))
    
    if fishes:
        fishes.sort()
        return fishes[0]
    
    return -1


def solution(feed,N):
    first_check = 0
    size = 2
    eat = 0
    answer = 0
    
    start_x = 0
    start_y = 0
    shark_x = 0
    shark_y = 0
    
    # 시작 지점 착기
    for x in range(N):
        for y in range(N):
            if feed[x][y] < size and feed[x][y] != 0:
                first_check += 1
                
            if feed[x][y] == 9:
                start_x = x
                start_y = y
                feed[x][y] = 0
                
    # 첫 순회에서 모든 값이 2보다 크면 먹을 수 있는 것 X
    if first_check == 0:
        return 0
    
    while True:
        result = bfs(shark_x,shark_y,size,N,feed)
        if result == -1:
            return answer
        
        dist, fish_x,fish_y = result
        feed[fish_x][fish_y] = 0
        shark_x,shark_y = fish_x,fish_y
        answer += dist
        eat += 1
        
        if eat == size:
            size += 1
            eat = 0

N = int(sys.stdin.readline().strip())
feed = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
        
print(solution(feed, N))


    

