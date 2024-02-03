from sys import stdin
import sys

sys.setrecursionlimit(10**7)

N, M, R = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

    # graph 정렬
    graph[u].sort()
    graph[v].sort()

cnt = 1


def dfs(v):
    global cnt
    print(v)  # 방문 순서 출력
    visited[v] = 1

    for cur_v in graph[v]:
        if visited[cur_v] == 0:
            cnt += 1
            dfs(cur_v)


dfs(R)
print(0)

