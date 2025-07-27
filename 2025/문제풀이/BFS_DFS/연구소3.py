# 바이러스 상태
# 활성 0/비활성 * -> 활성 시, 상하좌우로 퍼짐
# M개를 활성화 -> 모든 빈칸에 바이러스를 퍼트리는 "최소 시간"
# 최단 거리 -> BFS

# 1. 바이러스 3개 조합 구하기
# 2. 완탐 -> BFS로 최소 시간 구하기
# + 각 바이러스마다 BFS 돌면서, 0이나 *가 아닌 경우에 더 짧은 시간으로 치환?
# + 비활성화/벽을 문자로 치환한 이유가 있음.. -> bfs 조건 설정하기 편하게
# [예외]
# 벽이 있어 모두 퍼트리지 못하는 경우에 -1
# 빈칸이 없는 경우에 0

from itertools import combinations
from collections import deque, Counter
import copy

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

# 0인 경우 return
counter = Counter([])
for row in grid:
    counter += Counter(row)
if counter[0] == 0:
    print(0)
    exit()


all_viruses = [(x, y) for x in range(N) for y in range(N) if grid[x][y] == 2]
virus_list = combinations(all_viruses, M)
ans = int(1e9)

def bfs(virus_list, grid):
    q = deque()
    cnt = 0
    max_time = 0
    for vx, vy in virus_list:  # 바이러스 동시 탐색
        q.append((vx, vy, 0))

    while q:
        cx, cy, cnt = q.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 0 or isinstance(grid[nx][ny], int) and grid[nx][ny] > cnt + 1:
                    grid[nx][ny] = cnt + 1
                    q.append((nx, ny, cnt + 1))
                    max_time = max(max_time, cnt + 1)

    # 시간 체크
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return -1
    return max_time


# 배열에 숫자와 문자를 같이 쓰지 않는게 좋을 듯
for viruses in virus_list:
    time = bfs(viruses, copy.deepcopy(grid))
    if time != -1:
        ans = min(ans, time)

if ans != int(1e9):
    print(ans)
else:
    print(-1)
