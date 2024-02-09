# 1. 오답

# 새로운 동네
# 출/퇴근길 모두 방문하는 동네.., S -> T(1번) / T -> S(1번), S != T
# 단방향 그래프, 인접 리스트

# 정점 n/간선 갯수 m
# 간선 정보

# 단방향 그래프라, S->T / T->S 방문 노드가 다를 수 있음, 각각 체크해서 공통되는 것만 뽑으면 될듯
# dfs든 bfs든 상관없을듯

from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
fromS = [0] * (N + 1)
fromT = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
home, company = map(int, stdin.readline().split())

res = []
def dfs(start, target, visited):
    visited[start] = 1

    for node in graph[start]:
        if not visited[node] and node != target:
            res.append(node)
            dfs(node, target, visited)


dfs(home, company, fromS)
dfs(company, home, fromT)


print(res)
# res_cnt = [0] * (N+1)
# for r in res:
#     res_cnt[r] += 1

# print(len([x for x in res_cnt if x > 1]))


# 2. 재풀이

"""
5 9
1 2
1 4
2 1
2 3
3 4
3 5
4 1
4 3
5 1
1 3
"""

'''
8 14
1 2
1 5
1 7
2 3
3 1
4 1
4 2
5 4
5 8
6 2
6 3
7 1
7 6
8 7
6 5
'''
'''
5 5
1 2
2 1
2 3
3 2
2 4
1 3
'''