# 직사각형 ->  - ㅣ
# --  ㅣ  -> 같은 판자
#     ㅣ
# - -> 좌우 / | -> 상하  : 인접한거 1개로 카운트
# 방 바닥 장식에 필요한 판자 갯수
# N, M <= 50

# bfs -> 큐 / dfs -> 재귀
# dfS로 풀어야 하나?

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로

graph = [list(input().rstrip("\n")) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1]  # 좌우
dy = [1, -1]  # 상하

cnt = 0


def bfs(a, b):
    q = deque()
    q.append((a, b))
    s = graph[a][b]  # - or |

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        if s == "-":
            for i in range(2):
                ny = y + dy[i]
                if 0 <= ny < M and visited[x][ny] != 1 and graph[x][ny] == "-":
                    q.append((x, ny))
        elif s == "|":
            for i in range(2):
                nx = x + dx[i]
                if 0 <= nx < N and visited[nx][y] != 1 and graph[nx][y] == "|":
                    q.append((nx, y))


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)


# bfs로 안풀어도 되는 듯... 단순 계산 가능 문제 ㅠ -> 가로 cnt, 세로 cnt
