from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
q = [-100] * 7  # inf로 하는게 나을듯
for _ in range(N):
    a = float(input())
    if -q[0] > a:
        heappop(q)
        heappush(q, -a)  # 최대 힙, 역순으로 대입

q.sort(reverse=True)
for n in q:
    print("{:.3f}".format(-n))
