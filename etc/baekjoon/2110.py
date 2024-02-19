# N: 집의 수 / C: 공유기 갯수
# C개의 공유기 설치, 한 집에 한 개만 공유기 설치
# 가장 인접한 공유기 간 거리 최대
# ?

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
homes = [int(input().rstrip()) for _ in range(N)]
homes.sort()

left, right = 1, homes[-1] - homes[0]  # 이분탐색 기준 = 공유기 간 거리
res = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 1  # 첫 번째 집에 공유기 설치
    cur = homes[0]
    for i in range(1, len(homes)):
        if homes[i] - cur >= mid:
            cnt += 1
            cur = homes[i]

    if cnt >= C:  # 인접한 공유기 간 거리가 짧음 -> 거리를 더 크게
        # 이 범위 내에서 끝까지 탐색했을 때, 정답
        left = mid + 1
        res = mid
    else:
        right = mid - 1

print(res)

"""
5 3
1
2
8
4
9
"""
