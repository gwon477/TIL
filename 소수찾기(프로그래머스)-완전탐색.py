from itertools import permutations
from math import sqrt

# 소수인지 판별하는 부분
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def solution(numbers):
    num_set = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            num_set.add(num)
    
    prime_count = 0
    for num in num_set:
        if is_prime(num):
            prime_count += 1
    
    return prime_count


print(int(31**0.5))
print(int(sqrt(17)))