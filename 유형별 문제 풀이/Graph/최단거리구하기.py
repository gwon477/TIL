from collections import deque

def solution(maps):
    
    result = -1
    
    row = len(maps)
    col = len(maps[0])
    
    if maps[0][0] != 1:
        return result
    
    
    visited = [[False]*col for _ in range(row)]
    
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    
    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = True
    
    while queue:
        cur_x, cur_y, cur_len = queue.popleft()
        if cur_x == row -1 and cur_y == col-1:
            result = cur_len
            break
        
        for dx,dy in delta:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if maps[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    queue.append((next_x,next_y,cur_len+1))
                    visited[next_x][next_y] = True
                    
    return result

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))