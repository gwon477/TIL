# 입출력 예 #1

# 입력: citations = [10, 8, 5, 4, 3]
# 출력: 4
# 설명: 이 과학자가 발표한 논문의 수는 5편이고, 그 중 4편의 논문은 4회 이상 인용되었습니다. 나머지 1편의 논문은 4회 이하 인용되었기 때문에 이 과학자의 H-Index는 4입니다.

# 입출력 예 #2

# 입력: citations = [25, 8, 5, 3, 3]
# 출력: 3
# 설명: 이 과학자가 발표한 논문의 수는 5편이고, 그 중 3편의 논문은 3회 이상 인용되었습니다. 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

# 입출력 예 #3

# 입력: citations = [1, 1, 1, 1, 1]
# 출력: 1
# 설명: 이 과학자가 발표한 논문의 수는 5편이고, 모든 논문이 1회 이상 인용되었습니다. 그러나 2편 이상의 논문이 2회 이상 인용된 것은 없으므로 H-Index는 1입니다.

# 입출력 예 #4

# 입력: citations = [0, 0, 0, 0, 0]
# 출력: 0

def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    answer = 0
    for i, citation in enumerate(citations):
        # 인용 횟수가 현재 인덱스(논문 개수)보다 크면 answer 업데이트
        if citation >= i + 1:
            answer = i + 1
        else:
            break
    return answer

print(solution(citations=[3, 0, 6, 1, 5]))