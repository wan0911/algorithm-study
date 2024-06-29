import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 2차원 배열, BFS
def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            res.append(bfs(i, j))

res.sort()
print(len(res))
print(*res, sep='\n')


"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
