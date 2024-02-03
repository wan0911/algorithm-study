from sys import stdin
from collections import deque

# 이코테 얼음 영역? / 백준 섬의 개수
# m = 행, n = 열
# 분리된 영역 갯수, 넓이
# 왼쪽 아래: x1, y1 / 오른쪽 위: x2, y2a
# 주어진 좌표 영역 돌면서 1로 처리해버리면 되지 않나?
# 좌표 주의: 왼쪽 아래가 시작점 -> 좌표 뒤집어서 생각할 수 있나?

M, N, K = map(int, stdin.readline().split(' '))
graph = [[0]*N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = []


# 1. bfs
def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1

    while q:
        x, y = q.popleft()  

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < M) and (0 <= ny < N) and graph[nx][ny] == 0:  
                graph[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt


# 2. 주어진 구역 1로 채우기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

# 3. bfs 실행
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i, j))


print(len(result))
print(*sorted(result))