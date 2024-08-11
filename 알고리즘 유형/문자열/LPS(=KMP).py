# 해설 참고 : https://www.youtube.com/watch?v=DgOloMoml54

# - **정의:** 두 문자열에서 공통으로 나타나는 가장 긴 부분 수열을 찾는 문제입니다. 부분 수열(subsequence)은 문자열 내에서 문자들의 순서를 유지하면서 일부 문자를 제거한 문자열입니다.

# - **예시:**
#     - 문자열 `X = "ABCBDAB"`와 `Y = "BDCAB"`의 LCS는 `"BCAB"`입니다. 이 LCS의 길이는 4입니다.
    
# - **알고리즘:** LCS는 주로 동적 프로그래밍(Dynamic Programming)을 사용하여 2차원 DP 테이블을 채우는 방식으로 해결합니다.


def kmp_map(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1    
    
    return lps


def use_kmp(text, pattern):
    answer = []
    
    lps = kmp_map(pattern=pattern)
    
    i = 0
    j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            j += 1
            i += 1
            
        if j == len(pattern):
            answer.append(i-j)
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return answer

print(use_kmp("ABC ABCDAB ABCDABCDABDE","ABCDABD"))



# text = "ABC ABCDAB ABCDABCDABDE"
# pattern = "ABCDABD"

# result = kmp_search(text, pattern)
# print("패턴이 발견된 인덱스들:", result)
