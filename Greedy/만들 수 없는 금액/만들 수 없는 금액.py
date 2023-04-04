from sys import stdin
from itertools import combinations

N = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

# 전체 조합 -> 합 구하고,
# 1 부터 찾기 
cb = list()
for i in range(len(data)):
    cb.extend(([sum(c) for c in combinations(data, i)]))

set(cb)

for i in range(1000000):
    if i not in cb:
        print(i)
        break


'''
input
5
3 2 1 1 9

output
8
'''