class Solution(object):
    # 재귀
    def search(self, nums, target):
        min = 0
        max = len(nums) - 1 # 배열 idx 주의
        mid = (min + max) / 2

        while min <= max:
            # print(min, max, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                max = mid - 1
                mid = (min + max) / 2
            elif nums[mid] < target:
                min = mid + 1
                mid = (min + max) / 2

        return -1
