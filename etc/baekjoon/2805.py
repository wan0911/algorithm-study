# M: 필요한 나무 길이, N: 나무 갯수
# H: 톱날 높이
# H보다 큰 길이의 나무들은 다 자름, 잘린 나무를 가져갈 수 있음
# (자른 길이가 M 이상이면 만족) 필요한 만큼만 자르고 싶음 -> M을 최소로하는 H (H가 최대한 커야 함)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = [*map(int, input().split())]

left, right = 0, max(trees)
res = 0
while left <= right:
    lens = 0
    mid = (left + right) // 2

    for tree in trees:
        if tree > mid:
            lens += tree - mid

    if lens >= M:  # 자른 길이가 남아 돔
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)

"""
4 7
20 15 10 17
"""

'''
5 20
4 42 40 26 46
'''
