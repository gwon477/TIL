import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
start_x, start_y, direction = map(int, sys.stdin.readline().split())
road = []
for i in range(N):
    road.append(list(map(int, sys.stdin.readline().split())))

answer = 0
clean = set()

# 방향: 북, 동, 남, 서 (0, 1, 2, 3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = deque()
queue.append((start_x, start_y, direction))

while queue:
    cx, cy, direction = queue.popleft()

    # 현재 위치가 청소되지 않았다면 청소
    if (cx, cy) not in clean:
        clean.add((cx, cy))
        answer += 1

    clean_cnt = 0
    # 현재 칸 주변 4칸이 청소되었는지 여부 확인
    for i in range(4):
        nx, ny = cx + directions[i][0], cy + directions[i][1]
        if (nx, ny) in clean or road[nx][ny] == 1:
            clean_cnt += 1

    # 만약 주변 4칸 모두 청소가 되어 있거나 벽인 경우
    if clean_cnt == 4:
        # 후진 방향
        back_direction = (direction + 2) % 4
        bx, by = cx + directions[back_direction][0], cy + directions[back_direction][1]

        # 후진할 곳이 벽이면 작동 종료
        if road[bx][by] == 1:
            break
        # 후진할 수 있으면 후진
        else:
            queue.append((bx, by, direction))

    # 청소되지 않은 빈 칸이 있는 경우
    else:
        for i in range(4):
            # 반시계 방향으로 회전
            direction = (direction + 3) % 4
            nx, ny = cx + directions[direction][0], cy + directions[direction][1]

            # 청소되지 않은 빈 칸이 있으면 이동
            if (nx, ny) not in clean and road[nx][ny] == 0:
                queue.append((nx, ny, direction))
                break

print(answer)
