"""_summary_

학생 별 좋아하는 학생 맵 만들기

1. 맵 만들기

2. 학생 배치
   - 비어있는 칸 중에서 좋아하는 학생이 인접한 칸
   - 인접한 칸에 좋아하는 학생의 수가 같은 경우 빈칸이 많은 곳

3. 학생들이 앉은 자리에서 만족도 계산

"""

import sys
from collections import defaultdict,deque

N = int(sys.stdin.readline())

# 학생 별 좋아하는 학생 그래프 만들기
students = defaultdict(list)
for i in range(N **2):
    student,A,B,C,D = map(int,sys.stdin.readline().split(' '))
    students[student].append(A)
    students[student].append(B)
    students[student].append(C)
    students[student].append(D)

#1. 책상 맵 만들기    
tables = [[0 for i in range(N)] for j in range(N)]

#2. 학생 배치
directions = [(-1,0),(0,-1),(1,0),(0,1)]

# 학생 별로 자리 배치
for student in students:
    score = 0
    max_socre = 0
    fix = deque()
    for x in range(N):
        for y in range(N):
            score = 0
            if tables[x][y] == 0:
                for dx,dy in directions:
                    n_x, n_y = x + dx, y +dy
                    if 0<= n_x and n_x < N and 0 <= n_y and n_y < N:
                        if tables[n_x][n_y] in students[student]:
                            score += 5
                        if tables[n_x][n_y] == 0:
                            score += 1
            if max_socre < score:
                max_socre = score
                if len(fix) > 0:
                    fix.popleft()
                fix.append((x,y))
                
    f_x,f_y = fix[-1]
    tables[f_x][f_y] = student


result = 0

for x in range(N):
    for y in range(N):
        cnt = 0
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<= nx and nx<N and 0<=ny and ny < N and tables[nx][ny] in students[tables[x][y]]:
                cnt += 1
        
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000
         
    
print("tables :",tables)
print("result :",result)