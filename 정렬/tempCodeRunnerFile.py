class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head   # node1
        while node:
            print (node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:  # 삭제할 데이터가 head인 경우
            # temp = self.head
            self.head = self.head.next
            # del temp
        else:   
            node = self.head    # head가 아닌 경우
            while node.next:    # 노드 탐색 후 삭제
                if node.next.data == data:
                    # temp = node.next
                    node.next = node.next.next
                    # del temp
                    return
                else:
                    node = node.next
                    
''' 삭제 확인 '''
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for i in range(1,10):
    linkedlist1.add(i)
      
linkedlist1.delete(5)
linkedlist1.desc()