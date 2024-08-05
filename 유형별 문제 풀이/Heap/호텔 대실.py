import heapq
def solution(book_time):
    answer = 0
    
    for i in book_time:
        h,m = i[0].split(':')
        H = int(h) * 60
        i[0] = H + int(m)
        h,m = i[1].split(':')
        H = int(h) * 60
        i[1] = H + int(m) + 10
        
    
    book_time = sorted(book_time, key=lambda x: x[0])
    
    heap = []
    
    for start,end in book_time:
        
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        heapq.heappush(heap,end)
    
    answer = len(heap)
        
    return answer