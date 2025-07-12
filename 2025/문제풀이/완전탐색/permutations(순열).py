class Solution(object):
    def permute(self, nums):
        result = []

        def backtrack(path):  # path = 현재 list
            # 현재 path를 넣어주면 된다?
            if len(path) == len(nums):
                result.append(path)
                return

            for n in nums:  # 매번 1부터 n까지 완전탐색 + backtracking
                if n not in path:
                    path.append(n)
                    backtrack(path[:])
                    path.pop()  # bactracking을 잘 해주면 glb 변수로 선언할 필요 x

        backtrack([])
        return result
