def calculate_ranks(scores):
    # 점수를 내림차순으로 정렬하고, 등수를 매깁니다.
    sorted_scores = sorted(enumerate(scores), key=lambda x: -x[1])
    print(sorted_scores)
    ranks = [0] * len(scores)
    current_rank = 1
    
    for i in range(len(scores)):
        if i > 0 and sorted_scores[i][1] < sorted_scores[i-1][1]:
            current_rank = i + 1
        ranks[sorted_scores[i][0]] = current_rank
    
    return ranks

# ranks = [3,1,2]

import sys
input = sys.stdin.readline()
data = input.split()

N = int(data[0])
scores1 = list(map(int, data[1:N+1]))
scores2 = list(map(int, data[N+1:2*N+1]))
scores3 = list(map(int, data[2*N+1:3*N+1]))

# ranks1 = calculate_ranks(scores1)
# ranks2 = calculate_ranks(scores2)
# ranks3 = calculate_ranks(scores3)

total_scores = [scores1[i] + scores2[i] + scores3[i] for i in range(N)]
total_ranks = calculate_ranks(total_scores)

# print(" ".join(map(str, ranks1)))
# print(" ".join(map(str, ranks2)))
# print(" ".join(map(str, ranks3)))
# print(" ".join(map(str, total_ranks)))



print("TEST : ",calculate_ranks([40,70,70]))