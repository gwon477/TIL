import sys

G1,S1,B1 = map(int,sys.stdin.readline().split())
G2,S2,B2 = map(int,sys.stdin.readline().split())

def solution(G1,S1,B1,G2,S2,B2):
    answer = 0
    print("G1,S1,B1:",G1,S1,B1)
    print("G2,S2,B2:",G2,S2,B2)
    
    dp_A = [G1,S1,B1]
    dp_B = [G2,S2,B2]
    
    # 가지고 있는 모든 동전이 안되는 경우
    if G1 < G2 and S1 < S2 and B1 < B2:
        return -1
    
    # for i in range(3):
    #     while dp_A[i] < dp_B[i]:
            
    
    return answer

solution(G1,S1,B1,G2,S2,B2)