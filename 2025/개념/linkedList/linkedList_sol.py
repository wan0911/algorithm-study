# 뒤로가기, 앞으로가기 -> prev, next가 필요함 => linkedList? => doubly linkedList

# BrowserHistory: 시작
# visit: 앞 페이지들 삭제 * 앞 = forward 주의 !front
# back: 뒤로가기
# forward: 앞으로 가기


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


cur_val = None


class BrowserHistory:
    def __init__(self, value):
        new_node = Node(value)  # init 조건
        self.head = new_node

    def visit(self, value):  # append + 조건
        # 1. 앞 페이지들 삭제 -> cur.next 연결 끊기
        # 2. cur.next = new node
        # + 현재 idx를 어떻게 파악? -> global 변수로 저장?
        # => 구현을 idx로 접근함, class의 객체 속성(current)를 이용하면 됨
        # => idx로 구현하려 했다면.. array로 풀이하는 방법이 있음
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head  # start point -> 여기가 다르던가?
            while curr.value != cur_val:
                curr = curr.next
            curr.next = new_node
        cur_val = value

    def back(self, value, idx):
        curr = self.head
        while idx까지
            curr을 prev로 이동
        pass

    def forward(self, value, idx):
        pass
