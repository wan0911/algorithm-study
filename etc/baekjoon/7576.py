# 상하좌우
# 모든 토마토들이 익을 최소 일수 -> BFS
# 1일
# -1 = 토마토 x
# 0 = 안익은 토마토 // 익은 토마토가 있어야 인접한 토마토가 익음

# 1을 만나면 visit 시작
# 동시에 탐색을 어떻게 하지..??

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # 행, 열
graph = [[*map(int, input().split())] for _ in range(N)]
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

# 1. 익은 토마토 위치 q에 넣어놓기 -> 익은 토마토 = 1을 기준으로 탐색 시작하기 때문에..
# ** 동시 탐색하는 방법 -> 각 자리에서 cnt한 숫자로 graph에 업데이트하기 때문
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

# 2. bfs 탐색 시작
while q:
    cx, cy = q.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] += graph[cx][cy] + 1  # 여기서 카운트 된 값이 ans로
            q.append((nx, ny))

# print(graph, sep="\n")

# 3. 탐색 후, 체크
for row in graph:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)  # 종료 처리?
    ans = max(ans, max(row))

print(ans - 1)  # 시작 = 1


"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
