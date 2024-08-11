from collections import deque

def solution(land):
    # Y의 수
    N = len(land[0])
    
    # X의 수
    M = len(land)
    answer = 0
    checked = [[False] * N for i in range(len(land))]
    
    answer_list = []
    
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
    
    def bfs(start_x,start_y):
        print("자원 발견",(start_x,start_y))
        queue =deque([(start_x,start_y)])
        checked[start_x][start_y] = True
        cnt = 1
        col = set()
        while queue:
            c_x,c_y = queue.popleft()
            col.add(c_y)
            for dx,dy in directions:
                nx, ny = c_x + dx, c_y + dy
                if 0 <= nx < M and 0<= ny < N and land[nx][ny] == 1 and not checked[nx][ny]:
                    checked[nx][ny] = True
                    cnt += 1
                    queue.append((nx,ny))
                    
        
        return (cnt,col)
    
    answer_list = []

    
    for x in range(M):
        for y in range(N):
            if land[x][y] == 1 and not checked[x][y]:
                mount,col_list = bfs(x,y)
                answer_list.append((col_list,mount))

    print(answer_list)
    is_answer = [0] * N
    for col_list,mount in answer_list:
        for _ in col_list:
            is_answer[_] += mount
            
    print(is_answer)
    answer = max(is_answer)
    
    return answer

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print("asnwer :",solution(land))

