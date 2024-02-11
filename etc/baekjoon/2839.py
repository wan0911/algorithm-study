# 작은 수의 법칙

from sys import stdin

N = int(stdin.readline().rstrip())

res = 0
while N > 0:
    if N % 5 == 0:
        res += N // 5
        N = 0
    else:
        N -= 3
        res += 1
        

if N == 0:  # 전부 나누어 떨어졌다면
    print(res)
else:
    print(-1)


'''
18
'''