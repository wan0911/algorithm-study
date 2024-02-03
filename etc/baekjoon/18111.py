# 평탄화 작업 
# 1번(제거) - 2초 / 2번(추가) - 1초
# 모든 배열이 같은 숫자가 될 때까지
# N = 행, M = 열

from sys import stdin 
from collections import Counter

N, M, B = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
graph = [data for g in graph for data in g]


time = [0 for i in range(257)]
height = 0
for h in range(257):  # 땅 높이
    blocks = B

    for g in graph:
        # 1. 제거
        if g > h:
            blocks += (g - h)
            time[h] += (g - h) * 2

        # 2. 추가
        else:
            blocks -= (h - g)
            time[h] += (h - g) * 1
            
    # blocks < 0 일 때, 바로 break하면 안됨 → 순차적이 아님 → 전체 total값이 0보다 작은지 봐야 함
    if blocks >= 0 and time[h] <= time[height]:
        height = h

print(time[height], height)