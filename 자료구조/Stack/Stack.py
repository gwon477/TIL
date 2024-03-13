# Stack은 시간 순서상 가장 최근에 추가한 데이터가 가장 먼저 나오는 후입선출 LIFO(Last In First Out) 형식으로 데이터를 저장하는 자료구조
# stack의 top에 데이터를 추가하는 것을 push라고 하고 stack의 top에서 데이터를 추출 하는 것은 pop이라고 한다.

# Python에서 Stack = List 선언!!!!!!!!!!!!

# 대표 예제 : 괄호 유효성 검증
def isValid(s):
    stack = []
    for p in s: 
        if p == "(":
            stack.append(")")
        elif p =="{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack

result = isValid("{({[]}){}")
print(result)


# 대표 예제 : daily Temperature
def dailyTemperature(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day,cur_temp))
    return ans

result = dailyTemperature([73,74,75,71,69,72,76,73])
print(result)