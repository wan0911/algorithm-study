# N, 칸: 0 = 빈 칸 / 1 = 치킨집 / 2 =  집
# r, c 1부터 시작
# 치킨 거리: 집 - 가장 가까운 치킨집 거리
# 도시 치킨 거리 = sum(치킨 거리)

# 일부 치킨집 제거, M개까지만 유지
# 도시 치킨 거리 "최소"

from sys import stdin
from collections import deque
from itertools import combinations

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]


# 1. M개 조합 별 도시 치킨 거리 추출
# 2. 그중에 최소가 되는 조합과 거리 파악
## 치킨 거리 구하기
## 집(1)을 기준으로 bfs 하면서 치킨집(2)까지의 거리를 모두 구함 -> result.append -> 오름차순 -> result[0]

chiken_house = []
house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chiken_house.append((i, j))

        elif graph[i][j] == 1:
            house.append((i, j))

chiken_comb = list(combinations(chiken_house, M))


# 완탐
res = []
# 치킨집 조합에 대한 모든 집에 대한 치킨 도시 거리
for chiken in chiken_comb:
    # 모든 집에 대하여 완탐
    # 집마다 모든 치킨 집까지 거리 구하기 -> 최소만 distance에 더하기
    temp = []
    for h in house:
        hx, hy = h
        distance = 0

        for i in range(len(chiken)):
            cx, cy = chiken[i]

            if i == 0:
                distance = abs(cx - hx) + abs(cy - hy)
                continue

            distance = min(distance, abs(cx - hx) + abs(cy - hy))
        temp.append(distance)
    res.append(sum(temp))

print(min(res))

