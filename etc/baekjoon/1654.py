# N개의 랜선 필요, 모두 같은 길이로, 최대 N개
# K개 랜선, 길이 제각각
# *K -> N은 불가
# *랜선에서 꼭 한번은 잘라내야 함


import sys

input = sys.stdin.readline

K, N = map(int, input().split())
k_lens = [int(input().rstrip()) for _ in range(K)]


def binarySearch():
    left, right = 1, max(k_lens)
    res = 0

    while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for kl in k_lens:
            cnt += kl // mid

        if cnt >= N:
            res = mid  # 어차피 mid가 현재 최대 숫자임
            left = mid + 1
        else:
            right = mid - 1

    return res


print(binarySearch())

"""
4 11
802
743
457
539
"""
