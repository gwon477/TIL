from collections import deque

def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(len(computers)):
        graph[i+1] = []
        for j in range(len(computers)):
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
            
    
    queue = deque(1)
    visited = {}
    visited[1] = True
    
    while queue:
        cur_v = queue.popleft()
        for _ in graph[cur_v]:
            if _ not in visited:
                queue.append(_)
                visited[_] = True
        

    return answer

print(sol(n, computers))