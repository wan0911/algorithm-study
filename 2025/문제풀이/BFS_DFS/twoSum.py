class Solution(object):
    def twoSum(self, nums, target):
        # 정렬
        sorted_nums = [[idx, val] for idx, val in enumerate(nums)]
        sorted_nums.sort(key=lambda x: x[1])
        # 투포인터
        p1, p2 = 0, len(nums) - 1
        ans = None
        while p1 < p2:
            if sorted_nums[p1][1] + sorted_nums[p2][1] == target:
                ans = [sorted_nums[p1][0], sorted_nums[p2][0]]
                break
            elif sorted_nums[p1][1] + sorted_nums[p2][1] > target:
                p2 -= 1
            else:
                p1 += 1

        # print(ans)
        return ans
