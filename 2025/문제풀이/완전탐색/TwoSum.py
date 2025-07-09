class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums) - 1):
            new_target = target - nums[i]  # 반복문이니까 새로운 변수 필요
            result = [i]  # 초기화
            for j in range(i + 1, len(nums)):
                if nums[j] == new_target:
                    result.append(j)
                    return result
