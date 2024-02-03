from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1. bfs
def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    graph[x][y] = 0  

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = 0  
                cnt += 1
    return cnt

# 2. bfs 실행
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result.append(bfs(i, j))

# 3. out
print(len(result))
for r in sorted(result):
    print(r