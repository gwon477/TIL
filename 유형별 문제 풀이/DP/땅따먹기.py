def solution(land):
    answer = 0
    N = len(land)
    
    for i in range(1,N):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])  
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])  
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])  
        
    answer = max(land[N-1])
    return answer


# 입력값 〉 [[6, 7, 1, 2], [2, 3, 10, 8], [1, 3, 9, 4], [7, 11, 4, 9]]
# 기댓값 〉 35