import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    r, k = map(int, sys.stdin.readline().strip().split(' '))
    for i in range(k):
         o, p = map(int,sys.stdin.readline().strip().split(' '))
    print(k - 1)
