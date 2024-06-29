# 해킹
# dfs로 풀어야 시간복잡도가 작아지나?

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 인접 리스트 만들기
graph = [[] for n in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # 부모 - 자식 관계!


# 2. DFS
def dfs():
    