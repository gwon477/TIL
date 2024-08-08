## 💯 Python & MySQL Coding Challenges Repository

이 레포지토리는 코딩 테스트 및 기술 면접을 대비하여 알고리즘 문제 풀이와 SQL 쿼리 문제들로 구성되었습니다.
문제는 다양한 출처에서 가져오며, 각 문제의 풀이 과정과 결과를 정리합니다.


<br>

### 🔖 알고리즘 목차
- [유형1: 정렬](#유형1-정렬)
- [유형2: 그래프](#유형2-그래프)
- [유형3: 동적 프로그래밍](#유형3-동적-프로그래밍)
- [유형4: 해쉬](#유형4-해쉬)
- [유형5: 힙](#유형5-힙)
- [유형6: 스택](#유형6-스택)
- [유형7: 구현](#유형7-구현)
- [유형8: 그리디](#유형8-그리디)
- [유형9: 백트래킹](#유형9-백트래킹)
- [유형10: 탐색](#유형10-탐색)
- [유형11: 재귀](#유형11-재귀)
- [유형12: 문자열](#유형12-문자열)


### SQL 목차
- [유형1: GROUP BY](#유형1-GROUP-BY)
- [유형2: JOIN](#유형2-JOIN)
- [유형3: SELECT](#유형3-SELECT)
- [유형4: STRING/DATE](#유형4-STRING/DATE)
- [유형5: IS NULL](#유형5-IS-NULL)


<br>

---



<details>
<summary><strong id="유형1-정렬"> 유형1: 정렬</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| H-Index | 조건 정렬 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/42747) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EC%A0%95%EB%A0%AC/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/H-Index.py) | 🔥 |
| | | | | | | |
| 단어 정렬 | 조건 정렬 | 백준 | Silver 5 | [문제](https://www.acmicpc.net/problem/1181) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EC%A0%95%EB%A0%AC/%EC%A0%95%EB%A0%AC(1181%EB%B2%88).py) | 🔥 |

</details>


<details>
<summary><strong id="유형2-그래프"> 유형2: 그래프</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 미로 탈출 | BFS | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/159993) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EB%A0%88%EB%B2%84_%EB%AF%B8%EB%A1%9C%ED%83%88%EC%B6%9C.py) | 🔥 |
| 리코쳇 로봇 | BFS | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/169199) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EB%A6%AC%EC%BD%94%EC%B3%87%EB%A1%9C%EB%B4%87.py) | 🔥 |
| 석유 시추 | BFS | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/250136) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EC%84%9D%EC%9C%A0%EC%8B%9C%EC%B6%94.py) | 🔥 |
| 부대 복귀 | BFS | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/132266) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EB%B6%80%EB%8C%80%EB%B3%B5%EA%B7%80.py) | 🔥 |
| 가장 먼 노드 | BFS | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/49189) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EA%B0%80%EC%9E%A5%EB%A8%BC%EB%85%B8%EB%93%9C(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4).py) | 🔥 |
| 여행경로 | BFS | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/43164) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C.py) | 🔥 |
| | | | | | | |
| 단지번호붙이기 | BFS | 백준 | Silver 1 | [문제](https://www.acmicpc.net/problem/2667) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/2667%EB%B2%88.py) | 🔥 |
| 아기 상어 | BFS | 백준 | Gold 3 | [문제](https://www.acmicpc.net/problem/16236) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%EC%95%84%EA%B8%B0%EC%83%81%EC%96%B4.py) | 🔥 |
| 토마토 | BFS | 백준 | Gold 5 | [문제](https://www.acmicpc.net/problem/7576) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Graph/%ED%86%A0%EB%A7%88%ED%86%A0.py) | 🔥 |

</details>

<details>
<summary><strong id="유형3-동적-프로그래밍"> 유형3: 동적 프로그래밍</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 체육대회 | DP | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/15008/lessons/121684) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/DP/%5BPCCP%20%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%231%5D%202%EB%B2%88%20-%20%EC%B2%B4%EC%9C%A1%EB%8C%80%ED%9A%8C.py) | 🔥 |
| 땅따먹기 | DP | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/12913) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/DP/%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0.py) | 🔥 |
| 풍선 터트리기 | DP | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/68646) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/DP/%ED%92%8D%EC%84%A0%ED%84%B0%EB%9C%A8%EB%A6%AC%ED%82%A4.py) | 🔥 |
| | | | | | | |
| 가장 큰 증가하는 부분 수열 | DP | 백준 | Silver 2 | [문제](https://www.acmicpc.net/problem/11055) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/DP/11055%EB%B2%88.py) | 🔥 |
| 1로 만들기 | DP | 백준 | Silver 3 | [문제](https://www.acmicpc.net/problem/1463) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/DP/1463%EB%B2%88.py) | 🔥 |

</details>

<details>
<summary><strong id="유형4-해쉬"> 유형4: 해쉬</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 폰캣몬 | Hash | 프로그래머스 | Lv 1 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/1845) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Hash/hash(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%3A%ED%8F%AC%EC%BC%93%EB%AA%AC).py) | 🔥 |
| | | | | | | |
| 숫자 카드 2 | 해시를 사용한 집합과 맵 | 백준 | Silver 4 | [문제](https://www.acmicpc.net/problem/10816) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Hash/hash(10816%EB%B2%88).py) | 🔥 |
| 숫자 카드 | 해시를 사용한 집합과 맵 | 백준 | Silver 5 | [문제](https://www.acmicpc.net/problem/10815) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Hash/hash(10815%EB%B2%88).py) | 🔥 |

</details>

<details>
<summary><strong id="유형5-힙"> 유형5: 힙</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 디팬스 게임 | 우선 순위 큐 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/142085) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/%EB%94%94%ED%8E%9C%EC%8A%A4%EA%B2%8C%EC%9E%84.py) | 🔥🔥 |
| 호텔 대실 | 우선 순위 큐 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/155651) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/%ED%98%B8%ED%85%94%20%EB%8C%80%EC%8B%A4.py) | 🔥 |
| | | | | | | |
| 최소 힙 | 우선 순위 큐 | 백준 | Silver 2 | [문제](https://www.acmicpc.net/problem/1927) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/Haapq.py) | 🔥🔥 |

</details>

<details>
<summary><strong id="유형6-스택"> 유형6: 스택</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 프린터 큐 | 스택 | 백준 | Silver 2 | [문제](https://www.acmicpc.net/problem/1966) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Stack/1966.py) | 🔥 |
| 단어 뒤집기 2 | 스택 | 백준 | Silver 3 | [문제](https://www.acmicpc.net/problem/17413) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Stack/stack(17413%EB%B2%88).py) | 🔥 |
| 괄호 | 스택 | 백준 | Silver 4 | [문제](https://www.acmicpc.net/problem/9012) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Stack/stack(9012%EB%B2%88).py) | 🔥 |

</details>

<details>
<summary><strong id="유형7-구현"> 유형7: 구현</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 외톨이 알파벳 | 구현 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/15008/lessons/121683) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B5%AC%ED%98%84/%5BPCCP%20%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%231%5D%201%EB%B2%88%20-%20%EC%99%B8%ED%86%A8%EC%9D%B4%20%EC%95%8C%ED%8C%8C%EB%B2%B3.py) | 🔥 |
| 호텔 대실 | 구현 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/155651) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B5%AC%ED%98%84/%5BPCCP%20%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%231%5D%204%EB%B2%88%20-%20%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C.py) | 🔥 |
| 점찍기 | 구현 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/140107) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/%ED%98%B8%ED%85%94%20%EB%8C%80%EC%8B%A4.py) | 🔥 |
| 최고의 집합 | 구현 | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/12938) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/Haapq.py) | 🔥 |
| 합승 택시 요금 | 구현 | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/72413) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/%EB%94%94%ED%8E%9C%EC%8A%A4%EA%B2%8C%EC%9E%84.py) | 🔥 |
| | | | | | | |
| 수열 | 구현 | 백준 | Silver 4 | [문제](https://www.acmicpc.net/problem/2491) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/Haapq.py) | 🔥 |
| 비슷한 단어 | 구현 | 백준 | Silver 2 | [문제](https://www.acmicpc.net/problem/2607) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B5%AC%ED%98%84/2607%EB%B2%88.py) | 🔥 |
| 상어 초등학교 | 구현 | 백준 | Gold 5 | [문제](https://www.acmicpc.net/problem/21608) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/Heap/%EB%94%94%ED%8E%9C%EC%8A%A4%EA%B2%8C%EC%9E%84.py) | 🔥🔥 |
</details>

<details>
<summary><strong id="유형8-그리디"> 유형8: 그리디</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 요격 시스템 | 그리디 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/181188) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B7%B8%EB%A6%AC%EB%94%94/%EC%9A%94%EA%B2%A9%EC%8B%9C%EC%8A%A4%ED%85%9C.py) | 🔥 |
| 단속 카메라 | 그리디 | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B7%B8%EB%A6%AC%EB%94%94/%EB%8B%A8%EC%86%8D%EC%B9%B4%EB%A9%94%EB%9D%BC.py) | 🔥 |
| | | | | | | |
| 주식 | 그리디 | 백준 | Lv 2 | [문제](https://www.acmicpc.net/problem/11501) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B7%B8%EB%A6%AC%EB%94%94/%EC%A3%BC%EC%8B%9D.py) | 🔥🔥 |
| 타노스 | 그리디 | 백준 | Lv 2 | [문제](https://www.acmicpc.net/problem/20310) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EA%B7%B8%EB%A6%AC%EB%94%94/%ED%83%80%EB%85%B8%EC%8A%A4.py) | 🔥🔥 |

</details>


<details>
<summary><strong id="유형9-백트래킹"> 유형9: 백트래킹</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| N-Q | 백트래킹 | 백준 | Gold 5 | [문제](https://www.acmicpc.net/problem/9663) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EB%B0%B1%ED%8A%B8%EB%A0%88%ED%82%B9/N-Q.py) | 🔥 |

</details>


<details>
<summary><strong id="유형10-탐색"> 유형10: 탐색</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 입국 심사 | 탐색 | 프로그래머스 | Lv 3 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/43238) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89/%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4).py) | 🔥 |
| | | | | | | |
| 제곱근 | 이분 탐색 | 백준 | Silver 4 | [문제]https://www.acmicpc.net/problem/13706) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89/%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89(13706%EB%B2%88).py) | 🔥 |

