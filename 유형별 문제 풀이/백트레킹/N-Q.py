# def solution(n):
#     answer = 0
#     return answer


# def del_block(x,y,n):
    
    
#     direction = [(-1,-1),(1,-1),(-1,1),(1,1)]

#     visited = [[False] * n for i in range(n)]
    
#     visited[x][y] = True
#     for i in range(n):
#         visited[x][i] = True
#         visited[i][y] = True
    
#     for dx,dy in direction:
#         for i in range(1,n):
#             nx,ny = x + dx*i ,y + dy*i
#             if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
#                 visited[nx][ny] = True
                
#     return visited
# print(del_block(0,0,4))


def solution(n):
    global ans
    ans = 0
    row = [0] * n

    def is_promising(x):
        for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
        
        return True

    def n_queens(x):
        global ans
        if x == n:
            ans += 1
            return

        else:
            for i in range(n):
                row[x] = i
                if is_promising(x):
                    n_queens(x+1)
                    

    n_queens(0)
    return ans

print(solution(4))