import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(N)]  # visited 사용 X

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 2차원 배열, DFS
# 스택
def dfs(x, y, cnt):
    graph[x][y] = 0

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt + 1)  # 각 스택의 결과를 이전 스택에도 반영

    return cnt


# dfs 실행
res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            res.append(dfs(i, j, cnt=1))

res.sort()
print(len(res))
print(*res, sep="\n")


"""
틀린 이유

1. 재귀함수에서 cnt 값 업데이트를 제대로 구현하지 않음

def dfs(x, y, cnt):
    graph[x][y] = 0

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny, cnt) --> cnt가 증가해서 스택이 돌지만, 반환 시 이전 스택의 cnt 값에 업데이트 X (그냥 함수를 빠져나옴)
            
    return cnt
"""
