# 분할정복

# N = 2의 제곱수 / N = 1이 될 때까지 자른다
# 잘라진 하얀색 종이 / 파란색 종이

from sys import stdin

N = int(stdin.readline().rstrip())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0


def division(x, y, n):
    global white, blue
    check = graph[x][y]  # 시작점 색깔

    # 모든 구역 탐색
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 1. 모든 구역이 동일한 색이 아닐 때
            if graph[i][j] != check:  # 시작점과 다른 색깔 -> 4분할 시작
                # 1사분면
                division(x, y, n // 2)
                # 2사분면
                division(x, y + n // 2, n // 2)
                # 3사분면
                division(x + n // 2, y, n // 2)
                # 4사분면
                division(x + n // 2, y + n // 2, n // 2)
                return

    # 2. 모든 구역이 동일한 색일 때 = 분할이 끝난 시점
    if check == 1:
        blue += 1
    else:
        white += 1
    return


division(0, 0, N)
print(white)
print(blue)
