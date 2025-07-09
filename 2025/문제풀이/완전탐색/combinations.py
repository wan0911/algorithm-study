class Solution(object):
    def combine(self, n, k):
        # nCk = 4C2
        # n이니까 숫자순, n >= k
        ans = []

        def combinations(start, comb):
            # depth = r이면 stop
            if start > n or len(comb) == k:  # n == 1도 OK
                ans.append(comb)
                return  # 리턴 출력할건 없는듯?

            for j in range(start + 1, n + 1):
                comb.append(j)
                # print('chk', comb, ans)
                combinations(j, comb[:])  # deep copy 중요..
                comb.pop()  # backtracking
                # print(comb)

        for i in range(1, n + 1):
            combinations(i, [i])

        return ans
