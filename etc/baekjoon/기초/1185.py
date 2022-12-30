import sys

N, S = map(int, sys.stdin.readline().split())
result = []

arr = [i+1 for i in range(N)]
idx = 0
while arr:
    idx += S - 1
    print(idx, arr)
    if idx >= len(arr):
        idx %= len(arr)
    result.append(str(arr.pop(idx)))

print('<', ', '.join(result)[:], '>', sep='')


'''
- input
7 3

- output
<3, 6, 2, 7, 5, 1, 4>

'''
