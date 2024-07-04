import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))


def solution(nums,N):
    # DP 배열 초기화: 각 위치에서 끝나는 최대 증가 부분 수열의 합
    dp = nums[:]  # 각 원소 자체로 끝나는 경우의 합으로 초기화
    
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    
    return max(dp)  # DP 배열에서 최대값을 찾아 반환

print(solution(nums=nums,N=N))


#1 100 2 50 60 3 5 6 7 8