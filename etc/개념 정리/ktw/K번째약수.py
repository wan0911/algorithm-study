# 1 <= N <= 10000, K <= K
# 완전탐색 -> 1 ~ 10000 전부 탐색, K번째에서 stop
# 존재하지 않으면 -1 (1보다 클 때)

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0

for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            print(i)
            break
else:   # for에 대한 else문! (break를 만나지 않으면 실행)
    print(-1)
