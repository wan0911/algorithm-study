from collections import deque

def shortestPathBinaryMatrix(grid):
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def bfs():
            q = deque()
            q.append((0, 0))
            shortest_len = 1

            while q:
                cur_x, cur_y = q.popleft()
                visited[cur_x][cur_y] = True

                if cur_x == n - 1 and cur_y == n - 1:
                    break

                for dx, dy in delta:
                    next_x = cur_x + dx
                    next_y = cur_y + dy

                    if 0 <= next_x < n and 0 <= next_y < n:
                        if grid[next_x][next_y] == 0 and visited[next_x][next_y] == False:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
                            shortest_len += 1

            return print(shortest_len)

        return bfs()
    
shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])