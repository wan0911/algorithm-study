from sys import stdin

M, N = map(int, stdin.readline().split())

res = []
for num in range(M, N + 1):
    # 에라토스테네스의 체
    if num <= 1:  # 1은 소수가 아님
        continue

    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break

    if flag:
        res.append(num)

print(*res, sep="\n")
