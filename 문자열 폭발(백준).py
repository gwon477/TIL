import sys

string = str(sys.stdin.readline().strip())
bumb = str(sys.stdin.readline().strip())

def explode_string(s, bomb):
    stack = []
    bomb_length = len(bomb)
    
    for char in s:
        stack.append(char)
        # 폭발 문자열 길이만큼 쌓였을 때 확인
        if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]  # 폭발 문자열 삭제
    
    result = ''.join(stack)
    return result if result else "FRULA"

print(explode_string(string,bumb))

st = []

for _ in string:
    st.append(_)
    if len(st) >= len(bumb) and ''.join(st[-len(bumb):]) == bumb:
        print(st)
        del st[-len(bumb):]

