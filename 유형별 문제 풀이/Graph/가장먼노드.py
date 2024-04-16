from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    # O(N)
    for _ in edge:
        graph[_[0]].append(_[1])
        graph[_[1]].append(_[0])
        
    
    queue = deque()
    visited = {}
    queue.append((1,0))
    visited[1] = 0
    cost = 0
    
    while queue:
        cur_v,cur_cost = queue.popleft()
        
        for v in graph[cur_v]:
            if v not in visited:
                queue.append((v,cur_cost+1))
                visited[v] = cur_cost+1
        
        cost = cur_cost
        
    for _ in visited:
        if visited[_] == cost:
            answer += 1
            
    return print(answer)

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])