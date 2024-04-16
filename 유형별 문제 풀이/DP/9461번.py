



# 이 코드에서 시간 초과가 발생하는 주된 이유는 재귀 함수 P(n)의 비효율적인 사용 때문입니다. 
# 특히, P(n) 함수는 P(n-2)와 P(n-3)을 호출하며, 이 과정이 반복되면서 같은 계산을 여러 번 수행하게 됩니다. 
# 예를 들어, P(5)를 계산하기 위해서는 P(3)과 P(2)가 필요하고, P(4)를 계산하기 위해서도 P(2)와 P(1)이 필요합니다. 
# 이렇게 되면 P(2)와 같은 계산이 여러 번 중복되어 수행됩니다.

# 이러한 중복 계산은 입력 값 N이 커질수록 기하급수적으로 증가하게 되어, 시간 복잡도가 매우 높아집니다. 
# 따라서, 큰 N에 대해서는 시간 내에 계산을 완료하기 어렵게 됩니다.

# 이 문제를 해결하기 위한 방법 중 하나는 동적 계획법(Dynamic Programming, DP)을 사용하는 것입니다. 
# DP를 사용하면 이미 계산한 결과를 저장해 두었다가 재사용함으로써 중복 계산을 방지할 수 있습니다. 
# 예를 들어, P(n)의 결과를 계산한 후에는 배열이나 리스트에 저장해 두고, 같은 값을 다시 계산해야 할 때는 저장된 값을 재사용할 수 있습니다.

import sys

def P(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(sys.stdin.readline())
answer = []
for i in range(T):
    N = int(sys.stdin.readline())
    answer.append(P(N))
    
for ans in answer:
    print(ans)
