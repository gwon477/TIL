def solution(routes):
    answer = 0
    N = len(routes)
    # 나가는 지점을 기준으로 정렬
    SR = sorted(routes, key=lambda x:x[1])
    print(SR)
    camera = 1
    camera_position = SR[0][1]
    
    for i in range(1,N):
        if SR[i][0] > camera_position:
            camera += 1
            camera_position = SR[i][1]
    answer = camera
    return answer

# 테스트 케이스
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # Output: 2


    