from collections import deque

def solution(program):
    answer = []
    FT = 0
    JFT = [0] * 10
    
    print("전체 종료 시간 :", FT)
    print("각 큐 별 종료 시간 : ", JFT)
    
    sorted_program = sorted(program, key= lambda x:(x[1],x[0]))
    print("호출 시간 기준으로 정렬된 큐:",sorted_program)
    queue = deque()

    #스케줄 생성
    for _ in sorted_program:
        queue.append(_)
        break
        
    print(queue)
    
    c_time = 0
    K = 0
    priortity = 11
    
    visit = [False for i in range(len(sorted_program))]
    visit[0] = True
    
    while queue:
        c_score, c_call, c_delay = queue.popleft()
        print("실행중인 스케줄 정보 :", c_score, c_call, c_delay)
        print(visit)
        JFT[c_score] += c_time - c_call
        K += 1
        visit_index = 0
        # 스케줄 별 종료 시간
        c_time += c_delay
        
        if all(visit):
            break
   
        for i in range(1,len(sorted_program)):
            if sorted_program[i][1] < c_time:
                #N += 1
                if sorted_program[i][0] < priortity and not visit[i]:
                        priortity = sorted_program[i][0]
                        next_scadule = sorted_program[i]
                        visit_index = i
                        print("다음 정보 : ",next_scadule)
        
        
        priortity = 11
        visit[visit_index] = True           
        queue.append(next_scadule)
        
                
    answer.append(c_time)
    for i in range(1,len(JFT)):
        answer.append(JFT[i])

    return answer

#print("answer :", solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
print("answer :", solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))

# program	result(answer)
# [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]	[20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
# [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]	[19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]

# 1 ≤ program의 길이 ≤ 100,000
# program[i]은 i+1번 프로그램의 정보를 의미하며, [a, b, c]의 형태로 주어집니다.
# a는 프로그램의 점수를 의미하며, 1 ≤ a ≤ 10 을 만족합니다.
# b는 프로그램이 호출된 시각을 의미하며, 0 ≤ b ≤ 10,000,000을 만족합니다.
# c는 프로그램의 실행 시간을 의미하며, 1 ≤ c ≤ 1,000을 만족합니다.
# a, b쌍이 중복되는 프로그램은 입력으로 주어지지 않습니다. 즉, 호출된 시각이 같으면서 점수도 같은 프로그램은 없습니다.