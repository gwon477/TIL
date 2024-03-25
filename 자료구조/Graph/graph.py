# graph 선언
graph = {
    'A' : ['B','D','E'],
    'B' : ['A','C','D'],
    'C' : ['B'],
    'D' : ['A','B'],
    'E' : ['A']
}



# Graph BFS

from collections import deque

def bfs(graph, start_v):
    # 방문한 내역
    visited = [start_v]
    # 예약 내역
    q = deque(start_v)
    
    while q:
        # 예약 확인
        cur_v = q.popleft()
        
        for _ in graph[cur_v]:
            if _ in visited:
                pass
            else:
                q.append(_)
                visited.append(_)
    return visited

print(bfs(graph=graph, start_v= 'A'))



# DFS

visited = []

def dfs(cur_v):
    visited.append(cur_v)
    for _ in graph[cur_v]:
        if _ in visited:
            pass
        else:
            dfs(_)

