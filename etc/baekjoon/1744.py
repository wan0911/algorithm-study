# 수열 수 묶어서 -> 최대
# 한번만 묶을 수 있음
# 수열의 수를 모두 더함

# 오름차순 정렬, 큰 수 위주로 곱하기
# 2개씩 끊어서, 음수 체크
## 음수가 있으면 무조건 더하기

from sys import stdin

N = int(stdin.readline().rstrip())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]
nums.sort()

res = 0
temp = []


# for i in range(0, len(nums), 2):
#     if i == len(nums):
#         n1, n2 = nums[i], 0
#     else:
#         print(i)
#         n1, n2 = nums[i], nums[i + 1]

    # if n1 * n2 <= 0:
    #     res += (n1 + n2)
    # else:
    #     res += (n1*n2)

print(res)


"""
4
-1
2
1
3
"""

"""
6
0
1
2
4
3
5
"""
