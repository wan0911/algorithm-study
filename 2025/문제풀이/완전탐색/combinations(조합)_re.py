class Solution(object):
    def combine(self, n, k):  # 기본 실행 코드
        # 조합 nCr: 리스트 X, 숫자 n r
        # 조합이니까.. 리스트를 우측으로 점차 이동시킨다고 생각하면 편함
        def backtrack(start, path):
            if len(path) == k:
                result.append(path)
                return

            for i in range(start, n + 1):  # 리스트 vs 숫자 일 때 idx 생각 주의
                path.append(i)
                backtrack(i + 1, path[:])
                path.pop()

        result = []
        backtrack(1, [])  # start 지정
        return result
