# 걷기: x +- 1 / 순간이동: 2 * x
# 일직선상
# 최소 시간 => bfs?

# q에 추가된 순으로 탐색하는데.. 처음 방문 길이로 어떻게 최단 거리가 결정된다는건 줄 몰랐는데..
# 일단, bfs 탐색이다. -> "인접 노드"를 우선으로, "레벨별" 탐색!
# 그러니까..  예를 들어, q에서 6, .... 6이 들어왔어도 "레벨별"로 탐색하니까 먼저 들어온 6의 경우가 가장 최단 거리가 됨
# 나중에 들어온 6은 거리가 더 길기 때문에... 해당 경로는 탐색할 필요가 없음 (최단이 아니니까) -> 그래서 pass
# 이렇게 ~~ 계속 q에 들어온 수를 탐색하다가 찾고자 하는 "K"가 나오면 K에 대한 최단 경로를 출력해주면 됨
# 처음 방문이면.. 레벨별 탐색이니 이전 탐색 거리 + 1


import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10**5 + 1
visited = [0] * MAX


def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(visited[K])
            break

        for nx in [x - 1, x + 1, x * 2]:  # 레벨별 탐색
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


bfs()

"""
5 17
"""
