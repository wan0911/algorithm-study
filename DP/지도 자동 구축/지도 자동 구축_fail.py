from sys import stdin

N = int(stdin.readline())

dp = [0] * 16
dp[1] = 4
dp[2] = 9

for i in range(3, 16):
    idx = i - 2
    dp[i] = dp[i-1] + (5*(4**idx) - 4**idx)


print(dp[N+1])

""" 점이 늘어가는 규칙을 찾으려 했다 """