def check(row):
    graph = {
        "start_B" : 0,
        "start_W" : 0
    }
    
    # B로 시작해야한다고 가정
    s,e = 0,2
    while e <= len(row)+1:
        target = row[s:e]
        if target[0] != 'B':
            graph['start_B'] += 1
        if len(target) == 1:
            pass
        else:
            if target[1] != 'W':
                graph['start_B'] += 1

        s = e
        e += 2
    # W로 시작해야한다고 가정  
    s,e = 0,2
    while e <= len(row)+1:
        target = row[s:e]
        if target[0] != 'W':
            graph['start_W'] += 1
        if len(target) == 1:
            pass
        else:
            if target[1] != 'B':
                graph['start_W'] += 1
    
        s = e
        e += 2
    return graph

import sys

N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline().strip())
    
s_x,e_x = 0,8
s_y,e_y = 0,8

def board_check(board):
    SB = 0
    SW = 0

    for i,row in enumerate(board):
        graph = check(row)
        if i % 2 == 0:
            SB += graph['start_B']
            SW += graph['start_W']
        else:
            SB += graph['start_W']
            SW += graph['start_B']
    return min(SB,SW)

answer = []

# 8 칸씩 잘라서
for x in range(N+1-8):
    for y in range(M+1-8):
        new_board = []
        for i in range(s_x,e_x):
            new_board.append(board[i][s_y:e_y])
        tmp = board_check(new_board)
        answer.append(tmp)
        s_y += 1
        e_y += 1
    s_y,e_y = 0,8
    s_x += 1
    e_x += 1
        
print(min(answer))