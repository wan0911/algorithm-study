# 최소 힙
# N 범위
# 자연수 = 입력 push, 0 = 가장 작은 값 pop

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())
program = []

for _ in range(N):
    n = int(stdin.readline().rstrip())

    if n == 0:
        if len(program) == 0:
            print(0)
            continue

        # 최소 값 출력
        print(heappop(program))

    else:
        heappush(program, n)
