from collections import deque, defaultdict
import sys

def main():
    N = int(sys.stdin.readline())
    graph = defaultdict(list)
    
    for i in range(N-1):
        nodes = list(map(int, sys.stdin.readline().split()))
        graph[nodes[0]].append((nodes[1],nodes[2]))
        graph[nodes[1]].append((nodes[0],nodes[2]))
    
    def bfs(graph,start_v):

        visited=set()
        visited.add(start_v)
        q = deque()
        q.append((start_v,0))
        total_cost = 0

        while q:
            cur_v, cur_c = q.popleft()
            for v,c in graph[cur_v]:
                if v not in visited:
                    cost = c + cur_c
                    visited.add(v)
                    q.append((v,cost))
                    total_cost += cost

        return total_cost
    
    
    min_cost = []
    
    for i in range(N):
        min_cost.append(bfs(graph=graph,start_v=i))
        
    return min(min_cost)

print(main())