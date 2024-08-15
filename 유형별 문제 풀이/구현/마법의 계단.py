def solution(storey):
    answer = 0
    current = storey
    
    while current > 0:
        remainder = current % 10  # 현재 자리수
        current //= 10  # 다음 자리수로 이동
        
        if remainder <= 5:
            answer += remainder
            
        else:
            answer += (10 - remainder)  # 10에서 현재 자리수를 빼고
            current += 1  # 올림 발생

    return answer

print(solution(95))