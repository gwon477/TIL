from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    answer = []
    
    # 인접 리스트 생성
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    # 목적지에서 모든 노드까지의 최단 거리를 계산
    distances = [-1] * (n + 1)  # 모든 노드에 대한 거리를 -1로 초기화
    distances[destination] = 0  # 목적지에서 목적지까지의 거리는 0
    
    queue = deque([destination])
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 노드
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    # 각 소스에 대해 계산된 최단 거리를 답에 추가
    for source in sources:
        answer.append(distances[source])
    
    return answer
