from sys import stdin

# 데이터 셋
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4, 101):
    d[i] = d[i-3] + d[i-2]


num = int(stdin.readline()) 
for i in range(num):
    n = int(stdin.readline())
    print(d[n])

