def solution():
    return

print(solution())

import sys
from collections import defaultdict
import heapq

N,M,G,S,E = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(set)
vertexs = []
for i in range(M):
    s,e,c = map(int,sys.stdin.readline().split())
    vertexs.append((s,e,c))
groups = []
for i in range(G):
    group = list(map(int,sys.stdin.readline().split()))
    groups.append(group)

for s,e,c in vertexs:
    graph[s].add((e,c))
    graph[e].add((s,c))

for group in groups:
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j:
                graph[group[i]].add((group[j],0))
                graph[group[j]].add((group[i],0))
                
def dk(s,e):
    distance = [float('inf')] * (N+1)
    distance[s] = 0
    pq = []
    heapq.heappush(pq,(s,0))
    
    while pq:
        current_vertex, current_cost = heapq.heappop(pq)

        if current_cost > distance[current_vertex]:
            continue
        
        for next_vertex, cost in graph[current_vertex]:
            #print("next_vertex:",next_vertex)
            new_cost = current_cost + cost
            if new_cost < distance[next_vertex]:
                distance[next_vertex] = new_cost
                heapq.heappush(pq,(next_vertex,new_cost))
    
    print(distance)
    if distance[e] == float('inf'):
        return -1
    else:
        return distance[e]

print(dk(S,E))

# 출력
# 예시1
# 입력1
# 7 5 1 1 7
# 1 2 5
# 2 3 1
# 4 5 1
# 6 7 10
# 5 7 2
# 3 4 6

# 출력1

# 9

# 예시2

# 입력2

# 10 5 2 1 10

# 1 2 10

# 1 10 10

# 2 10 100

# 6 10 1

# 1 5 10000

# 1 6 3 4 5

# 2 10

# 출력2

# 1