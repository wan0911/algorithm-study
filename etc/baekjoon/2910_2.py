# 좀 더 나은 풀이법
from sys import stdin
from collections import Counter

N, C = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
count = {}
idx = 1

for n in nums:
    if n in count:
        count[n][0] += 1
    else:
        count[n] = [1, idx]    # idx = ord
        idx += 1

order = [[k, v] for k, v in count.items()]
order.sort(key = lambda x: (-x[1][0], x[1][1]))

result = []
for k, v in order:
    result += [k] * v[0]

print(*result)
