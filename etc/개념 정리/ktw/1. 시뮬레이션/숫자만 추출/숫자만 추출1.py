import sys

input = sys.stdin.readline

num = 0  # 한 문자씩 단위가 되므로
for w in input():
    if w.isdigit():
        num = num * 10 + int(w)

cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1

print(cnt)

"""
g0en2Ts8eSoft
"""
