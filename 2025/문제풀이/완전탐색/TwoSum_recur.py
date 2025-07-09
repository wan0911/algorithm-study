class Solution(object):
    # 재귀
    # 리턴 조건 1: level이 2
    # 리턴 조건 2: 정답을 찾았을 때 all stop
    def solution(self, nums, target):
        ans = []  # 재귀에서 공통으로 접근해야될 변수는 global로

        def backtracking(start):
            # 리턴 조건
            if len(ans) == 2 and (ans[0] + ans[1] == target):
                return True

            for i in range(start, len(nums)):
                ans.append(i)
                print(ans)
                # 자기 원소 이후부터 탐색, 전체 함수 return 조건
                if backtracking(start + 1):
                    return ans
                ans.pop()  # 마지막 원소 빼기
