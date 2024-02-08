from sys import stdin

N = int(stdin.readline().rstrip())
M = [int(stdin.readline().rstrip()) for _ in range(N)]

M = sorted(M)
for i in range(len(M)):
    print(M[i])
