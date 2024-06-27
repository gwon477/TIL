def dfs(start, end, must_visits, map):
    
    # 시작 노드 혹은 도착 노드가 접근 불가인 경우
    start_row = start[0] - 1
    start_col = start[1] - 1
    end_row = end[0] - 1
    end_col = end[1] -1
    
    if map[start_row][start_col] != 0 or map[end_row][end_col] != 0:
        return 0
    
    # 방향 정의
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    stack = [(start,0,0)]
    rows = len(map)
    cols = len(map[0])
    visited = set()
    
    while stack:
        (row,col),cnt,visited_must_visit = stack.pop()
        
        if (row,col) in visited:
            continue
            
        visited.add((row,col))
        
        if visited_must_visit < len(must_visit) and (row,col) == must_visits[visited_must_visit]:
            visited_must_visit +=1
            cnt += 1
            
            
        if (row,col) == end:
            if visited_must_visit == len(must_visits):
                return cnt
        
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if map[new_row][new_col] == 0 and (new_row,new_col) not in visited:
                    stack.append(((new_row,new_col), cnt+1, visited_must_visit))
    
    return 0

import sys

n,m = map(int,sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,sys.stdin.readline().strip().split())))
    


must_visited = []
for i in range(m):
    a,b = map(int,sys.stdin.readline().strip().split())
    must_visited.append((a,b))


must_visit = must_visited[1:len(must_visited)-1]
print(must_visited[0])
print(dfs(must_visited[0], must_visited[-1], must_visit, map=matrix))
