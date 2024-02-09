class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)   # head 설정
        
    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next    # curr 커서 이동
        return None
        
    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev    # curr 커서 이동
        return self.current.val
        
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next    # curr 커서 이동
        return self.current.val
        
        
# head, current, tail = "pointer"


## array_list로도 풀어보기