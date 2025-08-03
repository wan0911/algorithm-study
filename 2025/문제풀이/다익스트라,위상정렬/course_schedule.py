class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        위상정렬 -> "사이클" 있는지 없는지 확인
        """

        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v, u in prerequisites:
            graph[u].append(v) # u -> v, 인접리스트
            indegree[v] += 1
        # print(graph, indegree)
				
        q = deque()
        for v in range(numCourses):
            if indegree[v] == 0: # 가장 바깥쪽에 있는 노드 탐색
                q.append(v)
        while q:
            cur_v = q.popleft()
            visited.append(cur_v) # 수강한 수업 체크,  

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)
				
        # return len(course_visited) == numCourses 
        if len(visited) == numCourses:
            return True
        else:
            return False