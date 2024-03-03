import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
if N == 0:
    print(1)
else:
    num = 0
    for n in range(1, N + 1):
        num *= n

    print(Counter(str(num))["0"])
