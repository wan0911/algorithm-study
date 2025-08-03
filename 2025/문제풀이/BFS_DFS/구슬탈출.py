# N, M = x, y
# 빨간 구슬 1개, 파란 구슬 1개
# 가장 바깥 행과 열은 막혀있음, 구멍 1개
# 빨간 구슬이 구멍으로 빠져야 함, 파란 구슬이 빠지면 안됨, 동시에 빠져도 안됨
# 탐색 횟수: 10번 이내

'''
- 구슬은 동시에 움직임 -> BFS 동시 탐색
- .: 빈칸 / #: 벽 / 0: 구멍

- R과 B가 동시에 이동해서, 구멍에 도착하는 지점을 체크
- 탐색 횟수: 10회 초과 시 False
  R과 B는 같은 방향으로 움직인다. -> R과 B가 탐색 횟수 내에서 같은 구멍으로 빠지면 안됨
- BFS는 한번만 탐색해도 될듯
'''
from collections import deque

N, M = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(N)]

R_visited = [[0] * M for _ in range(N)]
B_visited = [[0] * M for _ in range(N)]
R_cnt, B_cnt = 0, 0 # 10번 이내로 탐색 가능한지 확인, R과 B 모두 통과해도 안됨
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]


def bfs():
    q = deque()
    # 구슬 위치 BFS 추가
    for n in range(N):
        for m in range(M):
            if grid[n][m] == 'R' or grid[n][m] == 'B':
                q.append((grid[n][m], n, m,))
                
    while q:
        color, cx, cy, cnt = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i] 
            if 0 <= nx < N and 0 <= ny < M and (grid[nx][ny] = '.' or grid[nx][ny] == '0'):
                if color == 'R' and not R_visited[nx][ny]:
                    R_cnt +=1 
                    R_visited[nx][ny] = 1
                    q.append((color, nx, ny))
                elif  color == 'B' and not B_visited[nx][ny]:
                    B_cnt +=1 
                    B_visited[nx][ny] = 1
                    q.append((color, nx, ny))
    
