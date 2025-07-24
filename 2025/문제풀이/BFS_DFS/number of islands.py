class Solution(object):
    def numIslands(self, grid):
        # 1로 연결된 부분이 '섬'이다, 0은 탐색할 수 없다.
        # 상하좌우 탐색 가능
        # grid 안의 원소 값이 string이다!
        m, n = len(grid), len(grid[0])
        # visited = [[0] * n for _ in range(m)]
        dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]  # 상하좌우
        cnt = 0

        def bfs(x, y):
            q = [[x, y]]
            while q:
                cx, cy = q.pop(0)
                # visited[cx][cy] = 1
                grid[cx][cy] = "0"
                for k in range(4):
                    nx, ny = cx + dx[k], cy + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        # if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and not visited[nx][ny]:
                        # 방문처리
                        # 원본 리스트를 바꿀지..? -> 그래야 중복 탐색을 안할듯?
                        grid[nx][ny] = "0"
                        q.append([nx, ny])

        # 탐색 시작
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(i, j)

        print(cnt)


""" DFS 풀이
class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]  # 상하좌우
        cnt = 0

        def dfs(x, y):
            q = [[x, y]]
            grid[x][y] = "0"

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    grid[nx][ny] == "0"
                    dfs(nx, ny)
        
        # 탐색 시작
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)

        print(cnt)
        return cnt # return이 무조건 있어야 하나?

"""
