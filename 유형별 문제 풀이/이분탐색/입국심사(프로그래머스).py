def solution(n, times):
    left = 1
    right = max(times) * n
    print(right)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        print()
        total = sum(mid // time for time in times)
        
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer

# 예제 테스트
# n = 6
times = [7, 10]
# print(solution(n, times))  # 출력: 28

mid = 30
print(sum(mid // time for time in times))

print(30 // 7)
print(30 // 10)