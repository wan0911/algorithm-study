# 최대 힙

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())
heap = []
res = []
for _ in range(N):
    x = int(stdin.readline().rstrip())

    if x != 0:
        heappush(heap, -x)
    else:
        if len(heap) != 0:
            res.append(-heappop(heap))
        else:
            res.append(0)

print(*res, sep="\n")


"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""
