# 문제 설명
# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
# wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
# 1 ≤ v1 < v2 ≤ n 입니다.
# 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

from collections import deque  # deque를 사용하기 위해 추가

def solution(n, wires):
    q = deque(wires)  # 초기화를 더 간단하게
    r = []

    def build_graph(exclude):
        # exclude 인덱스를 제외하고 그래프를 생성
        dic = {}
        for i, w in enumerate(wires):
            if i == exclude:
                continue
            if w[0] in dic:
                dic[w[0]].append(w[1])
            else:
                dic[w[0]] = [w[1]]
            if w[1] in dic:
                dic[w[1]].append(w[0])
            else:
                dic[w[1]] = [w[0]]
        return dic

    for i in range(len(wires)):
        dic = build_graph(i)  # 링크를 제외하고 그래프를 다시 만듬
        
        visited = set()
        queue = deque([wires[i][0]])  # 시작점을 임의로 정함

        while queue:
            cur_v = queue.popleft()
            if cur_v not in visited:
                visited.add(cur_v)
                if cur_v in dic:
                    for _ in dic[cur_v]:
                        if _ not in visited:
                            queue.append(_)

        r.append(abs(len(visited)-(n-len(visited))))
        
    answer = min(r)
    return answer
