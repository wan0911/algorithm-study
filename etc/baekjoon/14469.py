# 도착시간, 검문시간
# 동시 검문 x, 모든 소 입장, 최소 시간
# 정렬... a + b 합친게 작은 순? ->도착 순으로..

from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort()

time = 0
time += sum(data.pop(0))
for a, b in data:
    if time <= a:
        time = a + b
        continue
    elif time > a:
        time += b

print(time)
