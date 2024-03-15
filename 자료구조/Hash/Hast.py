# python 에서 hash table은 dictionary로 구현된다.
# dictionary의 key-value 특성을 이용하면 O(1)의 시간 복잡도로 값에 접근할 수 있다.add()

# 대표 예제 : TWO SUM 문제

# 입력받은 값을 dictionary에 저장한다.
# for 루프 : O(N)

# def two_sum(nums,target):
#     dic = {}
#     for _ in nums:
#         dic[_] = 1
        
#     for _ in nums:
#         dic[_] = 0
#         k = target - _
#         if (k in dic) and (dic[k] != 0):
#             return(True)
#     return(False)

# # 입력 받기
# import sys

# t = int(sys.stdin.readline().strip())
# n = list(map(int,sys.stdin.readline().strip().split()))

# print(two_sum(n,t))

#================================================================================================================================================
# 대표 예제 : Longest Consecutive Sequence  문제
# 풀이 방식 : 정렬을 활용

import sys

nums = list(map(int,sys.stdin.readline().strip().split()))

# def solSort(nums):
#     cnt = 1
#     res = 1
#     # nums를 정렬
#     # 시간복잡도 O(NlogN)
#     nums.sort()
        
#     for i in range(len(nums)-1):
#         if nums[i]+1 == nums[i+1]:
#             cnt += 1
#         else:
#             res = max(res, cnt)
#             cnt = 0 
#     res = max(res, cnt)
    
#     return res

# print(solSort(nums))


# 풀이방식 : Hash map

def solHash(nums):
    dic = {}
    res = 0
    
    for _ in nums:
        dic[_]= 1
    
    for num in dic:
        if num-1 not in dic:
            cnt = 1
            target = num + 1
            while target in dic:
                target +=1
                cnt +=1
            res = max(res,cnt)
    return res

print(solHash(nums))
