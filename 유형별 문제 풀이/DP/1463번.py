import sys

N = int(sys.stdin.readline())

ans = []
def backtraking(curr, cnt):
    if curr == 1:
        ans.append(cnt)
        return
    
    elif curr%3 == 0:
        curr = curr//3
        cnt += 1
        backtraking(curr=curr, cnt=cnt) 
    
    elif curr%2 == 0:
        curr = curr//2
        cnt += 1
        backtraking(curr=curr, cnt=cnt)
        
    else:
        curr -= 1
        cnt += 1
        backtraking(curr=curr, cnt=cnt)
        
backtraking(N,0)
print(ans[0])
