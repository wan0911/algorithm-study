from sys import stdin
from itertools import combinations
from copy import deepcopy

N, M = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

# 조합 - 중복 되는거 제거
cb = list(combinations(data, 2))
idx = list()
for i in range(len(cb)):
    a, b = cb[i]
    if a == b:
        idx.append(i)
        
print(len(cb) - len(idx))



'''
input
5 3
1 3 2 3 2

output 
8

---
input
8 5
1 5 4 3 2 4 5 2

output
25
'''

