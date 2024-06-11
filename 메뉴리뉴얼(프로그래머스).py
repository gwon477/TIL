from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    orders_sorted = []
    for _ in orders:
        orders_sorted.append(sorted(_))
    
    for _ in course:
        #r = findcase(_)
        
        r = findcase(orders_sorted,_)
        for i in r:
            answer.append(i)
    answer.sort()
    return answer

def findcase(orders,num):
    case = defaultdict()
    task = []
    for _ in orders:
        a = list(combinations(_,num))
        for _ in a:
            if _ not in case:
                case[_] = 0
            else:
                case[_] += 1
    case = [k for k,v in case.items() if max(case.values()) == v and max(case.values()) != 0]
    
    for _ in case:
        task.append(''.join(_))
    
    return task

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))