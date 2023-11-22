from sys import stdin
from collections import deque, defaultdict

n = int(stdin.readline())  # 사람 수
start_v, target_v = map(int, stdin.readline().split())  # 7과 3의 촌수
m = int(stdin.readline())  # 관계 수

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

    graph[x] = sorted(graph[x])
    graph[y] = sorted(graph[y])


bfs_result = [start_v]
def bfs(start_v):
    visited = [0] * (n + 1)
    q = deque()
    q.append(start_v)
    visited[start_v] = 1

    while q:
        cur_v = q.popleft()

        for v in graph[cur_v]:
            if not visited[v]:
                visited[v] = 1
                q.append(v)
                bfs_result.append(v)
        print(q)

bfs(start_v)
print(bfs_result)

"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

"""
