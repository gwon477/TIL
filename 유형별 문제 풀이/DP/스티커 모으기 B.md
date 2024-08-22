## 스티커 모으기 B[Link](https://school.programmers.co.kr/learn/courses/30/lessons/12971)

### ❑ 문제
N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.

![img](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d8d3a8b3-606c-4fb6-baf2-3a96cb53d70c/%E1%84%89%E1%85%B3%E1%84%90%E1%85%B5%E1%84%8F%E1%85%A5_hb1jty.jpg)


원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.


예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.


<br>

### ❑ 제한사항
    - sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.

    - sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.

    - 원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

<br>

### ❑ 입출력 예
| sticker | answer |
|:-----------------:|:------------:|
|[14, 6, 5, 11, 3, 9, 2, 10]|36|
|[1, 3, 2, 5, 4]|8|


<br>

### ❑ 입출력 예 설명
입출력 예 #1

6, 11, 9, 10이 적힌 스티커를 떼어 냈을 때 36으로 최대가 됩니다.


입출력 예 #2

3, 5가 적힌 스티커를 떼어 냈을 때 8로 최대가 됩니다.

<br>

### ✅ 접근
- 원형 형태의 판인 것이 포인트
- 첫번째 스티커를 선택했을 경우, 선택하지 않은 경우를 나눠서 계산
- DP를 사용해서 이전 경우의 수 중 합이 가장 큰 값을 유지

<br>


### ❑ 코드
```Python
def solution(sticker):
    N = len(sticker)
    
    # 스티커가 하나인 경우 바로 반환
    if N == 1:
        return sticker[0]
    
    # 첫 번째 스티커를 선택한 경우
    dpA = [0 for i in range(N)]
    dpA[0] = sticker[0]
    dpA[1] = max(sticker[0], sticker[1])
    
    for i in range(2, N - 1):  # 마지막 스티커는 선택하지 않음
        dpA[i] = max(dpA[i-1], dpA[i-2] + sticker[i])
        print("dpA:",dpA)
    
    # 첫 번째 스티커를 선택하지 않은 경우
    dpB = [0 for i in range(N)]
    dpB[1] = sticker[1]
    
    for i in range(2, N):  # 마지막 스티커까지 포함 가능
        dpB[i] = max(dpB[i-1], dpB[i-2] + sticker[i])
        print("dpB:",dpB)
    
    # 두 경우 중 최대값 반환
    # N-2인 이유 : 원으로 이어져있기 때문에 마지막 값은 고를 수 없음
    return max(dpA[N-2], dpB[N-1])



```