import heapq
from collections import Counter
class Solution(object):
    def networkDelayTime(self, times, n, k):
        '''
        가중치 그래프 + 단방향 그래프, 인접리스트 
        => 시작점부터 모든 노드에 신호가 닫기 위한, 최단 시간
            ** 시작점은 있는데, 끝점이 없음 => 
        [예외] 모든 노드에 신호가 도달할 수 없으면 -1 리턴
        ---
        n: 노드 갯수, k: 시작점
        1. 인접리스트 만들기
        2. 다익스트라 실행
        '''

        # 1. 인접리스트 만들기
        graph = [[] for _ in range(n + 1)] # vertex는 1부터 시작
        for vertex, n_vertex, cost in times:
            graph[vertex].append((n_vertex, cost))

        # 2. 다익스트라 실행
        distance = [float("INF")]  * (n+1)
        distance[k] = 0 # k = start
        q = []
        heappush(q, (0, k)) 
        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue
            for vv, ww in graph[now]:
                cost = distance[now] + ww # next 소모비용
                if cost < distance[vv]:
                    distance[vv] = cost
                    heappush(q, (cost, vv))

        # inf가 2개 이상이면 return -1
        distance.pop(0)
        counter = Counter(distance)
        print(distance)

        if counter[float("INF")] >= 1:
            return -1
        else:
            return max(distance)