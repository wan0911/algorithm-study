from sys import stdin

# 데이터 셋
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

num = int(stdin.readline()) 
for i in range(num):
    n = int(stdin.readline())
    print(dp[n])

