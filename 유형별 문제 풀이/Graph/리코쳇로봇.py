from collections import deque

def solution(board):
    answer = 0
    
    R = len(board)
    C = len(board[0])
    
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'R':
                start_x,start_y = x,y
            if board[x][y] == 'G':
                escape_x,escape_y = x,y
                
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
    queue = deque([(start_x,start_y,0)])
    visited = set()
    visited.add((start_x,start_y))
    
    while queue:
        cur_x,cur_y,cur_cost = queue.popleft()
        
        if (cur_x,cur_y) == (escape_x,escape_y):
            return cur_cost
        
        for dx,dy in directions:
            nx,ny = cur_x, cur_y
            while 0 <= nx+dx < R and 0 <= ny+dy < C and board[nx+dx][ny+dy] != 'D':
                nx += dx
                ny += dy
                
            if (nx,ny) not in  visited:
                visited.add((nx,ny))
                queue.append((nx,ny,cur_cost + 1))
        
    return -1



print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	))