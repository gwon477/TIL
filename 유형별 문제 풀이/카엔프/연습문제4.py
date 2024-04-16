from itertools import combinations
import sys

def main():
    N, K = map(int,sys.stdin.readline().split())
    nums = []
    ans = 0
    
    for i in range(N):
        nums.append(i)
        
    comb = list(combinations(nums,K))
    
    for _ in comb:
        if sum(_)%N == 0:
            ans +=1
            
    ans = ans%1000000007
    
    return print(ans)

main()