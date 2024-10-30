import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
dp = [-1e9]*(m+1)

for i in range(n-1,-1,-1):
    price = numbers[i]

    # 현재 내가 살 수 있는 가격인 price부터 dp를 확인한다. 그 밑은 어차피 해당 숫자를 살 수 없다
    for j in range(price,m+1):
        dp[j] = max(dp[j],dp[j-price]*10+i,i) # 현재 dp값, 이 숫자를 뒤에 붙인 값, 현재 숫자만 가져가는 값 이 셋 중에서 가장 큰 값 선택

print(dp[m])