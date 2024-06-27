def solution(maps):
    def dfs(x, y):
        stack = [(x, y)]
        food_sum = 0
        
        while stack:
            cx, cy = stack.pop()
            
            if 0 <= cx < len(maps) and 0 <= cy < len(maps[0]) and maps[cx][cy] != 'X' and not visited[cx][cy]:
                visited[cx][cy] = True
                food_sum += int(maps[cx][cy])
                
                # 상, 하, 좌, 우 탐색
                stack.append((cx - 1, cy))
                stack.append((cx + 1, cy))
                stack.append((cx, cy - 1))
                stack.append((cx, cy + 1))
        
        return food_sum

    if not maps:
        return [-1]
    
    # visited 배열 초기화
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    food_list = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                max_food = dfs(i, j)
                food_list.append(max_food)
    
    if not food_list:
        return [-1]
    
    return sorted(food_list)

# 예제 입력
maps1 = ["X591X","X1X5X","X231X","1XXX1"]
maps2 = ["XXX","XXX","XXX"]

# 결과 출력
print(solution(maps1))  # [1, 1, 27]
print(solution(maps2))  # [-1]
