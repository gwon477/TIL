
# 단순 조합

# def sol(nums,k):
#     result = []
    
#     def backtraking(start,curr):
#         if len(curr) == k:
#             result.append(curr[:])
#             return
#         for i in range(start, len(nums)):
#             curr.append(nums[i])
#             backtraking(i+1,curr)
#             curr.pop()
        
#     backtraking(start=0,curr=[])
#     return result

# print(sol(nums=[1,2,3,4],k=2))


# 부분 집합 문제 응용
def sol(nums):
    result = []
    
    def backtraking(start,curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtraking(i+1,curr)
            curr.pop()
    for k in range(len(nums)+1):
        backtraking(start=0,curr=[])
    return result

print(sol(nums=[1,2,3,4]))