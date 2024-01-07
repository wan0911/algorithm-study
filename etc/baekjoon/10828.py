import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    a = sys.stdin.readline().split()
    order = a[0]

    if order == 'push':
        q.append(a[1])
    elif order == 'pop':
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
