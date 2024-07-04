import sys

company_name = sys.stdin.readline()

def solution(name):
    answer = name[0]
    for i in range(1,len(name)):
        if name[i] == '-':
            answer += name[i+1]
            
    return answer

print(solution(company_name))
