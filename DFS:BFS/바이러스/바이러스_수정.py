# graph 트리 아님! 사이클 -> 양방향 연결
from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
S = int(stdin.readline())


# 그래프
graph = defaultdict(list)
for _ in range(S):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
def dfs(graph, start):
    global cnt
    visited, need_visit = set(), list()
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop()
        
        if node not in visited:
            # print(node)
            visited.add(node)
            need_visit.extend(graph[node])
    visited.remove(1)
    print(len(visited))
    

dfs(graph, 1)

'''
- tc
7
6
1 2
2 3
1 5
5 2
5 6
4 7

- result
4


10
7
1 2
2 3
3 4 
5 6
7 8
8 9
9 1 # 6
'''