from itertools import permutations

def solution(ability):
    num_students = len(ability)
    num_sports = len(ability[0])
    
    # 가능한 모든 학생 배치의 순열을 생성
    max_total_ability = 0
    for perm in permutations(range(num_students), num_sports):
        current_total = sum(ability[perm[i]][i] for i in range(num_sports))
        max_total_ability = max(max_total_ability, current_total)
    
    return max_total_ability



print("answer :", solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))