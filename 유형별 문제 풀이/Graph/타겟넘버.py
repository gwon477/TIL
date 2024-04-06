def solution(numbers, target):
    answer = 0
    
    # dfs 함수 정의
    def dfs(index, current_sum):# 상위 스코프의 answer 변수를 참조하기 위해 nonlocal 키워드 사용
        nonlocal answer
        if index == len(numbers):  # 모든 숫자를 다 사용한 경우
            if current_sum == target:  # 현재 합이 타겟 넘버와 같으면
                answer += 1  # 정답 카운트 증가
            return
        
        # 현재 숫자를 더하는 경우
        dfs(index + 1, current_sum + numbers[index])
        # 현재 숫자를 빼는 경우
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)  # dfs 탐색 시작
    return answer

print(solution([4, 1, 2, 1],4))