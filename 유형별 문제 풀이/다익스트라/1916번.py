# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = defaultdict(list)

for i in range(M):
    u,v,c = map(int,sys.stdin.readline().split())
    graph[u].append((c,v))

start,final = map(int,sys.stdin.readline().split())

print(graph)

def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0,start))
    
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    
    
    return costs[final]



print(dijkstra(graph=graph,start=start,final=final))