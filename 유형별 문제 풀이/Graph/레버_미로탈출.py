# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# S : 시작 지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽

from collections import deque

def bfs(maps,Start,Escape,Pass):
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    visited = [[False] * len(maps[0]) for i in range(len(maps))]

    # 시작 지점 부터 레버까지 찾기
    queue = deque([Start])
    start_x,start_y,start_cost = Start
    visited[start_x][start_y] = True

    while queue:
        cur_x,cur_y,cur_cost = queue.popleft()
        for dx,dy in directions:
            nx,ny = cur_x + dx, cur_y + dy
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]) and not visited[nx][ny]:
                if maps[nx][ny] == Escape:
                    return cur_cost + 1
                if maps[nx][ny] in Pass:
                    queue.append((nx,ny,cur_cost + 1))
                    visited[nx][ny] = True
    return 0

                
def solution(maps):
    answer = 0
    
    # 시작 지점 찾기
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'S':
                Start = (x,y,0)
            elif maps[x][y] == 'L':
                Lever = (x,y,0)
                
    # 시작 지점부터 레버까지 최단경로 구하기
    STL = 0
    LTE = 0
    
    STL += bfs(maps, Start,'L',('S','E','O'))
    
    if STL != 0 :
        # 레버부터 도착 지점까지 최단경로 구하기
        LTE += bfs(maps, Lever,'E',('L','S','O'))
        if LTE == 0:
            return -1
        else:
            answer = STL + LTE
    else:
        return -1
    
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
