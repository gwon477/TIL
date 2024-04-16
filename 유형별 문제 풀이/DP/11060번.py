import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
    
def find_last(index):
    global answer
    answer += 1
        
    next_index = index + nums[index]
        
    if next_index == 0:
        answer = -1
        return answer
        
    if next_index > N:
        return answer
    else:
        find_last(next_index)
            
find_last(index=0)


print(answer)