from itertools import permutations

def solution(k, dungeons):
    # 가능한 모든 던전 방문 순서를 생성
    max_dungeons = 0  # 탐험할 수 있는 최대 던전 수 초기화
    for dungeon_order in permutations(dungeons, len(dungeons)):
        fatigue = k  # 유저의 초기 피로도
        count = 0  # 탐험한 던전 수
        for dungeon in dungeon_order:
            required, cost = dungeon  # 필요 피로도와 소모 피로도
            if fatigue >= required:  # 유저가 던전을 탐험할 수 있는 경우
                fatigue -= cost  # 던전 탐험 후 피로도 감소
                count += 1  # 탐험한 던전 수 증가
            else:
                break  # 더 이상 탐험할 수 없는 경우 루프 중단
        max_dungeons = max(max_dungeons, count)  # 최대 탐험 가능 던전 수 업데이트

    return max_dungeons