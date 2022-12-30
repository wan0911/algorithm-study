from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    
    for i in range(300000):
        if sum1 == sum2:
            return i
        
        elif sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())

        else:
            sum1 += q2[0]
            sum2 -= q2[0]
            q1.append(q2.popleft()) 
    return -1 
  
  
'''
queue1	queue2	result
[3, 2, 7, 2]	[4, 6, 5, 1]	2
[1, 2, 1, 2]	[1, 10, 1, 2]	7
[1, 1]	[1, 5]	-1
'''
