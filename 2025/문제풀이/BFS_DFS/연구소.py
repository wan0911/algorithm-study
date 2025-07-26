# 세로 N, 가로 M: x, y = N, M
# 상하좌우
# 세울 수 있는 벽 3개
# 0: 빈 칸 / 1: 벽 / 2: 바이러스
# 벽 1을 세워서, 2개 침범할 수 없는 "최대의" 공간 만들기

from itertools import combinations
from collections import deque, Counter

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 바이러스(2)를 기준으로, 바이러스 퍼트리기 -> 이후 0인 영역만 count
def bfs(x, y, grid):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                q.append([nx, ny])
    return grid
                
# 메인 함수 
# 조합 3개 -> 좌표로 변환?
coords = [(x, y) for x in range(N) for y in range(M) if grid[x][y] == 0]
wall_list = list(combinations(coords, 3))

for walls in wall_list:
    w_grid = [row[:] for row in grid]
    # 벽 세우기
    for wx, wy in walls:
        w_grid[wx][wy] = 1
    
    for n in range(N):
        for m in range(M):
            if w_grid[n][m] == 2:
                w_grid = bfs(n, m, w_grid)
                
    # 영역 갯수 구하기
    counter = Counter([])
    for row in w_grid:
        counter += Counter(row)
    ans = max(ans, counter[0])
    
print(ans)