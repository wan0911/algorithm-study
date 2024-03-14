import sys


def funcZ(x, y, n):
    global cnt
    if x > r or x + n <= r or y > c or y + n <= c:
        cnt += n**2
        return

    if n > 2:
        n //= 2
        funcZ(x, y, n)
        funcZ(x, y + n, n)
        funcZ(x + n, y, n)
        funcZ(x + n, y + n, n)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        sys.exit()


n, r, c = map(int, input().split())
cnt = 0
funcZ(0, 0, 2**n)


"""
3 7 7

1 0 0
"""
