import sys

N, K = map(int,sys.stdin.readline().split(' '))

def solution(N,K):
    answer = 0
    current_amount = 1
    bottle = N
    
    # 처음에 홀수인 경우에 1의 물병을 추가해서 짝수로 마춰준다.
    if bottle % 2 != 0:
        answer += 1
        bottle += 1
    
    while bottle > K:
        if bottle == K:
            break
        # 양이 같은 물병들 모두 옮겨 담기
        bottle = bottle//2
        # 합쳐진 물의 양
        current_amount *= 2
        
        if bottle % 2 != 0 and bottle != 1:
            answer += current_amount
            bottle += 1
    
    return answer

print(solution(N,K))