# 절댓값..

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())

heap = []
res = []
for _ in range(N):
    x = int(stdin.readline().rstrip())

    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if len(heap) == 0:
            res.append(0)
        else:
            res.append(heappop(heap)[1])
            
print(*res, sep='\n')

"""
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
"""

