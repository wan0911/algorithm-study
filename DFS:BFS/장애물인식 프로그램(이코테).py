from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]     

cnt_list = []
# graph = 2차원 배열
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
print(result) 



'''
- input
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000
'''