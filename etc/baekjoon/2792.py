# M: 보석 갯수 / N: 학생 수
# 질투심 = 학생이 가진 보석의 수

# 같은 색상의 보석만 소유 가능
# 보석은 모두 나눠줘야 함

# 질투심 최소

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
counts = [int(input().rstrip()) for _ in range(M)]

left, right = 1, max(counts)
res = 10 ** 6
while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for ct in counts:
        if ct % mid == 0:
            cnt += ct // mid
        else:
            cnt += (ct // mid) + 1

    if cnt > N:
        res = mid
        left = mid + 1
    else:
        right = mid - 1


print(left)

"""
5 2
7
4

7 5
7
1
7
4
4
"""
