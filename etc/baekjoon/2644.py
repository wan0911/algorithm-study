from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
A, B = map(int, stdin.readline().split())
M = int(stdin.readline().rstrip())

visited = [0] * (N + 1)  # 1부터 시작하므로 0번째는 빈 공간
graph = defaultdict(list)
for _ in range(M):
    k, v = map(int, stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)


result = []


def dfs(v, cnt):
    cnt += 1
    visited[v] = 1  # 방문 처리

    if v == B:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)


dfs(A, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
