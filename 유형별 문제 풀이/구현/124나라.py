def solution(n):
    answer = ''
    
    while n > 0:
        n -= 1
        print("1을 뺸 후 N :", n)
        
        answer = '124'[n%3] + answer
        print("answer :", answer)
        
        n //= 3
    
    return answer

print(solution(9))