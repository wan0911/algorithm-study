from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().split()))
nums.sort()

N = int(stdin.readline().rstrip())
target = list(map(int, stdin.readline().split()))


for t in target:
    start = 0
    end = len(nums) - 1
    flag = 0

    while start <= end:
        idx = (start + end) // 2  # 기준점 - 반올림

        if t == nums[idx]:
            flag = 1

        if t > nums[idx]:
            start = idx + 1
        else:
            end = idx - 1
    print(flag)
