import math

def solution(arrayA, arrayB):
    answer = 0
    # listA 최대공약수 계산
    A = gcd(arrayA)
    
    # listB 최대공약수 계산
    B = gcd(arrayB)
    ml = 0
    al = 0
    
    # listA에서 최대 공약수가 있는경우
    if A != 1:
        cnt = 0
        for _ in arrayB:
            # B에서 나눠지는 인덱스가 있는 경우 0
            if _% A == 0:
                cnt += 1
        if cnt == 0:
            # B에서 나눠지는 인덱스가 없는 경우 answer = A
            ml = A
    
    if B != 1:
        cnt = 0
        for _ in arrayA:
            # B에서 나눠지는 인덱스가 있는 경우 0
            if _% B == 0:
                cnt += 1
        if cnt == 0:
            # B에서 나눠지는 인덱스가 없는 경우 answer = A
            al = B

    print(A,B)
    answer = max(ml,al)
    
    return answer

    
def gcd(args):
    def _gcd(n, m):
        while m > 0:
            n, m = m, n % m
        return n
    if len(args) < 2:
        return 1
    else:
        n = args[0]
        for m in args[1:]:
            n = _gcd(n, m)
        return n


print(2%4)

# [10, 17]	[5, 20]	0
# [10, 20]	[5, 17]	10
# [14, 35, 119]	[18, 30, 102]	7


# def cal(a,b): # 최대 공약수 구하기
#     if a%b == 0:
#         return b
#     return cal(b, a%b) # 35 = 17*2 + 1 인 것을 생각!
    
# def solution(arrayA, arrayB):
#     a = arrayA[0]
#     b = arrayB[0]
    
#     for i in range(1, len(arrayA)):
#         a = cal(arrayA[i], a)
#         b = cal(arrayB[i], b)
    
#     answerA = a
#     answerB = b
    
#     # 최대공약수가 다른 숫자카드와 나누어 떨어지는지 확인
#     for i in range(len(arrayA)):
#         if arrayA[i]%b == 0: # 영희 숫자카드가 철수 숫자를 나누는지 확인
#             answerB = 0
#         if arrayB[i]%a == 0: # 철수 숫자카드가 영희 숫자를 나누는지 확인
#             answerA = 0
    
            
#     return max(answerA, answerB)