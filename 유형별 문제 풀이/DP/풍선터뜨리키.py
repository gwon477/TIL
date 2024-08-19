def solution(a):
    n = len(a)
    
    # Step 1: Create the left_min array
    left_min = [0] * n
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    # Step 2: Create the right_min array
    right_min = [0] * n
    right_min[-1] = a[-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    
    # Step 3: Determine the number of balloons that can be the last one left
    count = 0
    for i in range(n):
        # A balloon can be the last one if it's less than or equal to
        # either the left_min of its left side or the right_min of its right side.
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1
    
    return count



k = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
b = [9, -1, -5]

print(solution(k))

# 최후까지 남을 수 있는 풍선은 -16, -92, -71, -68, -61, -33이 써진 풍선으로 모두 6개입니다.