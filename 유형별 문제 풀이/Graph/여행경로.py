# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict

def solution(Tickets):
    answer = []
    graph = defaultdict(list)
    for start,end in Tickets:
        graph[start].append(end)
        if len(graph[start]) > 1:
            graph[start].sort(reverse=True)
    
    print()
    
    stack = ['ICN']
    
    while stack:
        cur_prot = stack[-1]
        if cur_prot not in graph or not graph[cur_prot]:
            answer.append(stack.pop())
        else:
            stack.append(graph[cur_prot].pop())
    
    
    return answer[::-1]

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))