from sys import stdin

n = int(stdin.readline()) 

# 데이터 셋 만들어 놓기
d = [0]  * 1001
d[1] = 1
d[2] = 2
for i in ragne(3, 10001):
    d[i] = d[i-2] + d[i-1]


print(d[n] % 1007)