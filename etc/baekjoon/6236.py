# N: 총 돈 / M: 돈을 인출할 횟수 / K: 인출한 돈
# K 최소화

# K원을 M번 인출
# 한 번 K원을 인출하면, 그 돈을 다 소진하는 날짜까지 사용 가능
## 만약, 돈이 부족하면 다시 인출해야 함
## 그렇게, 총 인출 횟수가 M이 되도록
## 그러면서도 K는 가장 작은 수로


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input().rstrip()) for _ in range(N)]


def binarySearch():
    left, right = max(nums), sum(nums)
    res = 0

    while left <= right:
        mid = (left + right) // 2
        curr_money = mid

        cnt = 0
        for num in nums:
            if cnt > M:
                break

            if curr_money >= num:
                curr_money -= num
            else:
                cnt += 1
                curr_money = mid - num

        if cnt > M:
            left = mid + 1
        elif cnt <= M:
            right = mid - 1
            res = mid

    return res


print(binarySearch())


# '''
# 7 5
# 100
# 400
# 300
# 100
# 500
# 101
# 400
# '''
