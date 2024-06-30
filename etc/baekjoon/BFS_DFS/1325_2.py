# 해킹
# dfs로 풀어야 시간복잡도가 작아지나? -> ㄴㄴ

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 인접 리스트 만들기
graph = [[] for n in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # 부모 - 자식 관계!


# 2. DFS
def dfs(v, visited, cnt):
    visited[v] = 1

    for nv in graph[v]:
        if not visited[nv]:
            cnt = dfs(nv, visited, cnt + 1)
    return cnt


res = 0
lst = []
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    tmp = dfs(i, visited, cnt=1)

    if res < tmp:
        res = tmp
        lst.clear()
        lst.append(i)
    elif res == tmp:
        lst.append(i)


print(*lst)


"""
틀린이유

1. 재귀 함수 -> 메모리 초과 / 시간 초과
: 초반에 sys.setrecursionlimit(10**6) 을 통해 스택을 위한 array의 사이즈 지정 -> 메모리 초과 오류
: '스택'으로 구현하면 통과하는데, 스택은 필요 시에 사이즈를 늘리는 dynamic array이기 때문....

"""
