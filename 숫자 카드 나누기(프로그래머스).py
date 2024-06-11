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