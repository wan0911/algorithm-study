# 정리
# 1. 노드 구현
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

''' head node 설정 '''      
node1 = Node(1)
head = node1

# 2. 노드 추가 함수
def add(data):
    node = head     # head 부터 시작
    while node.next:
        node = node.next
    node.next = Node(data)   # next가 없는 마지막 노드를 찾으면 새로운 노드 연결

''' 확인용 데이터 2~9 추가  '''
for i in range(2, 10):
    add(i)
    
    
# 3. 노드 검색 함수
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)    # 마지막 찾은 노드 = next X




''' 복잡한 기능1. 링크드 리스트 사이 새로운 노드 삽입 '''
# 사이에 삽입할 노드
node3 = Node(1.5)

# 삽입 전 노드 구조 확인
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)


# 삽입 구현
node = head     # head = node1
search = True
while search:
    if node.data == 1:   # 링크드는 순서대로 X, 1.5를 삽입할거니까 1을 찾음
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next


# 삽입 확인
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)




''' 파이썬 객체지향.ver '''

# 노드 객체
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 노드 관리 객체 
# 노드 생성, 연결, 출력 한번에 관리
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            # 노드 탐색 후 연결
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):   # 노드 출력(검색)
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)
        

''' 확인 '''
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for i in range(1,10):
    linkedlist1.add(i)

linkedlist1.desc()     





''' 복잡한 기능2. 특정 노드 삭제 '''
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