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
    
    # true_words = []
    # able_words = set()
    # for word in words:
    #     T = word[0][4:-4]
    #     X = tuple(set(T) - set(('a','t','n','i','c')))
    #     true_words.append(set(X))
    #     for i in set(tuple(T)):
    #         able_words.add(i)
    
    # target = []
    # for i in range(1,M-4):
    #     target.extend(list(combinations(list(able_words),i)))
        
    answer = 0
    essential_letters = set(('a', 't', 'n', 'i', 'c'))  # 필수 문자 집합
    true_words = []
    able_words = set()  # 사용할 수 있는 문자들 저장할 집합

    for word in words:
        # 앞뒤의 필수 문자를 제외한 중간 문자만 추출
        T = set(word[4:-4])
        filtered = T - essential_letters  # 필수 문자 제외

        true_words.append(filtered)  # true_words에 추가
        able_words.update(filtered)  
        
    # print(true_words)
    # print(target)
    
    # for t in target:
    #     if t in true_words:
    #         answer += 1
            
    # print(answer)
    # return answer

    max_count = 0
    for comb in combinations(able_words, M - 5):
        comb_set = set(comb)
        count = sum(1 for word in true_words if word <= comb_set)  # 포함 여부 확인
        max_count = max(max_count, count)  # 최대값 갱신

    return max_count

solution(N, M, words)

