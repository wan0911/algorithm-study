# linkedList는 비연속적이므로 head부터 탐색해서 가야한다. -> O(n)
# linkedList는 코테 단골 소재는 아니지만, 이후 tree / graph를 학습하기 위해 배워야 한다


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None  # insert_back

    # O(n)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while self.next:  # self.next is None
                current = current.next
            current.next = new_node

    # O(1): insert_back
    def append2(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    # O(n)
    def insert(self, idx):
        current = self.head
        NewNode = Node()
        # insert하려는 앞 노드까지
        for i in range(idx - 1):
            current = current.next
        NewNode.next = current.next
        current.next = NewNode

    def remove(self, idx):
        current = self.head
        prevNode = None
        for i in range(idx):
            if i == idx - 1:
                prevNode = current
            current = current.next
        prevNode.next = current.next
