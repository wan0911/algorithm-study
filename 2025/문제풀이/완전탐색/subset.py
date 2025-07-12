class Solution(object):
    def subsets(self, nums):
        ans, c_comb = [], []

        # depth가 0 ~ len(nums)까지 모두 구해져야 함
        def combinations(depth, comb, s_idx=0):
            if len(comb) == depth:
                ans.append(comb)
                return

            # 배열 기준 탐색
            for idx in range(s_idx, len(nums)):
                # print(s_idx, idx, nums[idx], ans)
                c_comb.append(nums[idx])
                # print(s_idx, idx)
                combinations(depth, c_comb[:], idx + 1)  # s_idx -> idx로 수정
                c_comb.pop()

        # 함수 진입점
        # depth 길이 기준
        for n in range(len(nums) + 1):
            combinations(n, [])

        ans.sort()
        return ans
