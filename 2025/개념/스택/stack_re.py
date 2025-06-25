# 선입선출
# 한 곳에서만 자료를 넣고 뺄 수 있다
# 데이터를 넣고 빼는 작업이 많다 -> LinkedList로 구현


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# hea를 맨 처음 노드가 아니라, top 노드로 생각
# head
# 4 -> 5
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.isEmpty():
            return False

        temp = self.head.data
        self.head = self.next.head
        return temp

    def peak(self):
        if self.isEmpty():
            return False

        return self.head.data

    def isEmpty(self):
        return self.head is None


# 파이썬에서는 list를 이용해서 stack 처럼 활용 가능!
