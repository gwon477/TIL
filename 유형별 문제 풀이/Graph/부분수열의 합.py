import sys

answer = 0

N, S = map(int,sys.stdin.readline().strip().split())
print("N,S",N,S)

numbers = list(map(int,sys.stdin.readline().strip().split()))
print("numbers:",numbers)


def check(num):
    c = 0
    start = 0
    end = num
    
    while end <= N:
        if sum(numbers[start:end]) == S:
            c += 1
        start += 1
        end += 1
    return c

for i in range(1,N+1):
    answer += check(i)
    
print(answer)