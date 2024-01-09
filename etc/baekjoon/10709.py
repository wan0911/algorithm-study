# 세로: H, 가로: W
# 구름 1분 -> 1km(오른쪽)
# 각 구역에 대해 몇 분 뒤 처음으로 구름이 오는지


from sys import stdin

H, W = map(int, stdin.readline().split())
graph = [list(stdin.readline().rstrip()) for _ in range(H)]

visited = []


def dfs(x, y, n):
    visited.append((x, y))
    graph[x][y] = n

    if y + 1 < W and graph[x][y + 1] == "c":
        return

    # 다음 c를 만나면 break
    if y + 1 < W:
        dfs(x, y + 1, n + 1)


for i in range(H):
    for j in range(W):
        if (i, j) not in visited:
            if graph[i][j] == "c":  # dfs 실행 조건
                dfs(i, j, 0)
            else:
                graph[i][j] = -1

# out
for i in range(H):
    print(" ".join(map(str, graph[i])))


"""
6 8
.c......
........
.ccc..c.
....c...
..c.cc..
....c...
"""
