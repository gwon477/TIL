import sys

def main():
    N, K = map(int,sys.stdin.readline().split())
    nums = list(map(int,sys.stdin.readline().split()))
    
    A = N - K
    if A%(K-1) == 0:
        return print((A//(K-1))+1)
    else:
        return print((A//(K-1))+2)

main()

