# 이웃한 육지(L) / 상하좌우, 한칸 -> 1h
# 육지 - 육지 / 가장 긴 시간?
# visited / bfs?

# 보물 위치
# 같은 육지에서 - 서로 가장 멀리 떨어진 곳


from sys import stdin

a, b = map(int, stdin.readline().split())  # 행, 열
graph = [list(stdin.readline().rstrip()) for _ in range(a)]
visited = [[0] * b for _ in range(a)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 구역마다
# 첫 좌표, 마지막 좌표 간 distance
# 끝 - 끝: 거리 구하면 됨


def dfs(x, y, temp=[]):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (
            0 <= nx < a
            and 0 <= ny < b
            and graph[nx][ny] == "L"
            and visited[nx][ny] == 0
        ):
            dfs(nx, ny, temp)
            temp.append((x, y))
    return temp


result = []
for i in range(a):
    for j in range(b):
        if graph[i][j] == "L" and visited[i][j] == 0:
            result.append(dfs(i, j))


for i in result:
    print(i)


"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""
