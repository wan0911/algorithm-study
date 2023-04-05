from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    if graph[x][y] == 1:
        return False
    
    while q:
        x, y = q.popleft()
        graph[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                q.append((nx, ny))
    return True

        
cnt = 0  
for x in range(N):
    for y in range(M):
        if bfs(x, y) == True:
            cnt += 1
print(cnt)


'''
- tc 1
4 5
00110
00011
11111
00000

- result 1 
3


- tc 2
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

-result 2
8
'''


