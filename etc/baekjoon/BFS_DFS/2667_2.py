import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 1 # global


# 2차원 배열, DFS
# 스택
def dfs(x, y):
    global cnt
    visited[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
            cnt += 1
            dfs(nx, ny)


# dfs 실행
res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            res.append(cnt)
            cnt = 1  # 초기화

res.sort()
print(len(res))
print(*res, sep="\n")


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
