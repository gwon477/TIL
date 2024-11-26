def solution(name):
    alphabat = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # 각 문자에 대해 'A'에서 해당 문자로 변경하는 최소 조작 횟수 계산
    dp = [min(alphabat.index(c), 26 - alphabat.index(c)) for c in name]

    # 이동 거리의 기본값을 직진 시의 최대 이동으로 설정
    min_moves = len(name) - 1

    for i in range(len(name)):
        # 현재 위치에서 연속된 'A'의 시작 위치 탐색
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1

        # 최소 이동 경로 계산: 현재 위치에서 i까지의 이동과 다시 돌아가는 경로
        moves = i + i + len(name) - next_i
        min_moves = min(min_moves, moves)


    # 최종 결과 반환: 알파벳 변경 횟수의 합과 최소 이동 횟수
    return sum(dp) + min_moves


print("1번")
print(solution("ABAABAA"))
print("======================")


# 1
# 입력값 〉 "BAAAAABAA"
# 기댓값 〉 5

# 2
# 입력값 〉 "BBBABAABABABB"
# 기댓값 〉 20

# 3
# 입력값 〉 "BBABAAAAAAB"
# 기댓값 〉 9

# 4
# 입력값 〉 "BABBAABB"
# 기댓값 〉 11

# 5
# 입력값 〉 "BBAAAAAAABAB"
# 기댓값 〉 9

# 6
# 입력값 〉 "BAABBAAA"
# 기댓값 〉 7