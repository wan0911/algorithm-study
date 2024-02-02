# 새로운 동네
# 출/퇴근길 모두 방문하는 동네.., S -> T(1번) / T -> S(1번), S != T
# 단방향 그래프, 인접 리스트

# 정점 n/간선 갯수 m
# 간선 정보

# 단방향 그래프라, S->T / T->S 방문 노드가 다를 수 있음, 각각 체크해서 공통되는 것만 뽑으면 될듯
# dfs든 bfs든 상관없을듯

from sys import stdin

N, M = map(int, stdin.readline().split('_'))
graph = [[] for _ in range(N + 1)]
visited = [[0] * (N + 1)]
for _ in range(M):
    x, y = map(int, stdin.readline().split('_'))
    graph[x].append(y)
home, company = map(int, stdin.readline().split('_'))

res = []


def dfs(v):
    visited[v] = 1

    for node in graph[v]:
        if not visited[node]:
            res.append(node)
            dfs(node)


dfs(home)
print(res)

## 소프티어 풀이
# S->T / T->S 2번 DFS
n,m=map(int, input().split())   
    adj=[[] for _ in range(n+1)]    
    adjR=[[] for _ in range(n+1)]   # T->S
    for _ in range(m):
        a,b,=map(int,input().split())
        adj[a].append(b)    
        adjR[b].append(a)
    S,T=map(int, input().split())   


    fromS=[0]*(n+1)
    fromS[T]=1          
    DFS(S,adj,fromS)

    fromT=[0]*(n+1)
    fromT[S]=1          
    DFS(T,adj,fromT)

    toS=[0]*(n+1)
    DFS(S,adjR,toS)

    toT=[0]*(n+1)
    DFS(T,adjR,toT)
    
    count=0
    for i in range(1,n+1):
        if fromS[i] and fromT[i] and toS[i] and toT[i]:
            count+=1

    print(count-2)



'''
5_9↵
1_2↵
1_4↵
2_1↵
2_3↵
3_4↵
3_5↵
4_1↵
4_3↵
5_1↵
1_3
'''