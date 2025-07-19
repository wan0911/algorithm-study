from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        # 인접리스트
        # BFS 문제
        # 큐: FIFO
        visited = [0 for _ in range(len(rooms))]
        visited[0] = 1
        q = deque(rooms[0])
        while q:
            cur_key = q.popleft()
            visited[cur_key] = 1
            for next_key in rooms[cur_key]:
                if not visited[next_key]:
                    q.append(next_key)

        # print(visited)
        if sum(visited) == len(rooms):
            return True
        else:
            return False
