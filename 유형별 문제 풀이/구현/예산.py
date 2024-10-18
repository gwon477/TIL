import sys

# 입력받기
N = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

# 이진 탐색을 위한 함수 정의
def allocate(mid):
    total = 0
    for request in money:
        # 요청이 상한액을 넘으면 상한액으로 배정
        total += min(request, mid)
    return total

# 전체 요청 금액이 예산보다 작거나 같으면, 최대 요청 금액 출력
if sum(money) <= budget:
    print(max(money))
else:
    # 이진 탐색을 위한 초기 설정
    low, high = 0, max(money)
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2
        # 현재 상한액(mid)으로 배정한 총 예산 확인
        total = allocate(mid)  # 함수 호출 결과 저장
        if total <= budget:  # 배정된 예산이 총 예산을 초과하지 않음
            answer = mid  # 가능한 상한액을 저장
            low = mid + 1  # 더 큰 상한액을 시도
        else:
            high = mid - 1  # 상한액을 줄여야 함
    
    print(answer)
