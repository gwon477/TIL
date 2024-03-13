# Linked List 구현

# Linked List는 Node를 생성하는 클래서, 첫 노드를 지정하는 Start, 노드를 연결하는 next 등이 필요하다.
# Linked List는 중간에 데이터를 "추가"하거나 "삭제"하는 경우에 고려해 볼 수 있다.


# 노드를 생성하는 클래스
class Node:
    # 처음 node를 생성하면 값 = 0 , 다음 노드 주소값,이전 노드 주소값을 모두 None 으로 초기화 한다.
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# LinkedList를 정의하는 클래스
class LinkedList(object):
    # LinkedList 초기 값.
    # 처음에는 시작위치와 현재 위치가 동일하다.
    def __init__(self,val):
        self.head = self.current = Node(value=val)
    # 다음 노드를 지정
    def nextNode(self,nextValue):
        self.current.next = Node(value=nextValue, prev=self.current)
        self.current = self.current.next
        return None
    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -=1
            self.current = self.current.prev
        return self.current.value
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -=1
            self.current = self.current.next
        return self.current.value
        

first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6