</details>


<details>
<summary><strong id="유형11-재귀"> 유형11: 재귀</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| 하노이 팁 | 재귀 | 프로그래머스 | Lv 2 | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/12946) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4/%EC%9E%AC%EA%B7%80/%ED%95%98%EB%85%B8%EC%9D%B4%ED%83%91.py) | 🔥 |

</details>


<details>
<summary><strong id="유형12-문자열"> 유형12: 문자열</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
| LCS | 문자열 부분 집합 | - | - | [문제](https://www.acmicpc.net/problem/1927) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95/%EB%AC%B8%EC%9E%90%EC%97%B4/LCS.py) | 🔥 |
| LPS(KMP) | 문자 패턴 확인 | - | - | [문제](https://school.programmers.co.kr/learn/courses/30/lessons/142085) | [풀이](https://github.com/gwon477/TIL/blob/main/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95/%EB%AC%B8%EC%9E%90%EC%97%B4/LPS(%3DKMP).py) | 🔥 |

</details>

<br>


[목차로](#-알고리즘-목차)


---

- [유형1: GROUP BY](#유형1-GROUP-BY)
- [유형2: JOIN](#유형2-JOIN)
- [유형3: SELECT](#유형3-SELECT)
- [유형4: STRING/DATE](#유형4-STRING/DATE)
- [유형5: IS NULL](#유형5-IS-NULL)

<details>
<summary><strong id="유형1-GROUP-BY"> 유형1: GROUP BY</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
|  |  |  |  | [문제]() | [풀이]() | 🔥 |

</details>

<details>
<summary><strong id="유형2-JOIN"> 유형2: JOIN</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
|  |  |  |  | [문제]() | [풀이]() | 🔥 |

</details>

<details>
<summary><strong id="유형3-SELECT"> 유형3: SELECT</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
|  |  |  |  | [문제]() | [풀이]() | 🔥 |

</details>

<details>
<summary><strong id="유형4-STRING/DATE"> 유형4: STRING/DATE</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
|  |  |  |  | [문제]() | [풀이]() | 🔥 |

</details>

<details>
<summary><strong id="유형5-IS-NULL"> 유형5: IS NULL</strong></summary>

| 문제 이름 | 세부 유형 | 출처 | 난이도 | [문제](#) | [풀이](#) | 풀이 횟수 |
|:-----------------:|:------------:|:------:|:----:|:-------:|:-------:|:--------:|
|  |  |  |  | [문제]() | [풀이]() | 🔥 |

</details>



[목차로](#-SQL-목차)





---

### 💡 설명

다양한 알고리즘 문제를 풀고, 풀이 과정을 기록하는 것을 목표로 합니다. 각 문제는 출처, 문제 링크, 풀이 링크, 풀이 횟수 등의 정보와 함께 정리됩니다. 문제 풀이 과정에서 배운 점과 개선할 점을 기록하여, 꾸준히 알고리즘 실력을 향상시키는 것을 목적으로 합니다.
<br>