# 11399 번

import sys

N = map(int,sys.stdin.readline().strip())
line = list(map(int,sys.stdin.readline().strip().split(' ')))

def sol(line):
    sorted_line = sorted(line)
    
    result = 0
    
    best_case = []
    
    for i in range(len(sorted_line)):
        best_case.append(sum(sorted_line[0:i+1]))
        
    result = sum(best_case)
    
    return result
    
print(sol(line))