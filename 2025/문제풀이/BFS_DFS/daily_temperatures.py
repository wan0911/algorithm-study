# 더 깔끔한 풀이
class Solution(object):
    def dailyTemperatures(self, temperatures):
        temp_stack = []  # stack
        ans = [0 for _ in range(len(temperatures))]
        for day, curr_temp in enumerate(temperatures):
            # 마지막거와 비교해서 stack 진행?
            while temp_stack and temp_stack[-1][1] < curr_temp:
                prev_day = temp_stack.pop()[0]
                ans[prev_day] = day - prev_day  # time은 idx끼리 비교하면 됨
            temp_stack.append([day, curr_temp])

        # print(ans)
        return ans


"""
# 내가 다시 푼 풀이
class Solution(object):
    def dailyTemperatures(self, temperatures):
        temp_stack = [] # stack
        ans = [0 for _ in range(len(temperatures))]
        # [] 73
        # [73] 74 -> [1, ]
        # [74] 75  
        # [75] 71
        # [75, 71, 69] 72
        # [73,74,75,71,69,72,76,73]
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while temp_stack:
                # print(temp_stack)
                temp, j = temp_stack[-1]
                if temp >= curr_temp: # 마지막거와 비교해서 stack 진행? + 부등호 비교 주의
                    break
                ans[j] = i - j # time은 idx끼리 비교하면 됨 
                temp_stack.pop()
            temp_stack.append([curr_temp, i])

        # print(ans)
        return ans
"""
