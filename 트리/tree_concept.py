class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class NodeMgmt:
    def __init__(self, head):
        self.curr = self.head    # head = Node()
    
    ''' 데이터 적절한 위치에 삽입 '''
    def insert(self, data):
        # 그래프 탐색
        while True:
            if data < self.curr.left:
                if self.curr.left != None:
                    self.curr = self.curr.left
                else:
                    self.curr.left = Node(data)
                    break
                
            else:
                if self.curr.right != None:
                    self.curr = self.curr.right
                else:
                    self.curr.right = Node(data)
                    break
    
    ''' 데이터 탐색 = 트리에 존재하는 지 판단 '''
    def search(self, data):
        self.curr = self.head
        
        while self.curr:     # 없으면 None
            if self.curr.data == data:
                return True
            elif data < self.curr.data:
                self.curr = self.curr.left
            else:
                self.curr = self.curr.right
        return False
    
    ''' 데이터 삭제 '''
    def delete(self, data):
        searched = False
        self.curr = self.head
        self.parent = self.head
        
    # 삭제할 노드가 존재하지 않는 경우
        while self.curr:
            if self.curr.data == data:
                searched = True
                break
            elif data < self.curr.data:
                self.parent = self.curr
                self.curr = self.curr.left
            else:
                self.parent = self.curr
                self.curr = self.curr.right

        if searched == False:
            return False
        
        ## node 찾았음
        ## data == 삭제할 노드 값
        
        # 1. 삭제할 노드가 leaf node인 경우
        if self.curr.left == None and self.curr.right == None:
            if data < self.parent.data:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.curr    # curr node를 삭제해줘야 한다.(메모리)

        
        # 2. 삭제할 노드가 child node를 1개 가지고 있는 경우
        ## 2.1 왼쪽 child node를 가질 경우
        if self.curr.left != None and self.curr.right == None:
            if data < self.parent.data:     # parent의 left
                self.parent.left = self.curr.left
            else:                           # parent의 right 
                self.parent.right = self.curr.left
            
        ## 2.2 오른쪽 child node를 가질 경우
        elif self.curr.left == None and self.curr.right != None:
            if data < self.parent.data:
                self.parent.right = self.curr.left
            else:
                self.parent.right = self.curr.right
        
        
        # 3. 삭제할 노드가 child node를 2개 가지고 있는 경우
        ## 3.1 삭제할 node가 parent left에 존재
        ### 3.1.1 자식 중 가장 작은 값 node가 child node 없는 경우
        ### 3.1.2 자식 중 가장 작은 값 node가 child node 존재하는 경우
        
        if self.curr.left != None and self.curr.right != None:
            if data < self.parent.data:
                self.change_node = self.curr.right
                self.change_node_parent = self.curr.right
                
                while self.change_node.left != None:    # change_node 찾기
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                    
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                    
                
                
                
                
                
        
        
        ## 3.2 삭제할 node가 parent right에 존재
        
        
        