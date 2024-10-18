# import sys
# from itertools import combinations

# # 입력 받기
# L, C = map(int, sys.stdin.readline().split())
# alphabet = sorted(sys.stdin.readline().split())  # 정렬된 알파벳

# # 모음 정의
# vowels = set("aeiou")

# # 가능한 암호 조합을 찾는 함수
# def is_valid(password):
#     # 모음과 자음 개수 세기
#     vowel_count = 0
#     consonant_count = 0
#     for p in password:
#         if p in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
 
#     # 모음이 최소 1개, 자음이 최소 2개인지 확인
#     if vowel_count >= 1 and consonant_count >= 2:
#         return True
#     else:
#         return False

# # 주어진 알파벳에서 L개의 조합을 구함
# for password in combinations(alphabet, L):
#     #print(password)
#     if is_valid(password):
#         print(''.join(password))


a =['a','t','c','i']
a.sort()
print(a)