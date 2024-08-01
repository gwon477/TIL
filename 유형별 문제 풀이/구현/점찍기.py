def solution(k, d):
    answer = 0
    a = 0
    
    while a*k <= d:
        max_b_length = d**2 - (a*k)**2
        max_b = int((max_b_length**0.5)//k)
        print(max_b)
        answer += max_b + 1
        a += 1
    return answer

print(solution(1,5))

# k	d	result
# 2	4	6
# 1	5	26