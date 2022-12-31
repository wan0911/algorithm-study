from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

# 아마도 1차원에만 해당되지 않나....
def dfs(graph, start):
    visited, need_visit = list(), list()
    visited.append(start)
    
    cnt = 0
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            cnt += 1
            need_visit.append(graph[node])

    return cnt

print(dfs(graph, graph[0][0]))


'''
- input
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000
'''