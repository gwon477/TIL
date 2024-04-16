import sys
from itertools import combinations

def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    if len(set(nums)) == 1:
        return print("NO")
    
    case = list(combinations(nums,3))
    
    for _ in case:
        if _[0] < _[1] and _[1] < _[2]:
            return print("YES")
    
    return print("NO")

main()

# 6
# 3 1 4 1 5 9