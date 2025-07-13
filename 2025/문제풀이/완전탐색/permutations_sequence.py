class Solution(object):
    def getPermutation(self, n, k):
        # 주어진 숫자 배열에서 n(k 아님) 길이의 순열을 구하고, k번째 순열을 리턴
        num_list = [i for i in range(1, n + 1)]
        result = []
        def backtrack(ans):
            if len(result) == k:
                return

            if len(ans) == n:
                result.append(ans)
                return

            for num in num_list:
                if str(num) not in ans:
                    ans.append(str(num))
                    backtrack(ans[:])
                    ans.pop()

        backtrack([])
        # print(result)
        return "".join(result[-1])
