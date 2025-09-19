from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        dx, dy = [1, 1, -1, -1, 0, 0, -1, 1], [1, -1, 1, -1, 1, -1, 0, 0]

        if grid[0][0] != 0:
            return -1

        q = (
            deque()
        )  # (0,0)에서 시작하니까 cnt = 1, list말고 deque를 써야 시간복잡도 효율이 좋음
        q.append([0, 0, 1])
        visited[0][0] = 1
        ans = []
        while q:
            x, y, cnt = q.popleft()
            # print(x, y, cnt)
            # 여기서 visited, cnt 처리를 하면 중복 계산이 된다.
            if x == n - 1 and y == n - 1:
                ans.append(cnt)
                break

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and grid[nx][ny] == 0
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = 1
                    # cnt += 1
                    q.append([nx, ny, cnt + 1])

        if ans:
            return min(ans)
        else:
            return -1


[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
