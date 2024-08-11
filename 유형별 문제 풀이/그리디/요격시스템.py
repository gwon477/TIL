def solution(targets):
    answer = 0
    N = len(targets)
    targets = sorted(targets, key=lambda x: x[1])
    
    rocket_location = float('-inf')
    #print(targets)
    for i in range(0,N):
        if targets[i][0] >= rocket_location:
            answer += 1
            rocket_location = targets[i][1]
    
    return answer