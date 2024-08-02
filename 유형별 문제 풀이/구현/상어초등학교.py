import sys
from collections import defaultdict

N = int(sys.stdin.readline())

# 입력 받아서 학생 번호 - 좋아하는 짝궁 그래프 생성
graph = defaultdict(list)

sits = [[0 for i in range(N)] for i in range(N)]

#print("학생 자리 맵 :",sits)

for i in range(N*N):
    temp = list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(temp)):
        graph[temp[0]].append(temp[i])
        
print(graph)


# 네 방향에 좋아하는 짝이 있는지 확인
def checking(graph,cur_x,cur_y):
    score = 0
    
    #인접한 방향 체크
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
    # 네 방향 체크해서 graph에 있는 값이면 그 수에 맞게 +score 
    for dx,dy in directions:
        next_x,next_y = cur_x + dx, cur_y + dy
        
    
    return score





# 3
# 4 2 5 1 7
# 3 1 9 4 5
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4

