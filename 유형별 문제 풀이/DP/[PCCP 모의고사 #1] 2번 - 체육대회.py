from itertools import permutations

def solution(ability):
    num_students = len(ability)
    num_sports = len(ability[0])
    
    # 가능한 모든 학생 배치의 순열을 생성
    max_total_ability = 0
    for perm in permutations(range(num_students), num_sports):
        
        current_total = 0
        for i in range(num_sports):
            student_index = perm[i]
            current_total += ability[student_index][i]
            
        max_total_ability = max(max_total_ability, current_total)
    
    return max_total_ability


print("정답 :" , solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
for perm in permutations(range(5), 3):
    print(perm)
# ability	result
# [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]	210
# [[20, 30], [30, 20], [20, 30]]	60