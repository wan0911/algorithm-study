from sys import stdin

N, M = map(int, stdin.readline().split())
J = int(stdin.readline().rstrip())
apples = [int(stdin.readline().rstrip()) for _ in range(J)]

s = 1  # 바구니 기준점
cnt = 0

for a in apples:
    # 1. 사과가 바구니에 들어갈 때 -> 이동 x
    if a in range(s, s + M - 1):
        continue
    # 2. 사과가 바구니 왼쪽에 떨어질 때 -> 왼쪽으로 이동
    elif a < s:
        dx = s - a
        s -= dx
        cnt += dx
    # 3. 사과가 바구니 오른쪽에 떨어질 때 -> 오른쪽으로 이동
    elif a > s:
        # 1 2 5
        dx = a - (s + M - 1)
        s += dx
        cnt += dx

print(cnt)
