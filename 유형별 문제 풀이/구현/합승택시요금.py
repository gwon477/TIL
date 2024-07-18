# def solution(n, s, a, b, fares):
#     # 무한대를 의미하는 큰 값으로 초기화
#     inf = float('inf')
#     # 모든 쌍의 최단 경로를 저장할 2차원 배열 초기화
#     dist = [[inf] * (n + 1) for _ in range(n + 1)]
    
#     # 그래프 초기화: 자기 자신으로 가는 경로는 0으로 초기화
#     for i in range(1, n + 1):
#         dist[i][i] = 0
    
#     # 주어진 요금 정보로 그래프 초기화
#     for c, d, f in fares:
#         dist[c][d] = f
#         dist[d][c] = f
    
#     # 플로이드-워셜 알고리즘 적용
#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 if dist[i][j] > dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
    
#     # 최소 요금 계산
#     min_cost = inf
#     for k in range(1, n + 1):
#         cost = dist[s][k] + dist[k][a] + dist[k][b]
#         if cost < min_cost:
#             min_cost = cost
    
#     return min_cost

# # 예제 입력
# n = 6
# s = 4
# a = 6
# b = 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# # 함수 호출
# print(solution(n, s, a, b, fares))  # 82


import heapq

def dijkstra(n, graph, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # 다익스트라 알고리즘으로 최단 경로 계산
    dist_from_s = dijkstra(n, graph, s)
    dist_from_a = dijkstra(n, graph, a)
    dist_from_b = dijkstra(n, graph, b)
    
    # 최소 요금 계산
    min_cost = float('inf')
    for k in range(1, n + 1):
        cost = dist_from_s[k] + dist_from_a[k] + dist_from_b[k]
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

# 예제 입력
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# 함수 호출
print(solution(n, s, a, b, fares))  # 82
