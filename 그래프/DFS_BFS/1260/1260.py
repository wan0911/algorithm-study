from sys import stdin
from collections import deque, defaultdict

N, M, V = map(int, stdin.readline().split())
graph = defaultdict(list)

for i in range(M):
    v, e = map(int, stdin.readline().split())
    graph[v].append(e)
    graph[e].append(v)

    graph[v] = sorted(graph[v])
    graph[e] = sorted(graph[e])


def bfs(start_v):
    visited = [start_v]
    q = deque()
    q.append(start_v)
    bfs_result = [start_v]

    while q:
        cur_v = q.popleft()

        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
                bfs_result.append(v) 
    
    return ' '.join([str(x) for x in bfs_result])

visited = []
q = deque()
dfs_result = []
def dfs(start_v):
    visited.append(start_v)
    q.append(start_v)
    dfs_result.append(start_v)

    for v in graph[start_v]:
        if v not in visited:
            dfs(v)

dfs(V)

print(' '.join(str(x) for x in dfs_result))
print(bfs(V))