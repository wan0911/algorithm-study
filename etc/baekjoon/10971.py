# N개의 도시를 순회 -> 원래 도시로 돌아와야 함
# "양방향" "가중치" 그래프
# 최소 비용
## 모든 경로 탐색 -> 최소 경우 구하기
## 도시 간 이동 불가능할 수 있음

# 다익스트라가 아닌듯.. -> 출발 지점 X, 모든 도시를 순회해야 해서

1.0
import sys

input = sys.stdin.readline

# 변수
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if i == j or arr[j] == 0:
            continue
        graph[i].append((j, arr[j]))

# 함수
cost = float("inf")
def dfs(x, val, depth=1):
    global start, cost

    # 모든 도시를 순회했다면
    if depth == N:
        for nx, n_val in graph[x]:
            if nx == start:  # 처음 시작 도시로 돌아올 수 있을 때만, cost 업데이트 / 이외는 pass
                cost = min(cost, val + n_val)

    # 이미 방문한 도시이면, pass
    if visited[x]:
        return
    else:
        visited[x] = 1

    # *인접한 노드 탐색
    for nx, n_val in graph[x]:
        if not visited[nx]:
            # 출발 지점 ~ nx 지점까지의 최단 경로로 업데이트
            dfs(nx, val + n_val, depth + 1)
            visited[nx] = 0


# 완전탐색
for i in range(N):
    visited = [0] * N
    start = i
    dfs(i, 0)


print(cost)


"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""
