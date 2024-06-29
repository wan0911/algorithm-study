# 신뢰 -> 연결
# N개 컴퓨터, M개 케이스
# N = 4, M = 5

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

"""
틀린이유
1. 양방향이 아님
    - A가 B를 신뢰하는 경우, A -> B: 해킹 X, B -> A: 해킹 O 
2. visited 사용 시, 빈 list / set 사용하지 말기
    - 시간 복잡도가 오래 걸린다
"""

# 1. 인접 리스트 만들기
graph = [[] for n in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # 부모 - 자식 관계!


# 2. bfs
def bfs(num, cnt):
    q = deque([num])
    visited = [0] * (N + 1)  # visited = [] -> 시간 복잡도 O(N)... (여기가 중요함!)
    visited[num] = 1

    while q:
        num = q.popleft()

        for n in graph[num]:
            if not visited[n]:  # 시간 복잡도 O(1)
                visited[n] = 1
                q.append(n)
                cnt += 1
    return cnt


# 3. bfs 실행
res = []
max_length = 0
for i in range(1, N + 1):
    result = bfs(i)

    if max_length < result:
        max_length = result
        res = [i]
    elif max_length == result:
        res.append(i)


# 4. 결과
print(*res)


"""
5 4
3 1
3 2
4 3
5 3
"""
