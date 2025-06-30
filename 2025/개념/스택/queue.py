# FIFO: 한쪽 끝으로 넣고, 반대쪽으로 뺀다
# 순서대로 처리해야할 때
# 데이터를 넣고 빼고를 자주해야하니.. linkedList 활용


class Node:
    def __init__(self, value):
        self.data = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enquue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self, value):
        if self.isEmpty():
            return "Queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.head.data

    def isEmpty(self):
        return self.head is None
