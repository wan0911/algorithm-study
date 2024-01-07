import sys
from collections import deque

q = deque()
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif cmd[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif cmd[0] == 'back':
        if q: print(q[-1])
        else: print(-1)

          
'''
- input
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

- output
1
2
2
0
1
2
-1
0
1
-1
0
3
'''
