from collections import deque

queue = deque()
# enqueue: 뒤에서 Insert, O(1)
queue.append()
# dequeue: 앞에서 pop, O(1)
queue.popleft()

# 시간복잡도 때문에 linked List로 구현
# 코테에서 단독으로 쓰이지 않음, 다른 개념과 함께 쓰임
