from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        # (0,0) -> (n-1,n-1)까지 도달할 수 있는 최단 거리 / 도달하지 못하면 -1
        # BFS = 최단 거리 탐색, 같은 레벨별 탐색(동시 탐색)이므로 도착지에 먼저 도달하는 횟수가 최단거리가 됨 -> 인자에 cnt를 넣어야 하나?
        # 정사각형, 대각선 8방향, 0이 움직일 수 있는 길


        n = len(grid)
        dx, dy = [0,0,-1,1,-1,-1,1,1], [1,-1,0,0,1,-1,1,-1] # 방향 보통 어떻게 쓰는지 알아두기
        visited = [[0] * n for _ in range(n)]

        def bfs(x, y, s): # 변수 겹치는지 확인 ㅠ
            q = deque()
            q.append((x, y, s))

            while q:
                cx, cy, cnt = q.popleft()

                if cx == n - 1 and cy == n - 1: 
                    # bfs 순서에 따라 가장 최단의 경우가, 제일 빨리 도착하지 않을 수도 있나?
                    # => 아님 레벨별 탐색, popleft가 아닌 pop을 써서 틀렸던 것 
                    return cnt

                for i in range(8):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 0 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny, cnt + 1))


        # 탐색 완료 후, (n-1,n-1) visited = 0 이면 도달하지 못함
        if grid[0][0] == 1 or grid[n-1][n-1] != 0:
            return -1
        else:
            visited[0][0] = 1   # (0,0)에서 한번만 탐색 시작
            result = bfs(0,0,1)
            return result if result != None else -1
