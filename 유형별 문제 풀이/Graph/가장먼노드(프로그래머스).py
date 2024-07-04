# 가장 먼 노드

from collections import deque, defaultdict

def solution(n,vertex):
    answer = 0
    graph = defaultdict(list)
    
    for _ in vertex:
        graph[_[0]].append(_[1])
        graph[_[1]].append(_[0])
    
    queue = deque()
    queue.append((1,0))
    visited = {}
    visited[1] = 0
    max_cost = 0
    
    while queue:
        cur_vertex, cur_cost = queue.popleft()
        
        for next_vertex in graph[cur_vertex]:
            if next_vertex not in visited:
                visited[next_vertex] = cur_cost + 1
                queue.append((next_vertex,cur_cost + 1))
        
        max_cost = cur_cost
    
    for _ in visited:
        if visited[_] == max_cost:
            answer += 1
    
    return answer