# 풀이 실패 - 피드백중


class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])  # 3, 4 = x, y
        dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
        ans = []

        # 일단, word랑 일치하지 않으면 pass
        # 상하좌우 탐색하면서 word와 일치하는 방향 찾기
        # 재귀 or while
        final_ans = []

        def dfs(start, v_list, ans):  # 글자로 보자
            x, y = start[0], start[1]

            if ans == word:
                return True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 행, 열 위치 주의
                if 0 <= nx < m and 0 <= ny < n and v_list[nx][ny] == 0:
                    if (ans + board[nx][ny]) == word[0 : len(ans) + 1]:
                        visited[nx][ny] = 1
                        ans += board[nx][ny]
                        if dfs([nx, ny], v_list, ans):  # return 값 받기
                            return True
                        visited[nx][ny] = 0  # 백트래킹

        # 배열 탐색
        for i in range(m):
            for j in range(n):
                # dfs
                c_word = board[i][j]
                if c_word == word[0]:
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    if dfs([i, j], visited, c_word):
                        return True
        return False
