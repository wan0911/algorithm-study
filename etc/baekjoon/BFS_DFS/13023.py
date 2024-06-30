# 2초, 512 ?
# DFS 같은데..
# 0 ~ N 각각 DFS 돌려서 [0, ..., N]이 N번 나오면  -> X
"""
문제 이해를 잘못함 
    -> ABCDE 관계 = 그냥 depth >= 5가 존재하는가를 구하는 문제 (depth = N=으로 이해함)
- 무방향 그래프
- ** depth 계산
   - 블럭 총 갯수 구하는 문제가 아니다
   => cnt, 재귀 return에 유의
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


res = 0
def dfs(v, visited, depth):
    global res
    if depth == 5:
        res = 1
        return

    visited[v] = 1
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv, visited, depth + 1)
            
    visited[v] = 0  # 무방향 그래프 -> 방문 초기화 중요....(사이클)

for i in range(N):
    visited = [0] * N
    dfs(i, visited, 1)

    if res == 1:
        print(1)
        break
else:
    print(0)
