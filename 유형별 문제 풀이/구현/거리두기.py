# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    
    # 방향_1
    directions_1 = [(-1,0),(0,-1),(1,0),(0,1)]
    # 방향_2
    directions_2 = [(-2,0,-1,0),(0,-2,0,-1),(2,0,1,0),(0,2,0,1)]
    # 대각선
    diag = [(-1,-1,0,-1,-1,0),(1,-1,0,-1,1,0),(-1,1,-1,0,0,1),(1,1,0,1,1,0)]
    
    
    def Manhattan(x,y,place):
        for dx,dy in directions_1:
            nx,ny = x + dx, y + dy
            if 0<= nx < 5 and 0<= ny < 5:
                if place[nx][ny] == 'P':
                    return False
                
        for dx,dy,tx,ty in directions_2:
            nx,ny = x + dx, y + dy
            cx,cy = x + tx, y+ ty
            if 0<= nx < 5 and 0<= ny < 5:
                if place[nx][ny] == 'P':
                    if place[cx][cy] != 'X':
                        return False
                    
        for dx,dy,tx,ty,ttx,tty in diag:
            nx,ny = x + dx, y + dy
            cx,cy = x + tx, y+ ty
            ccx,ccy = x + ttx, y + tty
            if 0<= nx < 5 and 0<= ny < 5:
                if place[nx][ny] == 'P':
                    if place[cx][cy] != 'X' or place[ccx][ccy] != 'X':
                        return False
        
        return True
                    
        
    for place in places:
        check = True
        for x in range(len(place)):
            for y in range(len(place[0])):
                if place[x][y] == 'P':
                    if not Manhattan(x,y,place):
                        check = False
                        break
            if not check:
                break
        
        if check:
            answer.append(1)
        else:
            answer.append(0)
            
            
    return answer