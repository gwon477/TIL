import heapq
import math

def solution(jobs):
    # jobs를 요청 시간 순으로 정렬합니다.
    jobs.sort(key=lambda x: x[0])
    
    # 현재 시간 및 완료된 작업의 수, 총 대기 시간을 초기화합니다.
    current_time = 0
    completed_jobs = 0
    total_wait_time = 0
    
    # 대기 큐(최소 힙)
    heap = []
    
    # jobs의 인덱스를 위한 변수
    job_index = 0
    job_count = len(jobs)
    
    while completed_jobs < job_count:
        # 현재 시간까지 도착한 작업들을 힙에 추가합니다.
        while job_index < job_count and jobs[job_index][0] <= current_time:
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if heap:
            # 가장 실행 시간이 짧은 작업을 힙에서 꺼내 처리합니다.
            job_duration, job_start = heapq.heappop(heap)
            current_time += job_duration
            total_wait_time += current_time - job_start
            completed_jobs += 1
        else:
            # 힙이 비어있다면, 작업이 들어올 때까지 시간을 점프합니다.
            current_time = jobs[job_index][0]
    
    # 평균 대기 시간을 계산합니다. 소수점 이하 버림.
    return total_wait_time // job_count
