# - **정의:** 주어진 문자열에서 가장 긴 회문 부분 수열을 찾는 문제입니다. 회문(palindrome)은 앞으로 읽으나 뒤로 읽으나 같은 문자열을 의미합니다.

# - **예시:**
#     - 문자열 `X = "BBABCBCAB"`의 LPS는 `"BABCBAB"`로, 길이는 7입니다.

# - **알고리즘:** LPS 문제도 동적 프로그래밍을 사용하여 2차원 DP 테이블을 이용해 해결합니다. 이때 DP 테이블의 각 칸은 문자열의 부분 문자열에 대한 LPS 길이를 저장합니다.

# 문제 : https://www.acmicpc.net/problem/9251

# 해설 참고 : https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence





def lcs_map(X,Y):
    
    M = len(X)
    N = len(Y)
    
    dp = [[0 for i in range(N+1)] for j in range(M+1)]
    
    for i in range(1,M+1):
        for j in range(1,N+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return dp


X = "ACAYKP"
Y = "CAPCAK"

dp = lcs_map(X,Y)

def use_lcs(dp,X,Y):
    answer = []
    
    i,j = len(X),len(Y)
    
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            answer.append(X[i-1])
            i -= 1
            j -= 1
            
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(answer))


print(use_lcs(dp,X,Y))


# lcs_length, dp_table = lcs(X, Y)
# lcs_string = print_lcs(dp_table, X, Y)

# print("LCS의 길이:", lcs_length)
# print("LCS 문자열:", lcs_string)