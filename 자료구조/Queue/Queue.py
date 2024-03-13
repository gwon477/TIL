# Queue는 시간 순서상 먼저 저장한 데이터가 먼저 출력되는 선입선출 FIFO(First In First Out) 형식으로 데이터를 저장하는 자료구조.
# queue의 rear에 데이터를 추가하는 것을 enqueue라고 한다.
# queue의 front에서 데이터를 꺼내는 것을 dequeue라고 한다.

# queue는 Array, Linked 리스트 두가지로 모두 구현할 수 있다.



#=============================================================
# Array List로 queue를 구현하면 O(n)만큼의 시간복잡도가 필요하다.
# Array 배열 선언
q = []

# Array에서 enqueue
q.append(7)
q.append(7)
q.append(7)
q.append(7)

# Array에서 dequeue
# 0 번째 인덱스를 꺼내기 위해서 꺼낼 때마다 인덱스를 하나씩 앞당겨야한다.
q.pop(0)
q.pop(0)
q.pop(0)
#=============================================================
# LinkedList로 구현하면 deque를 사용한다.
from collections import deque
queue = deque()
# LinkedList에서 enqueue
queue.append(7)
queue.append(7)
queue.append(7)
queue.append(7)

# LinkedList에서 dequeue
queue.popleft()
queue.popleft()
queue.popleft()