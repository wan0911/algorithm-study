import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 2차원 배열, DFS
def dfs():
    


# dfs 실행
res = []
for i in range(N):
    for j in range(N):
        dfs(i, j)
