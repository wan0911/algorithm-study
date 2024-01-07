# 트리 그려보기!
# 부모 - 자식: 1촌
# 두 사람 간 이어진 촌수를 구할 때 까지 트리를 돌아야 한다 -> dfs


from sys import stdin

N = int(stdin.readline().rstrip())  # 전체 사람 수
A, B = map(int, stdin.readline().split())  # 촌수 계산해야 하는 두 사람
M = int(stdin.readline().rstrip())  # 촌수 관계

visitied = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    k, v = map(int, stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)
# print(*graph, sep='\n')


# 파라미터, visitied 주의
result = []


def dfs(v, cnt):
    cnt += 1
    visitied[v] = 1

    # B를 찾으면 stop
    for cur_v in graph[v]:
        if not visitied[cur_v]:
            if cur_v == B:
                result.append(cnt)
                return
            dfs(cur_v, cnt)


dfs(A, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0])
