import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
words = []
for i in range(N):
    words.append(sys.stdin.readline().split())

def solution(N,M,words):
    answer = 0
    
    if M < 5 :
        return 0
    
    true_words = []
    able_words = set()
    for word in words:
        T = word[0][4:-4]
        X = tuple(set(T) - set(('a','t','n','i','c')))
        true_words.append(set(X))
        for i in set(tuple(T)):
            able_words.add(i)
    
    target = []
    for i in range(1,M-4):
        target.extend(list(combinations(list(able_words),i)))
        
    print(true_words)
    print(target)
    
    for t in target:
        if t in true_words:
            answer += 1
    print(answer)
    return answer

solution(N, M, words)

