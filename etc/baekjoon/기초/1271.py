import sys

input = sys.stdin.readline

N, M = map(int, input().split())

print(N//M)
print(N%M)