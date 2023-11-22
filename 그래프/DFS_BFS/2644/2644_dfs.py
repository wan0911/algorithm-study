# dfs 풀이 -> 문제 해석부터 틀림

from sys import stdin
from collections import deque, defaultdict

n = int(stdin.readline())  # 사람 수
start_v, target_v = map(int, stdin.readline().split())  # 7과 3의 촌수
m = int(stdin.readline())  # 관계 수

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

    graph[x] = sorted(graph[x])
    graph[y] = sorted(graph[y])


visited = [0] * (n + 1)
dfs_result = []


def dfs(cur_v, num):
    visited[cur_v] = 1
    dfs_result.append(cur_v)

    if visited[target_v] == 1:
        return 

    for v in graph[cur_v]:
        if target_v in graph[cur_v]:
            dfs(target_v)
            break

        if not visited[v]:
            dfs(v)
            print(dfs_result)
            dfs_result.pop()


dfs(start_v)
if target_v not in dfs_result:
    print(-1)

"""
TC 2
9
7 8
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

TC 3
12
7 6
11
1 2
1 3
2 7
2 8
2 9
4 5
4 6
8 10
10 11
11 12
12 4
"""


# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
####

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

# dfs
def dfs(v, num):
  num += 1
  visited[v] = True

  if v == B:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)   # 1일 때, 초기화 됨

dfs(A, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)