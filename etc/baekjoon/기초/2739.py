import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, 9 + 1):
    print(f"{N} * {i} = {N * i}")