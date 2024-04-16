from collections import deque

def solution(n, computers):
    
    visited = [False] * n
    answer = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터가 있다면
            bfs(i)  # 해당 컴퓨터부터 BFS 탐색 시작
            answer += 1 
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))