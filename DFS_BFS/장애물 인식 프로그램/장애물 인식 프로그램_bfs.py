from collections import deque

n = int(input())
graph = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]

answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if not visited[nx][ny] and graph[nx][ny] == '1':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
 
    answer.append(count)
 
 
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            bfs(i, j)

print(len(answer))
print('\n'.join(map(str, sorted(answer))))