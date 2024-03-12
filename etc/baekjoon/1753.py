# 최단 경로 / 시작 노드 - 다른 노드
# 다익스트라
# 인접리스트, 초기화 (0, inf)

import sys
from queue import PriorityQueue

input = sys.stdin.readline


V, E = map(int, input().split())  # 노드, 간선
K = int(input())  # 출발 노드
distance = [sys.maxsize] * (V + 1)
visited = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]
q = PriorityQueue()

# 1. 인접리스트 설정
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 2. 시작점
q.put((0, K))  # (거리, 노드) -> heap을 쓰기 때문에..
distance[K] = 0  # 시작점 거리 = 0


# 3. 다익스트라 실행
while q.qsize() > 0:
    current = q.get()
    c_v = current[1]  # 탐색할 인접 노드

    if visited[c_v]:  # 각 노드는 1번씩만 방문..
        continue

    visited[c_v] = True
    for data in graph[c_v]:
        next = data[0]  # 다음 탐색 노드
        value = data[1]  # 거리

        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value

            q.put((distance[next], next))


for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
