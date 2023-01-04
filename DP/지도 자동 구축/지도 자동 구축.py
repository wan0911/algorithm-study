from sys import stdin

N = int(stdin.readline())

dp = [0] * 16
dp[0] = 2

for i in range(1, 16):
    dp[i] = dp[i-1] + (dp[i] - 1)

print(dp[N]**2)

"""점의 갯수 = 행렬 크기 nxn"""