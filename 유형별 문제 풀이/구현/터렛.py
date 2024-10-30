import sys

T = int(sys.stdin.readline())

def solution(point_info):
    point = 0
    
    x1,y1,r1,x2,y2,r2 = point_info
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    if x1 == x2 and y1 == y2 and r1 != r2:
        return 0
    
    turret_distance = abs(x2-x1)**2 + abs(y2-y1)**2
    
    if (r1 + r2)**2 < turret_distance:
        return 0
    
    if (r1 + r2)**2 == turret_distance or (r2 - r1) **2 == turret_distance:
        return 1
    
    if (r2-r1)**2 > turret_distance:
        return 0
    
    return 2

for i in range(T):
    point_info = list(map(int,sys.stdin.readline().split(' ')))
    print(solution(point_info))

