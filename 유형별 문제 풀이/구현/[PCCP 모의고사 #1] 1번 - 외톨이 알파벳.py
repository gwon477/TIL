from collections import defaultdict
def solution(input_string):
    answer = ''
    a = set()
    graph = defaultdict(list)
    before = input_string[0]
    graph[before].append(1)
    N = len(input_string)
    
    for i in range(1,N):
        if input_string[i] == before:
            graph[input_string[i]].append(1)
        else:
            if input_string[i] not in graph:
                graph[input_string[i]].append(1)
            else:
                a.add(input_string[i])
        before = input_string[i]
        
    if not a:
        return 'N'
    
    sorted_answer = sorted(a)
    for _ in sorted_answer:
        answer += _
    
    return answer


print("답 : ", solution("string"))