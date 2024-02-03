# 무방향 그래프
# 연결 요소 갯수? = 연결 뭉텅이 -> dfs 실행 횟수

from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]  # 1부터 시작, 정점의 갯수 = N
visited = [0] * (N + 1)

for _ in range(M):
    k, v = map(int, stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)


# cnt 설정
def dfs(v, cnt):
    visited[v] = 1

    for cur_v in graph[v]:
        if not visited[cur_v]:
            visited[cur_v] = 1
            cnt += 1
            cnt = dfs(cur_v, cnt)
    return cnt


# out
res = []
for i in range(1, N + 1):   # 노드로 실행
    if not visited[i]:
        res.append(dfs(i, 1))

print(len(res))