from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    answer = []
    
    dic = defaultdict(list)
    
    for key,value in roads:
        dic[key].append(value)
        dic[value].append(key)
    
    distances = [-1] * (n+1)
    distances[destination] = 0
    
    queue = deque([destination])
    
    while queue:
        cur_v = queue.popleft()
        cur_c = distances[cur_v]
        
        for _ in dic[cur_v]:
            if distances[_] == -1:
                queue.append(_)
                distances[_] = cur_c + 1
    
    for source in sources:
        answer.append(distances[source])
    
    return answer

print(solution(5,[[1, 2],[1, 4],[2, 4],[2, 5],[4, 5]],[1, 3, 5],5))

# n	roads	sources	destination	result
# 3	[[1, 2], [2, 3]]	[2, 3]	1	[1, 2]
# 5,[[1, 2],[1, 4],[2, 4],[2, 5],[4, 5]],[1, 3, 5],5