from collections import defaultdict


class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        keys = [i for i in range(n)]
        graph = defaultdict()
        for i in range(n):
            graph[i] = sorted(rooms[i])

        visited = [0] * n
        dfs_list = []

        def dfs(start_v):
            visited[start_v] = 1
            dfs_list.append(start_v)

            for v in graph[start_v]:
                if not visited[v]:
                    visited[v] = 1
                    dfs(v)

        dfs(0)

        if sum(set(keys) - set(dfs_list)) > 0:
            return False
        else:
            return True
