# 백준 13706번 : 제곱근 https://www.acmicpc.net/problem/13706
# 문제 
# 정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.

# 출력
# 첫째 줄에 정수 N의 제곱근을 출력한다.

# import sys

# N = int(sys.stdin.readline().strip())

# def sol(N):
#     left, right = 1, N
#     while left <= right:
#         mid = (left + right) // 2
#         if mid * mid == N:
#             return mid
#         elif mid * mid < N:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return None

# print(sol(N))


# sys.stdin.readline().strip




import sys

N = int(sys.stdin.readline())

def sol(N):
    if N%3 == 1:
        return "CY"
    else:
        return "SK"
    
print(sol(N))