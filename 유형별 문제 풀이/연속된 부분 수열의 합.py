def solution(sequence, k):
    answer = []
    N = len(sequence)
    start = 0
    end = 1
    
    shortest = 1000000
    
    while end <= N:
        if end == N:
            start += 1
        
        if sum(sequence[start:end]) < k:
            end += 1
            continue
            
        elif sum(sequence[start:end]) > k:
            start += 1
            continue
            
        else:
            if len(sequence[start:end]) < shortest:
                answer = [start,end-1]
                start = end
                end += 1
                continue

    return answer

print(solution([1, 1, 1, 2, 3, 4, 5],5))