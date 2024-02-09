from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:     # 배열 range 주의!
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    
    return False

# 탐색    
cnt = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
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